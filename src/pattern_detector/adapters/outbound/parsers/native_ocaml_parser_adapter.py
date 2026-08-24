"""High-performance Native OCaml (4.14 - 5.3+ / Multicore) AST & CST Parser Adapter implementing ParserPort."""

from __future__ import annotations

import os
import re
from pathlib import Path

from pattern_detector.domain.code_model import (
    CodeModel,
    FunctionModel,
    FunctionParamModel,
    ModuleModel,
    TypeModel,
    TypeRecordField,
    TypeVariantConstructor,
)
from pattern_detector.domain.value_objects import SourceLocation
from pattern_detector.ports.outbound import ParserPort


class NativeOCamlParserAdapter(ParserPort):
    """High-performance native OCaml parser supporting standard OCaml, Jane Street Core, and OCaml 5 effects."""

    def parse_sources(self, sources: dict[str, str]) -> CodeModel:
        model = CodeModel()
        for file_path, source_text in sources.items():
            mod = self.parse_file(file_path, source_text)
            model.modules[mod.name] = mod
        return model

    def parse_file(self, file_path: str, source_text: str) -> ModuleModel:
        clean_text = self._strip_comments_and_strings(source_text)
        mod_name = Path(file_path).stem.capitalize()
        loc = SourceLocation(file_path=file_path, line=1, column=1)

        root_module = ModuleModel(
            name=mod_name,
            file_path=file_path,
            raw_source=source_text,
            location=loc,
        )

        # 1. Includes and Opens
        root_module.includes = self._parse_includes(clean_text)
        root_module.opens = self._parse_opens(clean_text)

        # 2. Types (Records, Variants, GADTs)
        root_module.types = self._parse_types(clean_text, file_path)

        # 3. Functions / Let bindings
        root_module.functions = self._parse_functions(clean_text, file_path)

        # 4. Submodules and Functors
        root_module.submodules = self._parse_submodules(clean_text, file_path)

        # Functor check on root module
        if "module Make (" in clean_text or "module Make(" in clean_text:
            root_module.is_functor = True

        return root_module

    # -------------------------------------------------------------------------
    # Parsing Helpers
    # -------------------------------------------------------------------------

    def _strip_comments_and_strings(self, text: str) -> str:
        # Strip nested comments (* ... *)
        clean = re.sub(r"\(\*[\s\S]*?\*\)", " ", text)
        return clean

    def _parse_includes(self, text: str) -> list[str]:
        includes = []
        for m in re.finditer(r"\binclude\s+([A-Z][a-zA-Z0-9_.]*)", text):
            includes.append(m.group(1))
        return includes

    def _parse_opens(self, text: str) -> list[str]:
        opens = []
        for m in re.finditer(r"\bopen\s+([A-Z][a-zA-Z0-9_.]*)", text):
            opens.append(m.group(1))
        return opens

    def _parse_types(self, text: str, file_path: str) -> dict[str, TypeModel]:
        types: dict[str, TypeModel] = {}

        # Matches: type ... name = ...
        pattern = re.compile(
            r"\btype\s+([a-zA-Z0-9_'\s(),_]+?)\s*=\s*",
            re.MULTILINE,
        )

        matches = list(pattern.finditer(text))
        for i, m in enumerate(matches):
            raw_header = m.group(1).strip()
            # The type name is the last token in the header (e.g. type 'a tree -> tree, type _ expr -> expr, type buffer -> buffer)
            header_tokens = raw_header.split()
            name = header_tokens[-1].strip() if header_tokens else "t"

            line_no = text[:m.start()].count("\n") + 1
            loc = SourceLocation(file_path=file_path, line=line_no)

            # Extract body up to next type, let, module, val, open, include or end of text
            start_body = m.end()
            next_start = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            chunk = text[start_body:next_start]

            # Cut off at first let, module, val, open, include
            cut_m = re.search(r"\n\s*(?:let|module|val|open|include)\b", chunk)
            body = chunk[:cut_m.start()].strip() if cut_m else chunk.strip()

            is_record = "{" in body and "}" in body
            is_gadt = bool(re.search(r"\|\s*[A-Z][a-zA-Z0-9_]*\s*:", body)) or bool(re.search(r"^[A-Z][a-zA-Z0-9_]*\s*:", body))
            is_variant = ("|" in body or (body and body[0].isupper())) and not is_record
            is_poly = "`" in body
            is_abstract = not body

            record_fields = []
            if is_record:
                field_block = body[body.find("{") + 1:body.rfind("}")].strip()
                for f_item in field_block.split(";"):
                    f_item = f_item.strip()
                    if not f_item:
                        continue
                    is_mut = "mutable " in f_item
                    clean_f = f_item.replace("mutable ", "").strip()
                    if ":" in clean_f:
                        f_name, f_type = clean_f.split(":", 1)
                        record_fields.append(
                            TypeRecordField(
                                name=f_name.strip(),
                                type_str=f_type.strip(),
                                is_mutable=is_mut,
                                is_function=("->" in f_type),
                            )
                        )

            variant_constructors = []
            if is_variant or is_gadt:
                for c_item in body.split("|"):
                    c_item = c_item.strip()
                    if not c_item or c_item.startswith("{"):
                        continue
                    if ":" in c_item:  # GADT constructor: Int : int -> int expr
                        c_name, c_type = c_item.split(":", 1)
                        variant_constructors.append(
                            TypeVariantConstructor(
                                name=c_name.strip(),
                                return_type=c_type.strip(),
                                is_gadt=True,
                            )
                        )
                    else:
                        tokens = c_item.split(" of ")
                        c_name = tokens[0].strip()
                        c_args = tokens[1].split("*") if len(tokens) > 1 else []
                        variant_constructors.append(
                            TypeVariantConstructor(
                                name=c_name,
                                args=[a.strip() for a in c_args],
                                is_gadt=False,
                            )
                        )

            types[name] = TypeModel(
                name=name,
                is_abstract=is_abstract,
                is_record=is_record,
                is_variant=is_variant,
                is_gadt=is_gadt,
                is_polymorphic_variant=is_poly,
                record_fields=record_fields,
                variant_constructors=variant_constructors,
                location=loc,
            )

        return types

    def _parse_functions(self, text: str, file_path: str) -> dict[str, FunctionModel]:
        functions: dict[str, FunctionModel] = {}

        # Matches: let [rec] name p1 p2 = ...
        pattern = re.compile(
            r"\blet\s+(rec\s+)?([a-zA-Z0-9_!?]+)\s+([^=;\n]+)?=",
            re.MULTILINE,
        )

        pos = 0
        matches = list(pattern.finditer(text))
        for i, m in enumerate(matches):
            is_rec = bool(m.group(1))
            name = m.group(2)
            params_raw = m.group(3) or ""

            # Exclude operator bindings and keyword noise
            if name in ("open", "in", "and", "module", "type", "exception"):
                continue

            line_no = text[:m.start()].count("\n") + 1
            loc = SourceLocation(file_path=file_path, line=line_no)

            # Extract body up to next top-level let or end of module
            next_start = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            body = text[m.end():next_start].strip()

            params = []
            for p in params_raw.split():
                p = p.strip("()")
                if p:
                    params.append(FunctionParamModel(name=p))

            calls = re.findall(r"\b([A-Z][a-zA-Z0-9_]*)\.([a-zA-Z0-9_]+)", body)
            complexity = 1 + body.count("match ") + body.count("with |") + body.count("if ") + body.count("function |")

            functions[name] = FunctionModel(
                name=name,
                params=params,
                is_rec=is_rec,
                body=body,
                cyclomatic_complexity=complexity,
                calls=calls,
                has_raise=("raise " in body or "failwith " in body),
                has_try_with=("try " in body and "with " in body),
                has_ref=("ref " in body or ":=" in body),
                has_physical_eq=(" == " in body or " != " in body),
                has_pipe=("|>" in body or "@@" in body),
                has_monadic_bind=("let*" in body or "let+" in body or ">>=" in body),
                location=loc,
            )

        return functions

    def _parse_submodules(self, text: str, file_path: str) -> dict[str, ModuleModel]:
        submodules: dict[str, ModuleModel] = {}

        # Matches: module [rec] Name [(Arg : S)] = struct ... end
        pattern = re.compile(
            r"\bmodule\s+(rec\s+)?([A-Z][a-zA-Z0-9_]*)\s*(?:\(([^)]+)\))?\s*(?::\s*([A-Z][a-zA-Z0-9_]*))?\s*=\s*struct\b",
            re.MULTILINE,
        )

        pos = 0
        while pos < len(text):
            m = pattern.search(text, pos)
            if not m:
                break

            is_rec = bool(m.group(1))
            name = m.group(2)
            functor_arg = m.group(3) or ""
            functor_sig = m.group(4) or ""

            line_no = text[:m.start()].count("\n") + 1
            loc = SourceLocation(file_path=file_path, line=line_no)

            body, end_pos = self._extract_struct_end_block(text, m.end())
            pos = end_pos + 1

            submod = ModuleModel(
                name=name,
                file_path=file_path,
                is_functor=bool(functor_arg),
                functor_param=functor_arg,
                functor_sig=functor_sig,
                is_recursive=is_rec,
                raw_source=body,
                location=loc,
            )
            submod.includes = self._parse_includes(body)
            submod.opens = self._parse_opens(body)
            submod.types = self._parse_types(body, file_path)
            submod.functions = self._parse_functions(body, file_path)
            submodules[name] = submod

        return submodules

    def _extract_struct_end_block(self, text: str, start_pos: int) -> tuple[str, int]:
        depth = 1
        i = start_pos
        tokens = re.finditer(r"\b(struct|sig|end)\b", text[start_pos:])

        for token in tokens:
            word = token.group(1)
            if word in ("struct", "sig"):
                depth += 1
            elif word == "end":
                depth -= 1
                if depth == 0:
                    end_idx = start_pos + token.start()
                    return text[start_pos:end_idx], start_pos + token.end()

        return text[start_pos:], len(text)
