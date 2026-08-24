# 🐫 DPX-OCaml: Module Architecture & Functional Pattern Report

- **Target Path:** `/Volumes/External/Code/vectis`
- **Files Scanned:** `121`
- **Total Patterns & Findings:** `920`
- **Analysis Elapsed Time:** `0.096s`

## 📊 Breakdown by Category

| Category | Count |
|---|:---:|
| **MODULE_SYSTEM** | 161 |
| **FUNCTIONAL_IDIOM** | 7 |
| **BEHAVIORAL** | 82 |
| **TYPE_SAFETY** | 29 |
| **RESILIENCE** | 12 |
| **PRINCIPLE** | 629 |

## 📋 Detailed Pattern Findings

### #1 FUNCTOR_PARAMETRIC_MODULE on `Two_tier_jit_usecase`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/application/two_tier_jit_usecase.ml:1:1`
- **Summary:** Module 'Two_tier_jit_usecase' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Two_tier_jit_usecase' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/application/two_tier_jit_usecase.ml:1:1`

### #2 FUNCTOR_PARAMETRIC_MODULE on `Obfuscate_c_source_usecase`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/application/obfuscate_c_source_usecase.ml:1:1`
- **Summary:** Module 'Obfuscate_c_source_usecase' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Obfuscate_c_source_usecase' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/application/obfuscate_c_source_usecase.ml:1:1`

### #3 FUNCTOR_PARAMETRIC_MODULE on `Synthesize_isa_usecase`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/application/synthesize_isa_usecase.ml:1:1`
- **Summary:** Module 'Synthesize_isa_usecase' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Synthesize_isa_usecase' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/application/synthesize_isa_usecase.ml:1:1`

### #4 FUNCTOR_PARAMETRIC_MODULE on `Obfuscation_pipeline`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/application/obfuscation_pipeline.ml:1:1`
- **Summary:** Module 'Obfuscation_pipeline' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Obfuscation_pipeline' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/application/obfuscation_pipeline.ml:1:1`

### #5 FUNCTOR_PARAMETRIC_MODULE on `Flattening_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:1:1`
- **Summary:** Module 'Flattening_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Flattening_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:1:1`

### #6 FUNCTOR_PARAMETRIC_MODULE on `Mba_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/mba_service.ml:1:1`
- **Summary:** Module 'Mba_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Mba_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/native/mba_service.ml:1:1`

### #7 FUNCTOR_PARAMETRIC_MODULE on `Opaque_predicate_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/opaque_predicate_service.ml:1:1`
- **Summary:** Module 'Opaque_predicate_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Opaque_predicate_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/native/opaque_predicate_service.ml:1:1`

### #8 FUNCTOR_PARAMETRIC_MODULE on `Two_tier_jit_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/two_tier_jit_service.ml:1:1`
- **Summary:** Module 'Two_tier_jit_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Two_tier_jit_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/native/two_tier_jit_service.ml:1:1`

### #9 FUNCTOR_PARAMETRIC_MODULE on `C_concurrent_fiber_runtime`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_concurrent_fiber_runtime.ml:1:1`
- **Summary:** Module 'C_concurrent_fiber_runtime' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_concurrent_fiber_runtime' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_concurrent_fiber_runtime.ml:1:1`

### #10 FUNCTOR_PARAMETRIC_MODULE on `C_isa_synthesizer_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:1:1`
- **Summary:** Module 'C_isa_synthesizer_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_isa_synthesizer_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:1:1`

### #11 FUNCTOR_PARAMETRIC_MODULE on `C_visa_decoy_generator`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_decoy_generator.ml:1:1`
- **Summary:** Module 'C_visa_decoy_generator' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_visa_decoy_generator' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_decoy_generator.ml:1:1`

### #12 FUNCTOR_PARAMETRIC_MODULE on `C_self_modifying_vm_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:1:1`
- **Summary:** Module 'C_self_modifying_vm_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_self_modifying_vm_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:1:1`

### #13 FUNCTOR_PARAMETRIC_MODULE on `C_rolling_vkey_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:1:1`
- **Summary:** Module 'C_rolling_vkey_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_rolling_vkey_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:1:1`

### #14 FUNCTOR_PARAMETRIC_MODULE on `C_arm64_jit_compiler`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:1:1`
- **Summary:** Module 'C_arm64_jit_compiler' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_arm64_jit_compiler' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:1:1`

### #15 FUNCTOR_PARAMETRIC_MODULE on `C_nested_vm_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:1:1`
- **Summary:** Module 'C_nested_vm_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_nested_vm_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:1:1`

### #16 FUNCTOR_PARAMETRIC_MODULE on `C_jitify_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:1:1`
- **Summary:** Module 'C_jitify_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_jitify_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:1:1`

### #17 FUNCTOR_PARAMETRIC_MODULE on `C_micro_dispatcher_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_micro_dispatcher_service.ml:1:1`
- **Summary:** Module 'C_micro_dispatcher_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_micro_dispatcher_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_micro_dispatcher_service.ml:1:1`

### #18 FUNCTOR_PARAMETRIC_MODULE on `C_vcpu_context_scramble_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:1:1`
- **Summary:** Module 'C_vcpu_context_scramble_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_vcpu_context_scramble_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:1:1`

### #19 FUNCTOR_PARAMETRIC_MODULE on `C_decentralized_dispatcher_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:1:1`
- **Summary:** Module 'C_decentralized_dispatcher_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_decentralized_dispatcher_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:1:1`

### #20 FUNCTOR_PARAMETRIC_MODULE on `C_vpc_path_invalidation_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vpc_path_invalidation_service.ml:1:1`
- **Summary:** Module 'C_vpc_path_invalidation_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_vpc_path_invalidation_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vpc_path_invalidation_service.ml:1:1`

### #21 FUNCTOR_PARAMETRIC_MODULE on `C_visa_spec_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:1:1`
- **Summary:** Module 'C_visa_spec_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_visa_spec_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:1:1`

### #22 FUNCTOR_PARAMETRIC_MODULE on `C_visa_stmt_compiler`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_stmt_compiler.ml:1:1`
- **Summary:** Module 'C_visa_stmt_compiler' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_visa_stmt_compiler' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_stmt_compiler.ml:1:1`

### #23 FUNCTOR_PARAMETRIC_MODULE on `C_virtualize_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:1:1`
- **Summary:** Module 'C_virtualize_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_virtualize_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:1:1`

### #24 FUNCTOR_PARAMETRIC_MODULE on `C_visa_expr_compiler`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_expr_compiler.ml:1:1`
- **Summary:** Module 'C_visa_expr_compiler' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_visa_expr_compiler' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_expr_compiler.ml:1:1`

### #25 FUNCTOR_PARAMETRIC_MODULE on `C_bogus_calls_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_bogus_calls_service.ml:1:1`
- **Summary:** Module 'C_bogus_calls_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_bogus_calls_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_bogus_calls_service.ml:1:1`

### #26 FUNCTOR_PARAMETRIC_MODULE on `C_call_graph_flatten_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_call_graph_flatten_service.ml:1:1`
- **Summary:** Module 'C_call_graph_flatten_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_call_graph_flatten_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_call_graph_flatten_service.ml:1:1`

### #27 FUNCTOR_PARAMETRIC_MODULE on `C_outline_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_outline_service.ml:1:1`
- **Summary:** Module 'C_outline_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_outline_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_outline_service.ml:1:1`

### #28 FUNCTOR_PARAMETRIC_MODULE on `C_merge_functions_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_merge_functions_service.ml:1:1`
- **Summary:** Module 'C_merge_functions_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_merge_functions_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_merge_functions_service.ml:1:1`

### #29 FUNCTOR_PARAMETRIC_MODULE on `C_inline_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_inline_service.ml:1:1`
- **Summary:** Module 'C_inline_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_inline_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_inline_service.ml:1:1`

### #30 FUNCTOR_PARAMETRIC_MODULE on `C_pointer_masking_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_pointer_masking_service.ml:1:1`
- **Summary:** Module 'C_pointer_masking_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_pointer_masking_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_pointer_masking_service.ml:1:1`

### #31 FUNCTOR_PARAMETRIC_MODULE on `C_struct_permute_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_struct_permute_service.ml:1:1`
- **Summary:** Module 'C_struct_permute_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_struct_permute_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_struct_permute_service.ml:1:1`

### #32 FUNCTOR_PARAMETRIC_MODULE on `C_bpm_mba_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_bpm_mba_service.ml:1:1`
- **Summary:** Module 'C_bpm_mba_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_bpm_mba_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_bpm_mba_service.ml:1:1`

### #33 FUNCTOR_PARAMETRIC_MODULE on `C_mba_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:1:1`
- **Summary:** Module 'C_mba_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_mba_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:1:1`

### #34 FUNCTOR_PARAMETRIC_MODULE on `C_float_mba_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_float_mba_service.ml:1:1`
- **Summary:** Module 'C_float_mba_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_float_mba_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_float_mba_service.ml:1:1`

### #35 FUNCTOR_PARAMETRIC_MODULE on `C_encode_literals_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:1:1`
- **Summary:** Module 'C_encode_literals_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_encode_literals_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:1:1`

### #36 FUNCTOR_PARAMETRIC_MODULE on `C_array_interleave_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_array_interleave_service.ml:1:1`
- **Summary:** Module 'C_array_interleave_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_array_interleave_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_array_interleave_service.ml:1:1`

### #37 FUNCTOR_PARAMETRIC_MODULE on `C_homomorphic_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_homomorphic_service.ml:1:1`
- **Summary:** Module 'C_homomorphic_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_homomorphic_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_homomorphic_service.ml:1:1`

### #38 FUNCTOR_PARAMETRIC_MODULE on `C_encode_data_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_data_service.ml:1:1`
- **Summary:** Module 'C_encode_data_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_encode_data_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_data_service.ml:1:1`

### #39 FUNCTOR_PARAMETRIC_MODULE on `C_egraph_mba_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:1:1`
- **Summary:** Module 'C_egraph_mba_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_egraph_mba_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:1:1`

### #40 FUNCTOR_PARAMETRIC_MODULE on `C_lut_arithmetic_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_lut_arithmetic_service.ml:1:1`
- **Summary:** Module 'C_lut_arithmetic_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_lut_arithmetic_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_lut_arithmetic_service.ml:1:1`

### #41 FUNCTOR_PARAMETRIC_MODULE on `C_polynomial_mba_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_polynomial_mba_service.ml:1:1`
- **Summary:** Module 'C_polynomial_mba_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_polynomial_mba_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_polynomial_mba_service.ml:1:1`

### #42 FUNCTOR_PARAMETRIC_MODULE on `C_loki_invariant_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_loki_invariant_service.ml:1:1`
- **Summary:** Module 'C_loki_invariant_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_loki_invariant_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_loki_invariant_service.ml:1:1`

### #43 FUNCTOR_PARAMETRIC_MODULE on `C_instruction_permute_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_instruction_permute_service.ml:1:1`
- **Summary:** Module 'C_instruction_permute_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_instruction_permute_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_instruction_permute_service.ml:1:1`

### #44 FUNCTOR_PARAMETRIC_MODULE on `C_ghost_code_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_ghost_code_service.ml:1:1`
- **Summary:** Module 'C_ghost_code_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_ghost_code_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_ghost_code_service.ml:1:1`

### #45 FUNCTOR_PARAMETRIC_MODULE on `C_constant_unfold_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_constant_unfold_service.ml:1:1`
- **Summary:** Module 'C_constant_unfold_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_constant_unfold_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_constant_unfold_service.ml:1:1`

### #46 FUNCTOR_PARAMETRIC_MODULE on `C_relational_morph_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_relational_morph_service.ml:1:1`
- **Summary:** Module 'C_relational_morph_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_relational_morph_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_relational_morph_service.ml:1:1`

### #47 FUNCTOR_PARAMETRIC_MODULE on `C_stack_aliasing_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_stack_aliasing_service.ml:1:1`
- **Summary:** Module 'C_stack_aliasing_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_stack_aliasing_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_stack_aliasing_service.ml:1:1`

### #48 FUNCTOR_PARAMETRIC_MODULE on `C_opcode_equalize_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_opcode_equalize_service.ml:1:1`
- **Summary:** Module 'C_opcode_equalize_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_opcode_equalize_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_opcode_equalize_service.ml:1:1`

### #49 FUNCTOR_PARAMETRIC_MODULE on `C_instruction_subst_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_instruction_subst_service.ml:1:1`
- **Summary:** Module 'C_instruction_subst_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_instruction_subst_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_instruction_subst_service.ml:1:1`

### #50 FUNCTOR_PARAMETRIC_MODULE on `C_live_range_split_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_live_range_split_service.ml:1:1`
- **Summary:** Module 'C_live_range_split_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_live_range_split_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_live_range_split_service.ml:1:1`

### #51 FUNCTOR_PARAMETRIC_MODULE on `C_anti_slicing_entanglement_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:1:1`
- **Summary:** Module 'C_anti_slicing_entanglement_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_anti_slicing_entanglement_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:1:1`

### #52 FUNCTOR_PARAMETRIC_MODULE on `C_loop_to_recursion_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_loop_to_recursion_service.ml:1:1`
- **Summary:** Module 'C_loop_to_recursion_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_loop_to_recursion_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_loop_to_recursion_service.ml:1:1`

### #53 FUNCTOR_PARAMETRIC_MODULE on `C_ephemeral_payload_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:1:1`
- **Summary:** Module 'C_ephemeral_payload_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_ephemeral_payload_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:1:1`

### #54 FUNCTOR_PARAMETRIC_MODULE on `C_early_constructor_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_early_constructor_service.ml:1:1`
- **Summary:** Module 'C_early_constructor_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_early_constructor_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_early_constructor_service.ml:1:1`

### #55 FUNCTOR_PARAMETRIC_MODULE on `C_api_hash_resolver_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_api_hash_resolver_service.ml:1:1`
- **Summary:** Module 'C_api_hash_resolver_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_api_hash_resolver_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_api_hash_resolver_service.ml:1:1`

### #56 FUNCTOR_PARAMETRIC_MODULE on `C_rename_symbols_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/symbols/c_rename_symbols_service.ml:1:1`
- **Summary:** Module 'C_rename_symbols_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_rename_symbols_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/symbols/c_rename_symbols_service.ml:1:1`

### #57 FUNCTOR_PARAMETRIC_MODULE on `C_strip_directives_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/symbols/c_strip_directives_service.ml:1:1`
- **Summary:** Module 'C_strip_directives_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_strip_directives_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/symbols/c_strip_directives_service.ml:1:1`

### #58 FUNCTOR_PARAMETRIC_MODULE on `C_threaded_implicit_flow_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_threaded_implicit_flow_service.ml:1:1`
- **Summary:** Module 'C_threaded_implicit_flow_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_threaded_implicit_flow_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_threaded_implicit_flow_service.ml:1:1`

### #59 FUNCTOR_PARAMETRIC_MODULE on `C_sigfpe_flow_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:1:1`
- **Summary:** Module 'C_sigfpe_flow_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_sigfpe_flow_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:1:1`

### #60 FUNCTOR_PARAMETRIC_MODULE on `C_sigill_flow_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigill_flow_service.ml:1:1`
- **Summary:** Module 'C_sigill_flow_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_sigill_flow_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigill_flow_service.ml:1:1`

### #61 FUNCTOR_PARAMETRIC_MODULE on `C_implicit_flow_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:1:1`
- **Summary:** Module 'C_implicit_flow_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_implicit_flow_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:1:1`

### #62 FUNCTOR_PARAMETRIC_MODULE on `C_syscall_error_flow_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_syscall_error_flow_service.ml:1:1`
- **Summary:** Module 'C_syscall_error_flow_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_syscall_error_flow_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_syscall_error_flow_service.ml:1:1`

### #63 FUNCTOR_PARAMETRIC_MODULE on `C_flattening_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:1:1`
- **Summary:** Module 'C_flattening_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_flattening_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:1:1`

### #64 FUNCTOR_PARAMETRIC_MODULE on `C_diophantine_opaque_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_diophantine_opaque_service.ml:1:1`
- **Summary:** Module 'C_diophantine_opaque_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_diophantine_opaque_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_diophantine_opaque_service.ml:1:1`

### #65 FUNCTOR_PARAMETRIC_MODULE on `C_loop_unroll_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_unroll_service.ml:1:1`
- **Summary:** Module 'C_loop_unroll_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_loop_unroll_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_unroll_service.ml:1:1`

### #66 FUNCTOR_PARAMETRIC_MODULE on `C_basic_block_split_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:1:1`
- **Summary:** Module 'C_basic_block_split_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_basic_block_split_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:1:1`

### #67 FUNCTOR_PARAMETRIC_MODULE on `C_bogus_control_flow_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_bogus_control_flow_service.ml:1:1`
- **Summary:** Module 'C_bogus_control_flow_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_bogus_control_flow_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_bogus_control_flow_service.ml:1:1`

### #68 FUNCTOR_PARAMETRIC_MODULE on `C_irreducible_loop_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:1:1`
- **Summary:** Module 'C_irreducible_loop_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_irreducible_loop_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:1:1`

### #69 FUNCTOR_PARAMETRIC_MODULE on `C_opaque_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_opaque_service.ml:1:1`
- **Summary:** Module 'C_opaque_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_opaque_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_opaque_service.ml:1:1`

### #70 FUNCTOR_PARAMETRIC_MODULE on `C_indirect_jump_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:1:1`
- **Summary:** Module 'C_indirect_jump_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_indirect_jump_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:1:1`

### #71 FUNCTOR_PARAMETRIC_MODULE on `C_loop_fission_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_fission_service.ml:1:1`
- **Summary:** Module 'C_loop_fission_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_loop_fission_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_fission_service.ml:1:1`

### #72 FUNCTOR_PARAMETRIC_MODULE on `C_dynamic_opaque_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_dynamic_opaque_service.ml:1:1`
- **Summary:** Module 'C_dynamic_opaque_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_dynamic_opaque_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_dynamic_opaque_service.ml:1:1`

### #73 FUNCTOR_PARAMETRIC_MODULE on `C_self_checksum_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_self_checksum_service.ml:1:1`
- **Summary:** Module 'C_self_checksum_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_self_checksum_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_self_checksum_service.ml:1:1`

### #74 FUNCTOR_PARAMETRIC_MODULE on `C_anti_vtil_aliasing_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_vtil_aliasing_service.ml:1:1`
- **Summary:** Module 'C_anti_vtil_aliasing_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_anti_vtil_aliasing_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_vtil_aliasing_service.ml:1:1`

### #75 FUNCTOR_PARAMETRIC_MODULE on `C_anti_disassembly_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_disassembly_service.ml:1:1`
- **Summary:** Module 'C_anti_disassembly_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_anti_disassembly_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_disassembly_service.ml:1:1`

### #76 FUNCTOR_PARAMETRIC_MODULE on `C_anti_debug_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_debug_service.ml:1:1`
- **Summary:** Module 'C_anti_debug_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_anti_debug_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_debug_service.ml:1:1`

### #77 FUNCTOR_PARAMETRIC_MODULE on `C_eh_shadowing_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_eh_shadowing_service.ml:1:1`
- **Summary:** Module 'C_eh_shadowing_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_eh_shadowing_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_eh_shadowing_service.ml:1:1`

### #78 FUNCTOR_PARAMETRIC_MODULE on `C_hook_detect_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_hook_detect_service.ml:1:1`
- **Summary:** Module 'C_hook_detect_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_hook_detect_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_hook_detect_service.ml:1:1`

### #79 FUNCTOR_PARAMETRIC_MODULE on `C_timing_check_service`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_timing_check_service.ml:1:1`
- **Summary:** Module 'C_timing_check_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'C_timing_check_service' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_timing_check_service.ml:1:1`

### #80 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/application/synthesize_isa_usecase.ml:3:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/application/synthesize_isa_usecase.ml:3:1`

### #81 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/application/obfuscation_pipeline.ml:15:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/application/obfuscation_pipeline.ml:15:1`

### #82 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:6:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:6:1`

### #83 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/mba_service.ml:6:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/native/mba_service.ml:6:1`

### #84 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/opaque_predicate_service.ml:6:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/native/opaque_predicate_service.ml:6:1`

### #85 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_concurrent_fiber_runtime.ml:5:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_concurrent_fiber_runtime.ml:5:1`

### #86 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:4:1`

### #87 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_decoy_generator.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_decoy_generator.ml:4:1`

### #88 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:4:1`

### #89 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:4:1`

### #90 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:4:1`

### #91 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:4:1`

### #92 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:4:1`

### #93 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_micro_dispatcher_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_micro_dispatcher_service.ml:4:1`

### #94 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:4:1`

### #95 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:4:1`

### #96 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vpc_path_invalidation_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vpc_path_invalidation_service.ml:4:1`

### #97 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:6:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:6:1`

### #98 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_stmt_compiler.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_stmt_compiler.ml:4:1`

### #99 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:4:1`

### #100 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_expr_compiler.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_expr_compiler.ml:4:1`

### #101 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_bogus_calls_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_bogus_calls_service.ml:4:1`

### #102 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_call_graph_flatten_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_call_graph_flatten_service.ml:4:1`

### #103 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_outline_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_outline_service.ml:4:1`

### #104 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_merge_functions_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_merge_functions_service.ml:4:1`

### #105 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_inline_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_inline_service.ml:4:1`

### #106 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_pointer_masking_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_pointer_masking_service.ml:4:1`

### #107 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_struct_permute_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_struct_permute_service.ml:4:1`

### #108 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_bpm_mba_service.ml:5:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_bpm_mba_service.ml:5:1`

### #109 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:4:1`

### #110 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_float_mba_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_float_mba_service.ml:4:1`

### #111 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:4:1`

### #112 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_array_interleave_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_array_interleave_service.ml:4:1`

### #113 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_homomorphic_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_homomorphic_service.ml:4:1`

### #114 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_data_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_data_service.ml:4:1`

### #115 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:4:1`

### #116 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_lut_arithmetic_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_lut_arithmetic_service.ml:4:1`

### #117 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_polynomial_mba_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_polynomial_mba_service.ml:4:1`

### #118 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_loki_invariant_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_loki_invariant_service.ml:4:1`

### #119 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_instruction_permute_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_instruction_permute_service.ml:4:1`

### #120 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_ghost_code_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_ghost_code_service.ml:4:1`

### #121 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_constant_unfold_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_constant_unfold_service.ml:4:1`

### #122 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_relational_morph_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_relational_morph_service.ml:4:1`

### #123 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_stack_aliasing_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_stack_aliasing_service.ml:4:1`

### #124 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_opcode_equalize_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_opcode_equalize_service.ml:4:1`

### #125 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_instruction_subst_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_instruction_subst_service.ml:4:1`

### #126 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_live_range_split_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_live_range_split_service.ml:4:1`

### #127 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:4:1`

### #128 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_loop_to_recursion_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_loop_to_recursion_service.ml:4:1`

### #129 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:4:1`

### #130 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_early_constructor_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_early_constructor_service.ml:4:1`

### #131 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_api_hash_resolver_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_api_hash_resolver_service.ml:4:1`

### #132 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/symbols/c_rename_symbols_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/symbols/c_rename_symbols_service.ml:4:1`

### #133 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/symbols/c_strip_directives_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/symbols/c_strip_directives_service.ml:4:1`

### #134 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_threaded_implicit_flow_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_threaded_implicit_flow_service.ml:4:1`

### #135 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:4:1`

### #136 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigill_flow_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigill_flow_service.ml:4:1`

### #137 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:4:1`

### #138 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_syscall_error_flow_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_syscall_error_flow_service.ml:4:1`

### #139 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:4:1`

### #140 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_diophantine_opaque_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_diophantine_opaque_service.ml:4:1`

### #141 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_unroll_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_unroll_service.ml:4:1`

### #142 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:4:1`

### #143 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_bogus_control_flow_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_bogus_control_flow_service.ml:4:1`

### #144 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:4:1`

### #145 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_opaque_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_opaque_service.ml:4:1`

### #146 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:4:1`

### #147 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_fission_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_fission_service.ml:4:1`

### #148 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_dynamic_opaque_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_dynamic_opaque_service.ml:4:1`

### #149 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_self_checksum_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_self_checksum_service.ml:4:1`

### #150 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_vtil_aliasing_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_vtil_aliasing_service.ml:4:1`

### #151 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_disassembly_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_disassembly_service.ml:4:1`

### #152 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_debug_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_debug_service.ml:4:1`

### #153 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_eh_shadowing_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_eh_shadowing_service.ml:4:1`

### #154 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_hook_detect_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_hook_detect_service.ml:4:1`

### #155 FUNCTOR_PARAMETRIC_MODULE on `Make`
- **Category:** `module_system`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_timing_check_service.ml:4:1`
- **Summary:** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection

#### Evidence Trail:
- `+85%` **[FUNCTOR_PARAMETRIC_MODULE]** Module 'Make' implements Functor Parametric Module pattern enabling compile-time type parameterization and dependency injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_timing_check_service.ml:4:1`

### #156 ABSTRACT_DATA_TYPE_INTERFACE on `Vectis_state_masking`
- **Category:** `module_system`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:1:1`
- **Summary:** Module 'Vectis_state_masking' encapsulates Abstract Data Type (ADT) via primary type `t` with constructor 'create'

#### Evidence Trail:
- `+80%` **[ABSTRACT_DATA_TYPE_SIGNATURE]** Module 'Vectis_state_masking' encapsulates Abstract Data Type (ADT) via primary type `t` with constructor 'create' -> `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:1:1`

### #157 ABSTRACT_DATA_TYPE_INTERFACE on `Cfg`
- **Category:** `module_system`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/cfg.ml:1:1`
- **Summary:** Module 'Cfg' encapsulates Abstract Data Type (ADT) via primary type `t` with constructor 'create'

#### Evidence Trail:
- `+80%` **[ABSTRACT_DATA_TYPE_SIGNATURE]** Module 'Cfg' encapsulates Abstract Data Type (ADT) via primary type `t` with constructor 'create' -> `/Volumes/External/Code/vectis/lib/domain/cfg.ml:1:1`

### #158 ABSTRACT_DATA_TYPE_INTERFACE on `Stepper`
- **Category:** `module_system`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:62:1`
- **Summary:** Module 'Stepper' encapsulates Abstract Data Type (ADT) via primary type `t` with constructor 'create'

#### Evidence Trail:
- `+80%` **[ABSTRACT_DATA_TYPE_SIGNATURE]** Module 'Stepper' encapsulates Abstract Data Type (ADT) via primary type `t` with constructor 'create' -> `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:62:1`

### #159 ABSTRACT_DATA_TYPE_INTERFACE on `BasicBlock`
- **Category:** `module_system`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/cfg.ml:4:1`
- **Summary:** Module 'BasicBlock' encapsulates Abstract Data Type (ADT) via primary type `t` with constructor 'create'

#### Evidence Trail:
- `+80%` **[ABSTRACT_DATA_TYPE_SIGNATURE]** Module 'BasicBlock' encapsulates Abstract Data Type (ADT) via primary type `t` with constructor 'create' -> `/Volumes/External/Code/vectis/lib/domain/cfg.ml:4:1`

### #160 ABSTRACT_DATA_TYPE_INTERFACE on `CFG`
- **Category:** `module_system`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/cfg.ml:13:1`
- **Summary:** Module 'CFG' encapsulates Abstract Data Type (ADT) via primary type `t` with constructor 'create'

#### Evidence Trail:
- `+80%` **[ABSTRACT_DATA_TYPE_SIGNATURE]** Module 'CFG' encapsulates Abstract Data Type (ADT) via primary type `t` with constructor 'create' -> `/Volumes/External/Code/vectis/lib/domain/cfg.ml:13:1`

### #161 MODULE_INCLUSION_EXTENDER on `System_entropy_adapter`
- **Category:** `module_system`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/infrastructure/random/system_entropy_adapter.ml:1:1`
- **Summary:** Module 'System_entropy_adapter' extends and composes functionality from 1 included module(s) (Entropy_port.S)

#### Evidence Trail:
- `+80%` **[MODULE_INCLUSION_EXTENSION]** Module 'System_entropy_adapter' extends and composes functionality from 1 included module(s) (Entropy_port.S) -> `/Volumes/External/Code/vectis/lib/infrastructure/random/system_entropy_adapter.ml:1:1`

### #162 POLYMORPHIC_VARIANTS on `C_visa_c_handlers`
- **Category:** `functional_idiom`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_visa_c_handlers.ml:1:1`
- **Summary:** Module 'C_visa_c_handlers' adopts Polymorphic Variants (``ZeroLogic, ``Nop) providing open tag subtyping without nominal declarations

#### Evidence Trail:
- `+80%` **[POLYMORPHIC_OPEN_VARIANTS]** Module 'C_visa_c_handlers' adopts Polymorphic Variants (``ZeroLogic, ``Nop) providing open tag subtyping without nominal declarations -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_visa_c_handlers.ml:1:1`

### #163 POLYMORPHIC_VARIANTS on `C_visa_spec`
- **Category:** `functional_idiom`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_spec.ml:1:1`
- **Summary:** Module 'C_visa_spec' adopts Polymorphic Variants (``String, ``Int) providing open tag subtyping without nominal declarations

#### Evidence Trail:
- `+80%` **[POLYMORPHIC_OPEN_VARIANTS]** Module 'C_visa_spec' adopts Polymorphic Variants (``String, ``Int) providing open tag subtyping without nominal declarations -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_spec.ml:1:1`

### #164 POLYMORPHIC_VARIANTS on `C_arm64_jit_compiler`
- **Category:** `functional_idiom`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:1:1`
- **Summary:** Module 'C_arm64_jit_compiler' adopts Polymorphic Variants (``Eq, ``Ne) providing open tag subtyping without nominal declarations

#### Evidence Trail:
- `+80%` **[POLYMORPHIC_OPEN_VARIANTS]** Module 'C_arm64_jit_compiler' adopts Polymorphic Variants (``Eq, ``Ne) providing open tag subtyping without nominal declarations -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:1:1`

### #165 POLYMORPHIC_VARIANTS on `C_arm64_edsl`
- **Category:** `functional_idiom`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_edsl.ml:1:1`
- **Summary:** Module 'C_arm64_edsl' adopts Polymorphic Variants (``ZeroLogic, ``Nop) providing open tag subtyping without nominal declarations

#### Evidence Trail:
- `+80%` **[POLYMORPHIC_OPEN_VARIANTS]** Module 'C_arm64_edsl' adopts Polymorphic Variants (``ZeroLogic, ``Nop) providing open tag subtyping without nominal declarations -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_edsl.ml:1:1`

### #166 POLYMORPHIC_VARIANTS on `Make`
- **Category:** `functional_idiom`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:4:1`
- **Summary:** Module 'Make' adopts Polymorphic Variants (``Eq, ``Ne) providing open tag subtyping without nominal declarations

#### Evidence Trail:
- `+80%` **[POLYMORPHIC_OPEN_VARIANTS]** Module 'Make' adopts Polymorphic Variants (``Eq, ``Ne) providing open tag subtyping without nominal declarations -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:4:1`

### #167 PIPELINE_OPERATOR on `C_visa_spec.layout`
- **Category:** `functional_idiom`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_spec.ml:178:1`
- **Summary:** Function 'layout' composes functional data transformations across a 16-stage pipe (`|>`)

#### Evidence Trail:
- `+75%` **[PIPELINE_OPERATOR_CHAIN]** Function 'layout' composes functional data transformations across a 16-stage pipe (`|>`) -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_spec.ml:178:1`

### #168 PIPELINE_OPERATOR on `C_visa_spec.opcodes`
- **Category:** `functional_idiom`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_spec.ml:192:1`
- **Summary:** Function 'opcodes' composes functional data transformations across a 66-stage pipe (`|>`)

#### Evidence Trail:
- `+75%` **[PIPELINE_OPERATOR_CHAIN]** Function 'opcodes' composes functional data transformations across a 66-stage pipe (`|>`) -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_spec.ml:192:1`

### #169 CLOSURE_CURRYING_STRATEGY on `Goblint_cil_adapter.filter_builtins`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/infrastructure/c_frontend/goblint_cil_adapter.ml:32:1`
- **Summary:** Function 'filter_builtins' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'filter_builtins' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/infrastructure/c_frontend/goblint_cil_adapter.ml:32:1`

### #170 CLOSURE_CURRYING_STRATEGY on `Goblint_cil_adapter.emit_to_string`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/infrastructure/c_frontend/goblint_cil_adapter.ml:44:1`
- **Summary:** Function 'emit_to_string' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'emit_to_string' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/infrastructure/c_frontend/goblint_cil_adapter.ml:44:1`

### #171 CLOSURE_CURRYING_STRATEGY on `Goblint_cil_adapter.emit_to_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/infrastructure/c_frontend/goblint_cil_adapter.ml:57:1`
- **Summary:** Function 'emit_to_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'emit_to_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/infrastructure/c_frontend/goblint_cil_adapter.ml:57:1`

### #172 CLOSURE_CURRYING_STRATEGY on `C_concurrent_fiber_runtime.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_concurrent_fiber_runtime.ml:70:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_concurrent_fiber_runtime.ml:70:1`

### #173 CLOSURE_CURRYING_STRATEGY on `C_self_modifying_vm_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:74:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:74:1`

### #174 CLOSURE_CURRYING_STRATEGY on `C_rolling_vkey_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:16:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:16:1`

### #175 CLOSURE_CURRYING_STRATEGY on `C_nested_vm_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:340:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:340:1`

### #176 CLOSURE_CURRYING_STRATEGY on `C_vcpu_context_scramble_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:10:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:10:1`

### #177 CLOSURE_CURRYING_STRATEGY on `C_decentralized_dispatcher_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:124:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:124:1`

### #178 CLOSURE_CURRYING_STRATEGY on `C_visa_spec_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:210:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:210:1`

### #179 CLOSURE_CURRYING_STRATEGY on `C_virtualize_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:205:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:205:1`

### #180 CLOSURE_CURRYING_STRATEGY on `C_bogus_calls_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_bogus_calls_service.ml:39:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_bogus_calls_service.ml:39:1`

### #181 CLOSURE_CURRYING_STRATEGY on `C_call_graph_flatten_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_call_graph_flatten_service.ml:23:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_call_graph_flatten_service.ml:23:1`

### #182 CLOSURE_CURRYING_STRATEGY on `C_outline_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_outline_service.ml:83:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_outline_service.ml:83:1`

### #183 CLOSURE_CURRYING_STRATEGY on `C_merge_functions_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_merge_functions_service.ml:101:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_merge_functions_service.ml:101:1`

### #184 CLOSURE_CURRYING_STRATEGY on `C_inline_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_inline_service.ml:52:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_inline_service.ml:52:1`

### #185 CLOSURE_CURRYING_STRATEGY on `C_pointer_masking_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_pointer_masking_service.ml:16:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_pointer_masking_service.ml:16:1`

### #186 CLOSURE_CURRYING_STRATEGY on `C_struct_permute_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_struct_permute_service.ml:26:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_struct_permute_service.ml:26:1`

### #187 CLOSURE_CURRYING_STRATEGY on `C_bpm_mba_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_bpm_mba_service.ml:119:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_bpm_mba_service.ml:119:1`

### #188 CLOSURE_CURRYING_STRATEGY on `C_mba_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:128:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:128:1`

### #189 CLOSURE_CURRYING_STRATEGY on `C_float_mba_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_float_mba_service.ml:63:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_float_mba_service.ml:63:1`

### #190 CLOSURE_CURRYING_STRATEGY on `C_encode_literals_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:145:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:145:1`

### #191 CLOSURE_CURRYING_STRATEGY on `C_array_interleave_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_array_interleave_service.ml:17:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_array_interleave_service.ml:17:1`

### #192 CLOSURE_CURRYING_STRATEGY on `C_homomorphic_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_homomorphic_service.ml:47:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_homomorphic_service.ml:47:1`

### #193 CLOSURE_CURRYING_STRATEGY on `C_encode_data_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_data_service.ml:62:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_data_service.ml:62:1`

### #194 CLOSURE_CURRYING_STRATEGY on `C_lut_arithmetic_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_lut_arithmetic_service.ml:41:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_lut_arithmetic_service.ml:41:1`

### #195 CLOSURE_CURRYING_STRATEGY on `C_polynomial_mba_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_polynomial_mba_service.ml:125:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_polynomial_mba_service.ml:125:1`

### #196 CLOSURE_CURRYING_STRATEGY on `C_instruction_permute_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_instruction_permute_service.ml:127:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_instruction_permute_service.ml:127:1`

### #197 CLOSURE_CURRYING_STRATEGY on `C_ghost_code_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_ghost_code_service.ml:50:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_ghost_code_service.ml:50:1`

### #198 CLOSURE_CURRYING_STRATEGY on `C_constant_unfold_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_constant_unfold_service.ml:22:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_constant_unfold_service.ml:22:1`

### #199 CLOSURE_CURRYING_STRATEGY on `C_relational_morph_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_relational_morph_service.ml:97:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_relational_morph_service.ml:97:1`

### #200 CLOSURE_CURRYING_STRATEGY on `C_stack_aliasing_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_stack_aliasing_service.ml:7:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_stack_aliasing_service.ml:7:1`

### #201 CLOSURE_CURRYING_STRATEGY on `C_opcode_equalize_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_opcode_equalize_service.ml:41:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_opcode_equalize_service.ml:41:1`

### #202 CLOSURE_CURRYING_STRATEGY on `C_instruction_subst_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_instruction_subst_service.ml:102:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_instruction_subst_service.ml:102:1`

### #203 CLOSURE_CURRYING_STRATEGY on `C_live_range_split_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_live_range_split_service.ml:43:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_live_range_split_service.ml:43:1`

### #204 CLOSURE_CURRYING_STRATEGY on `C_anti_slicing_entanglement_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:98:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:98:1`

### #205 CLOSURE_CURRYING_STRATEGY on `C_loop_to_recursion_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_loop_to_recursion_service.ml:10:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_loop_to_recursion_service.ml:10:1`

### #206 CLOSURE_CURRYING_STRATEGY on `C_ephemeral_payload_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:21:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:21:1`

### #207 CLOSURE_CURRYING_STRATEGY on `C_early_constructor_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_early_constructor_service.ml:5:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_early_constructor_service.ml:5:1`

### #208 CLOSURE_CURRYING_STRATEGY on `C_api_hash_resolver_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_api_hash_resolver_service.ml:91:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_api_hash_resolver_service.ml:91:1`

### #209 CLOSURE_CURRYING_STRATEGY on `C_rename_symbols_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/symbols/c_rename_symbols_service.ml:30:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/symbols/c_rename_symbols_service.ml:30:1`

### #210 CLOSURE_CURRYING_STRATEGY on `C_strip_directives_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/symbols/c_strip_directives_service.ml:19:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/symbols/c_strip_directives_service.ml:19:1`

### #211 CLOSURE_CURRYING_STRATEGY on `C_threaded_implicit_flow_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_threaded_implicit_flow_service.ml:65:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_threaded_implicit_flow_service.ml:65:1`

### #212 CLOSURE_CURRYING_STRATEGY on `C_sigfpe_flow_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:91:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:91:1`

### #213 CLOSURE_CURRYING_STRATEGY on `C_sigill_flow_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigill_flow_service.ml:80:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigill_flow_service.ml:80:1`

### #214 CLOSURE_CURRYING_STRATEGY on `C_implicit_flow_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:91:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:91:1`

### #215 CLOSURE_CURRYING_STRATEGY on `C_syscall_error_flow_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_syscall_error_flow_service.ml:67:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_syscall_error_flow_service.ml:67:1`

### #216 CLOSURE_CURRYING_STRATEGY on `C_flattening_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:85:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:85:1`

### #217 CLOSURE_CURRYING_STRATEGY on `C_diophantine_opaque_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_diophantine_opaque_service.ml:57:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_diophantine_opaque_service.ml:57:1`

### #218 CLOSURE_CURRYING_STRATEGY on `C_loop_unroll_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_unroll_service.ml:32:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_unroll_service.ml:32:1`

### #219 CLOSURE_CURRYING_STRATEGY on `C_basic_block_split_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:39:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:39:1`

### #220 CLOSURE_CURRYING_STRATEGY on `C_bogus_control_flow_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_bogus_control_flow_service.ml:46:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_bogus_control_flow_service.ml:46:1`

### #221 CLOSURE_CURRYING_STRATEGY on `C_irreducible_loop_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:122:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:122:1`

### #222 CLOSURE_CURRYING_STRATEGY on `C_opaque_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_opaque_service.ml:67:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_opaque_service.ml:67:1`

### #223 CLOSURE_CURRYING_STRATEGY on `C_indirect_jump_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:42:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:42:1`

### #224 CLOSURE_CURRYING_STRATEGY on `C_loop_fission_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_fission_service.ml:37:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_fission_service.ml:37:1`

### #225 CLOSURE_CURRYING_STRATEGY on `C_dynamic_opaque_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_dynamic_opaque_service.ml:96:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_dynamic_opaque_service.ml:96:1`

### #226 CLOSURE_CURRYING_STRATEGY on `C_self_checksum_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_self_checksum_service.ml:67:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_self_checksum_service.ml:67:1`

### #227 CLOSURE_CURRYING_STRATEGY on `C_anti_disassembly_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_disassembly_service.ml:30:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_disassembly_service.ml:30:1`

### #228 CLOSURE_CURRYING_STRATEGY on `C_anti_debug_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_debug_service.ml:80:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_debug_service.ml:80:1`

### #229 CLOSURE_CURRYING_STRATEGY on `C_hook_detect_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_hook_detect_service.ml:47:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_hook_detect_service.ml:47:1`

### #230 CLOSURE_CURRYING_STRATEGY on `C_timing_check_service.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_timing_check_service.ml:53:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_timing_check_service.ml:53:1`

### #231 CLOSURE_CURRYING_STRATEGY on `Make.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_concurrent_fiber_runtime.ml:66:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_concurrent_fiber_runtime.ml:66:1`

### #232 CLOSURE_CURRYING_STRATEGY on `Make.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:71:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:71:1`

### #233 CLOSURE_CURRYING_STRATEGY on `Make.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:13:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:13:1`

### #234 CLOSURE_CURRYING_STRATEGY on `Make.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:337:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:337:1`

### #235 CLOSURE_CURRYING_STRATEGY on `Make.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:7:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:7:1`

### #236 CLOSURE_CURRYING_STRATEGY on `Make.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:205:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:205:1`

### #237 CLOSURE_CURRYING_STRATEGY on `Make.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:202:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:202:1`

### #238 CLOSURE_CURRYING_STRATEGY on `Make.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_struct_permute_service.ml:23:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_struct_permute_service.ml:23:1`

### #239 CLOSURE_CURRYING_STRATEGY on `Make.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_stack_aliasing_service.ml:4:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_stack_aliasing_service.ml:4:1`

### #240 CLOSURE_CURRYING_STRATEGY on `Make.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_loop_to_recursion_service.ml:7:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_loop_to_recursion_service.ml:7:1`

### #241 CLOSURE_CURRYING_STRATEGY on `Make.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:18:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:18:1`

### #242 CLOSURE_CURRYING_STRATEGY on `Make.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_early_constructor_service.ml:2:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_early_constructor_service.ml:2:1`

### #243 CLOSURE_CURRYING_STRATEGY on `Make.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_threaded_implicit_flow_service.ml:62:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_threaded_implicit_flow_service.ml:62:1`

### #244 CLOSURE_CURRYING_STRATEGY on `Make.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:88:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:88:1`

### #245 CLOSURE_CURRYING_STRATEGY on `Make.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigill_flow_service.ml:77:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigill_flow_service.ml:77:1`

### #246 CLOSURE_CURRYING_STRATEGY on `Make.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:88:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:88:1`

### #247 CLOSURE_CURRYING_STRATEGY on `Make.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:36:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:36:1`

### #248 CLOSURE_CURRYING_STRATEGY on `Make.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:39:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:39:1`

### #249 CLOSURE_CURRYING_STRATEGY on `Make.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_debug_service.ml:77:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_debug_service.ml:77:1`

### #250 CLOSURE_CURRYING_STRATEGY on `Make.transform_file`
- **Category:** `behavioral`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_timing_check_service.ml:50:1`
- **Summary:** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection

#### Evidence Trail:
- `+75%` **[CURRIED_STRATEGY_INJECTION]** Function 'transform_file' accepts higher-order strategy parameter 'f' for dynamic algorithm injection -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_timing_check_service.ml:50:1`

### #251 UNCHECKED_EXCEPTION_RAISE on `Cil_interpreter.max_steps`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/infrastructure/runtime/cil/cil_interpreter.ml:14:1`
- **Summary:** Type Safety Audit: Function 'max_steps' in 'Cil_interpreter' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead

#### Evidence Trail:
- `+80%` **[UNCHECKED_EXCEPTION_THROW]** Type Safety Audit: Function 'max_steps' in 'Cil_interpreter' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead -> `/Volumes/External/Code/vectis/lib/infrastructure/runtime/cil/cil_interpreter.ml:14:1`

### #252 UNCHECKED_EXCEPTION_RAISE on `Cil_interpreter.idx`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/infrastructure/runtime/cil/cil_interpreter.ml:42:1`
- **Summary:** Type Safety Audit: Function 'idx' in 'Cil_interpreter' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead

#### Evidence Trail:
- `+80%` **[UNCHECKED_EXCEPTION_THROW]** Type Safety Audit: Function 'idx' in 'Cil_interpreter' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead -> `/Volumes/External/Code/vectis/lib/infrastructure/runtime/cil/cil_interpreter.ml:42:1`

### #253 UNCHECKED_EXCEPTION_RAISE on `Cil_interpreter.a`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/infrastructure/runtime/cil/cil_interpreter.ml:141:1`
- **Summary:** Type Safety Audit: Function 'a' in 'Cil_interpreter' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead

#### Evidence Trail:
- `+80%` **[UNCHECKED_EXCEPTION_THROW]** Type Safety Audit: Function 'a' in 'Cil_interpreter' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead -> `/Volumes/External/Code/vectis/lib/infrastructure/runtime/cil/cil_interpreter.ml:141:1`

### #254 UNCHECKED_EXCEPTION_RAISE on `Cil_stack.pop_i64`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/infrastructure/runtime/cil/cil_stack.ml:26:1`
- **Summary:** Type Safety Audit: Function 'pop_i64' in 'Cil_stack' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead

#### Evidence Trail:
- `+80%` **[UNCHECKED_EXCEPTION_THROW]** Type Safety Audit: Function 'pop_i64' in 'Cil_stack' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead -> `/Volumes/External/Code/vectis/lib/infrastructure/runtime/cil/cil_stack.ml:26:1`

### #255 UNCHECKED_EXCEPTION_RAISE on `Goblint_cil_adapter.res`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/infrastructure/c_frontend/goblint_cil_adapter.ml:23:1`
- **Summary:** Type Safety Audit: Function 'res' in 'Goblint_cil_adapter' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead

#### Evidence Trail:
- `+80%` **[UNCHECKED_EXCEPTION_THROW]** Type Safety Audit: Function 'res' in 'Goblint_cil_adapter' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead -> `/Volumes/External/Code/vectis/lib/infrastructure/c_frontend/goblint_cil_adapter.ml:23:1`

### #256 UNCHECKED_EXCEPTION_RAISE on `System_entropy_adapter.choose`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/infrastructure/random/system_entropy_adapter.ml:22:1`
- **Summary:** Type Safety Audit: Function 'choose' in 'System_entropy_adapter' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead

#### Evidence Trail:
- `+80%` **[UNCHECKED_EXCEPTION_THROW]** Type Safety Audit: Function 'choose' in 'System_entropy_adapter' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead -> `/Volumes/External/Code/vectis/lib/infrastructure/random/system_entropy_adapter.ml:22:1`

### #257 UNCHECKED_EXCEPTION_RAISE on `Two_tier_jit_service.tier2_plain_bytes`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/two_tier_jit_service.ml:22:1`
- **Summary:** Type Safety Audit: Function 'tier2_plain_bytes' in 'Two_tier_jit_service' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead

#### Evidence Trail:
- `+80%` **[UNCHECKED_EXCEPTION_THROW]** Type Safety Audit: Function 'tier2_plain_bytes' in 'Two_tier_jit_service' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead -> `/Volumes/External/Code/vectis/lib/domain/services/native/two_tier_jit_service.ml:22:1`

### #258 UNCHECKED_EXCEPTION_RAISE on `Two_tier_jit_service.tier1_bytes`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/two_tier_jit_service.ml:48:1`
- **Summary:** Type Safety Audit: Function 'tier1_bytes' in 'Two_tier_jit_service' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead

#### Evidence Trail:
- `+80%` **[UNCHECKED_EXCEPTION_THROW]** Type Safety Audit: Function 'tier1_bytes' in 'Two_tier_jit_service' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead -> `/Volumes/External/Code/vectis/lib/domain/services/native/two_tier_jit_service.ml:48:1`

### #259 UNCHECKED_EXCEPTION_RAISE on `C_isa_synthesizer_service.synthesize_8vcpu_cascade`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:389:1`
- **Summary:** Type Safety Audit: Function 'synthesize_8vcpu_cascade' in 'C_isa_synthesizer_service' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead

#### Evidence Trail:
- `+80%` **[UNCHECKED_EXCEPTION_THROW]** Type Safety Audit: Function 'synthesize_8vcpu_cascade' in 'C_isa_synthesizer_service' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:389:1`

### #260 UNCHECKED_EXCEPTION_RAISE on `C_visa_spec.validate_layout`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_spec.ml:126:1`
- **Summary:** Type Safety Audit: Function 'validate_layout' in 'C_visa_spec' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead

#### Evidence Trail:
- `+80%` **[UNCHECKED_EXCEPTION_THROW]** Type Safety Audit: Function 'validate_layout' in 'C_visa_spec' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_spec.ml:126:1`

### #261 UNCHECKED_EXCEPTION_RAISE on `C_visa_spec.cover`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_spec.ml:135:1`
- **Summary:** Type Safety Audit: Function 'cover' in 'C_visa_spec' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead

#### Evidence Trail:
- `+80%` **[UNCHECKED_EXCEPTION_THROW]** Type Safety Audit: Function 'cover' in 'C_visa_spec' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_spec.ml:135:1`

### #262 UNCHECKED_EXCEPTION_RAISE on `Adapter.choose`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/infrastructure/random/system_entropy_adapter.ml:15:1`
- **Summary:** Type Safety Audit: Function 'choose' in 'Adapter' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead

#### Evidence Trail:
- `+80%` **[UNCHECKED_EXCEPTION_THROW]** Type Safety Audit: Function 'choose' in 'Adapter' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead -> `/Volumes/External/Code/vectis/lib/infrastructure/random/system_entropy_adapter.ml:15:1`

### #263 UNCHECKED_EXCEPTION_RAISE on `Make.synthesize_8vcpu_cascade`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:386:1`
- **Summary:** Type Safety Audit: Function 'synthesize_8vcpu_cascade' in 'Make' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead

#### Evidence Trail:
- `+80%` **[UNCHECKED_EXCEPTION_THROW]** Type Safety Audit: Function 'synthesize_8vcpu_cascade' in 'Make' throws unhandled runtime exception (`failwith`/`raise`); return typed `Result.t` or `Option.t` instead -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:386:1`

### #264 DEFENSIVE_CATCH_ALL_EXN on `Vectis_cc.ret_code`
- **Category:** `resilience`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/bin/vectis_cc.ml:242:1`
- **Summary:** Resilience Smell (Defensive Catch-All): Function 'ret_code' in 'Vectis_cc' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only

#### Evidence Trail:
- `+85%` **[DEFENSIVE_CATCH_ALL_SWALLOW]** Resilience Smell (Defensive Catch-All): Function 'ret_code' in 'Vectis_cc' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only -> `/Volumes/External/Code/vectis/bin/vectis_cc.ml:242:1`

### #265 DEFENSIVE_CATCH_ALL_EXN on `Vectis_synth.opt_int64`
- **Category:** `resilience`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/bin/vectis_synth.ml:58:1`
- **Summary:** Resilience Smell (Defensive Catch-All): Function 'opt_int64' in 'Vectis_synth' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only

#### Evidence Trail:
- `+85%` **[DEFENSIVE_CATCH_ALL_SWALLOW]** Resilience Smell (Defensive Catch-All): Function 'opt_int64' in 'Vectis_synth' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only -> `/Volumes/External/Code/vectis/bin/vectis_synth.ml:58:1`

### #266 DEFENSIVE_CATCH_ALL_EXN on `Build_polymorphic_library_usecase.tmp_dir`
- **Category:** `resilience`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/application/build_polymorphic_library_usecase.ml:51:1`
- **Summary:** Resilience Smell (Defensive Catch-All): Function 'tmp_dir' in 'Build_polymorphic_library_usecase' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only

#### Evidence Trail:
- `+85%` **[DEFENSIVE_CATCH_ALL_SWALLOW]** Resilience Smell (Defensive Catch-All): Function 'tmp_dir' in 'Build_polymorphic_library_usecase' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only -> `/Volumes/External/Code/vectis/lib/application/build_polymorphic_library_usecase.ml:51:1`

### #267 DEFENSIVE_CATCH_ALL_EXN on `Build_polymorphic_library_usecase.obf_result`
- **Category:** `resilience`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/application/build_polymorphic_library_usecase.ml:64:1`
- **Summary:** Resilience Smell (Defensive Catch-All): Function 'obf_result' in 'Build_polymorphic_library_usecase' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only

#### Evidence Trail:
- `+85%` **[DEFENSIVE_CATCH_ALL_SWALLOW]** Resilience Smell (Defensive Catch-All): Function 'obf_result' in 'Build_polymorphic_library_usecase' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only -> `/Volumes/External/Code/vectis/lib/application/build_polymorphic_library_usecase.ml:64:1`

### #268 DEFENSIVE_CATCH_ALL_EXN on `Build_polymorphic_library_usecase.compile_res`
- **Category:** `resilience`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/application/build_polymorphic_library_usecase.ml:100:1`
- **Summary:** Resilience Smell (Defensive Catch-All): Function 'compile_res' in 'Build_polymorphic_library_usecase' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only

#### Evidence Trail:
- `+85%` **[DEFENSIVE_CATCH_ALL_SWALLOW]** Resilience Smell (Defensive Catch-All): Function 'compile_res' in 'Build_polymorphic_library_usecase' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only -> `/Volumes/External/Code/vectis/lib/application/build_polymorphic_library_usecase.ml:100:1`

### #269 DEFENSIVE_CATCH_ALL_EXN on `Goblint_cil_adapter.res`
- **Category:** `resilience`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/infrastructure/c_frontend/goblint_cil_adapter.ml:23:1`
- **Summary:** Resilience Smell (Defensive Catch-All): Function 'res' in 'Goblint_cil_adapter' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only

#### Evidence Trail:
- `+85%` **[DEFENSIVE_CATCH_ALL_SWALLOW]** Resilience Smell (Defensive Catch-All): Function 'res' in 'Goblint_cil_adapter' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only -> `/Volumes/External/Code/vectis/lib/infrastructure/c_frontend/goblint_cil_adapter.ml:23:1`

### #270 DEFENSIVE_CATCH_ALL_EXN on `Goblint_cil_adapter.content`
- **Category:** `resilience`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/infrastructure/c_frontend/goblint_cil_adapter.ml:52:1`
- **Summary:** Resilience Smell (Defensive Catch-All): Function 'content' in 'Goblint_cil_adapter' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only

#### Evidence Trail:
- `+85%` **[DEFENSIVE_CATCH_ALL_SWALLOW]** Resilience Smell (Defensive Catch-All): Function 'content' in 'Goblint_cil_adapter' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only -> `/Volumes/External/Code/vectis/lib/infrastructure/c_frontend/goblint_cil_adapter.ml:52:1`

### #271 DEFENSIVE_CATCH_ALL_EXN on `C_isa_synthesizer_service.oc`
- **Category:** `resilience`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:353:1`
- **Summary:** Resilience Smell (Defensive Catch-All): Function 'oc' in 'C_isa_synthesizer_service' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only

#### Evidence Trail:
- `+85%` **[DEFENSIVE_CATCH_ALL_SWALLOW]** Resilience Smell (Defensive Catch-All): Function 'oc' in 'C_isa_synthesizer_service' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:353:1`

### #272 DEFENSIVE_CATCH_ALL_EXN on `C_isa_synthesizer_service.synthesize_8vcpu_cascade`
- **Category:** `resilience`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:389:1`
- **Summary:** Resilience Smell (Defensive Catch-All): Function 'synthesize_8vcpu_cascade' in 'C_isa_synthesizer_service' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only

#### Evidence Trail:
- `+85%` **[DEFENSIVE_CATCH_ALL_SWALLOW]** Resilience Smell (Defensive Catch-All): Function 'synthesize_8vcpu_cascade' in 'C_isa_synthesizer_service' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:389:1`

### #273 DEFENSIVE_CATCH_ALL_EXN on `C_visa_expr_compiler.snapshot`
- **Category:** `resilience`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_expr_compiler.ml:101:1`
- **Summary:** Resilience Smell (Defensive Catch-All): Function 'snapshot' in 'C_visa_expr_compiler' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only

#### Evidence Trail:
- `+85%` **[DEFENSIVE_CATCH_ALL_SWALLOW]** Resilience Smell (Defensive Catch-All): Function 'snapshot' in 'C_visa_expr_compiler' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_expr_compiler.ml:101:1`

### #274 DEFENSIVE_CATCH_ALL_EXN on `Make.oc`
- **Category:** `resilience`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:350:1`
- **Summary:** Resilience Smell (Defensive Catch-All): Function 'oc' in 'Make' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only

#### Evidence Trail:
- `+85%` **[DEFENSIVE_CATCH_ALL_SWALLOW]** Resilience Smell (Defensive Catch-All): Function 'oc' in 'Make' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:350:1`

### #275 DEFENSIVE_CATCH_ALL_EXN on `Make.synthesize_8vcpu_cascade`
- **Category:** `resilience`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:386:1`
- **Summary:** Resilience Smell (Defensive Catch-All): Function 'synthesize_8vcpu_cascade' in 'Make' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only

#### Evidence Trail:
- `+85%` **[DEFENSIVE_CATCH_ALL_SWALLOW]** Resilience Smell (Defensive Catch-All): Function 'synthesize_8vcpu_cascade' in 'Make' swallows all exceptions (`with _ -> ...`); catch specific expected exceptions only -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:386:1`

### #276 MUTABLE_REF_OVERUSE on `Vectis_cc`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/bin/vectis_cc.ml:1:1`
- **Summary:** Functional Purity Audit: Module 'Vectis_cc' defines 60 mutable references / fields, breaking immutability; favor pure recursive accumulators

#### Evidence Trail:
- `+75%` **[MUTABLE_STATE_OVERUSE]** Functional Purity Audit: Module 'Vectis_cc' defines 60 mutable references / fields, breaking immutability; favor pure recursive accumulators -> `/Volumes/External/Code/vectis/bin/vectis_cc.ml:1:1`

### #277 MUTABLE_REF_OVERUSE on `Main`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/bin/main.ml:1:1`
- **Summary:** Functional Purity Audit: Module 'Main' defines 70 mutable references / fields, breaking immutability; favor pure recursive accumulators

#### Evidence Trail:
- `+75%` **[MUTABLE_STATE_OVERUSE]** Functional Purity Audit: Module 'Main' defines 70 mutable references / fields, breaking immutability; favor pure recursive accumulators -> `/Volumes/External/Code/vectis/bin/main.ml:1:1`

### #278 MUTABLE_REF_OVERUSE on `Vectis_synth`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/bin/vectis_synth.ml:1:1`
- **Summary:** Functional Purity Audit: Module 'Vectis_synth' defines 18 mutable references / fields, breaking immutability; favor pure recursive accumulators

#### Evidence Trail:
- `+75%` **[MUTABLE_STATE_OVERUSE]** Functional Purity Audit: Module 'Vectis_synth' defines 18 mutable references / fields, breaking immutability; favor pure recursive accumulators -> `/Volumes/External/Code/vectis/bin/vectis_synth.ml:1:1`

### #279 MUTABLE_REF_OVERUSE on `Vectis_state_masking`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:1:1`
- **Summary:** Functional Purity Audit: Module 'Vectis_state_masking' defines 5 mutable references / fields, breaking immutability; favor pure recursive accumulators

#### Evidence Trail:
- `+75%` **[MUTABLE_STATE_OVERUSE]** Functional Purity Audit: Module 'Vectis_state_masking' defines 5 mutable references / fields, breaking immutability; favor pure recursive accumulators -> `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:1:1`

### #280 MUTABLE_REF_OVERUSE on `Vectis_vm_interpreter`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_vm_interpreter.ml:1:1`
- **Summary:** Functional Purity Audit: Module 'Vectis_vm_interpreter' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators

#### Evidence Trail:
- `+75%` **[MUTABLE_STATE_OVERUSE]** Functional Purity Audit: Module 'Vectis_vm_interpreter' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators -> `/Volumes/External/Code/vectis/lib/domain/vectis_vm_interpreter.ml:1:1`

### #281 MUTABLE_REF_OVERUSE on `Vectis_egraph`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_egraph.ml:1:1`
- **Summary:** Functional Purity Audit: Module 'Vectis_egraph' defines 5 mutable references / fields, breaking immutability; favor pure recursive accumulators

#### Evidence Trail:
- `+75%` **[MUTABLE_STATE_OVERUSE]** Functional Purity Audit: Module 'Vectis_egraph' defines 5 mutable references / fields, breaking immutability; favor pure recursive accumulators -> `/Volumes/External/Code/vectis/lib/domain/vectis_egraph.ml:1:1`

### #282 MUTABLE_REF_OVERUSE on `Vectis_isa`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_isa.ml:1:1`
- **Summary:** Functional Purity Audit: Module 'Vectis_isa' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators

#### Evidence Trail:
- `+75%` **[MUTABLE_STATE_OVERUSE]** Functional Purity Audit: Module 'Vectis_isa' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators -> `/Volumes/External/Code/vectis/lib/domain/vectis_isa.ml:1:1`

### #283 MUTABLE_REF_OVERUSE on `C_visa_profile_service`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_profile_service.ml:1:1`
- **Summary:** Functional Purity Audit: Module 'C_visa_profile_service' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators

#### Evidence Trail:
- `+75%` **[MUTABLE_STATE_OVERUSE]** Functional Purity Audit: Module 'C_visa_profile_service' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_profile_service.ml:1:1`

### #284 MUTABLE_REF_OVERUSE on `C_arm64_jit_compiler`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:1:1`
- **Summary:** Functional Purity Audit: Module 'C_arm64_jit_compiler' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators

#### Evidence Trail:
- `+75%` **[MUTABLE_STATE_OVERUSE]** Functional Purity Audit: Module 'C_arm64_jit_compiler' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:1:1`

### #285 MUTABLE_REF_OVERUSE on `C_arm64_edsl`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_edsl.ml:1:1`
- **Summary:** Functional Purity Audit: Module 'C_arm64_edsl' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators

#### Evidence Trail:
- `+75%` **[MUTABLE_STATE_OVERUSE]** Functional Purity Audit: Module 'C_arm64_edsl' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_edsl.ml:1:1`

### #286 MUTABLE_REF_OVERUSE on `C_visa_stmt_compiler`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_stmt_compiler.ml:1:1`
- **Summary:** Functional Purity Audit: Module 'C_visa_stmt_compiler' defines 9 mutable references / fields, breaking immutability; favor pure recursive accumulators

#### Evidence Trail:
- `+75%` **[MUTABLE_STATE_OVERUSE]** Functional Purity Audit: Module 'C_visa_stmt_compiler' defines 9 mutable references / fields, breaking immutability; favor pure recursive accumulators -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_stmt_compiler.ml:1:1`

### #287 MUTABLE_REF_OVERUSE on `C_egraph_mba_service`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:1:1`
- **Summary:** Functional Purity Audit: Module 'C_egraph_mba_service' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators

#### Evidence Trail:
- `+75%` **[MUTABLE_STATE_OVERUSE]** Functional Purity Audit: Module 'C_egraph_mba_service' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:1:1`

### #288 MUTABLE_REF_OVERUSE on `C_instruction_permute_service`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_instruction_permute_service.ml:1:1`
- **Summary:** Functional Purity Audit: Module 'C_instruction_permute_service' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators

#### Evidence Trail:
- `+75%` **[MUTABLE_STATE_OVERUSE]** Functional Purity Audit: Module 'C_instruction_permute_service' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_instruction_permute_service.ml:1:1`

### #289 MUTABLE_REF_OVERUSE on `C_anti_slicing_entanglement_service`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:1:1`
- **Summary:** Functional Purity Audit: Module 'C_anti_slicing_entanglement_service' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators

#### Evidence Trail:
- `+75%` **[MUTABLE_STATE_OVERUSE]** Functional Purity Audit: Module 'C_anti_slicing_entanglement_service' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:1:1`

### #290 MUTABLE_REF_OVERUSE on `C_implicit_flow_service`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:1:1`
- **Summary:** Functional Purity Audit: Module 'C_implicit_flow_service' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators

#### Evidence Trail:
- `+75%` **[MUTABLE_STATE_OVERUSE]** Functional Purity Audit: Module 'C_implicit_flow_service' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:1:1`

### #291 MUTABLE_REF_OVERUSE on `C_irreducible_loop_service`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:1:1`
- **Summary:** Functional Purity Audit: Module 'C_irreducible_loop_service' defines 9 mutable references / fields, breaking immutability; favor pure recursive accumulators

#### Evidence Trail:
- `+75%` **[MUTABLE_STATE_OVERUSE]** Functional Purity Audit: Module 'C_irreducible_loop_service' defines 9 mutable references / fields, breaking immutability; favor pure recursive accumulators -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:1:1`

### #292 MUTABLE_REF_OVERUSE on `Make`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:4:1`
- **Summary:** Functional Purity Audit: Module 'Make' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators

#### Evidence Trail:
- `+75%` **[MUTABLE_STATE_OVERUSE]** Functional Purity Audit: Module 'Make' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:4:1`

### #293 MUTABLE_REF_OVERUSE on `Make`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:4:1`
- **Summary:** Functional Purity Audit: Module 'Make' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators

#### Evidence Trail:
- `+75%` **[MUTABLE_STATE_OVERUSE]** Functional Purity Audit: Module 'Make' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:4:1`

### #294 MUTABLE_REF_OVERUSE on `Make`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:4:1`
- **Summary:** Functional Purity Audit: Module 'Make' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators

#### Evidence Trail:
- `+75%` **[MUTABLE_STATE_OVERUSE]** Functional Purity Audit: Module 'Make' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:4:1`

### #295 MUTABLE_REF_OVERUSE on `Make`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:4:1`
- **Summary:** Functional Purity Audit: Module 'Make' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators

#### Evidence Trail:
- `+75%` **[MUTABLE_STATE_OVERUSE]** Functional Purity Audit: Module 'Make' defines 4 mutable references / fields, breaking immutability; favor pure recursive accumulators -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:4:1`

### #296 MUTABLE_REF_OVERUSE on `Make`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:4:1`
- **Summary:** Functional Purity Audit: Module 'Make' defines 9 mutable references / fields, breaking immutability; favor pure recursive accumulators

#### Evidence Trail:
- `+75%` **[MUTABLE_STATE_OVERUSE]** Functional Purity Audit: Module 'Make' defines 9 mutable references / fields, breaking immutability; favor pure recursive accumulators -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:4:1`

### #297 PHYSICAL_EQUALITY_SMELL on `C_concurrent_fiber_runtime.tmpl`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_concurrent_fiber_runtime.ml:13:1`
- **Summary:** Type Safety Hazard (Physical Equality): Function 'tmpl' in 'C_concurrent_fiber_runtime' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs

#### Evidence Trail:
- `+80%` **[PHYSICAL_EQUALITY_COMPARISON]** Type Safety Hazard (Physical Equality): Function 'tmpl' in 'C_concurrent_fiber_runtime' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_concurrent_fiber_runtime.ml:13:1`

### #298 PHYSICAL_EQUALITY_SMELL on `C_visa_c_runtime.jitter_fn`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_visa_c_runtime.ml:132:1`
- **Summary:** Type Safety Hazard (Physical Equality): Function 'jitter_fn' in 'C_visa_c_runtime' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs

#### Evidence Trail:
- `+80%` **[PHYSICAL_EQUALITY_COMPARISON]** Type Safety Hazard (Physical Equality): Function 'jitter_fn' in 'C_visa_c_runtime' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_visa_c_runtime.ml:132:1`

### #299 PHYSICAL_EQUALITY_SMELL on `C_visa_c_runtime.decoy_val`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_visa_c_runtime.ml:232:1`
- **Summary:** Type Safety Hazard (Physical Equality): Function 'decoy_val' in 'C_visa_c_runtime' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs

#### Evidence Trail:
- `+80%` **[PHYSICAL_EQUALITY_COMPARISON]** Type Safety Hazard (Physical Equality): Function 'decoy_val' in 'C_visa_c_runtime' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_visa_c_runtime.ml:232:1`

### #300 PHYSICAL_EQUALITY_SMELL on `C_visa_c_runtime.epilogue_jitter`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_visa_c_runtime.ml:318:1`
- **Summary:** Type Safety Hazard (Physical Equality): Function 'epilogue_jitter' in 'C_visa_c_runtime' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs

#### Evidence Trail:
- `+80%` **[PHYSICAL_EQUALITY_COMPARISON]** Type Safety Hazard (Physical Equality): Function 'epilogue_jitter' in 'C_visa_c_runtime' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_visa_c_runtime.ml:318:1`

### #301 PHYSICAL_EQUALITY_SMELL on `C_visa_c_handlers.f_vor1`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_visa_c_handlers.ml:129:1`
- **Summary:** Type Safety Hazard (Physical Equality): Function 'f_vor1' in 'C_visa_c_handlers' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs

#### Evidence Trail:
- `+80%` **[PHYSICAL_EQUALITY_COMPARISON]** Type Safety Hazard (Physical Equality): Function 'f_vor1' in 'C_visa_c_handlers' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_visa_c_handlers.ml:129:1`

### #302 PHYSICAL_EQUALITY_SMELL on `C_isa_sail_templates.s`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_sail_templates.ml:393:1`
- **Summary:** Type Safety Hazard (Physical Equality): Function 's' in 'C_isa_sail_templates' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs

#### Evidence Trail:
- `+80%` **[PHYSICAL_EQUALITY_COMPARISON]** Type Safety Hazard (Physical Equality): Function 's' in 'C_isa_sail_templates' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_sail_templates.ml:393:1`

### #303 PHYSICAL_EQUALITY_SMELL on `C_isa_sail_templates.p1`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_sail_templates.ml:167:1`
- **Summary:** Type Safety Hazard (Physical Equality): Function 'p1' in 'C_isa_sail_templates' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs

#### Evidence Trail:
- `+80%` **[PHYSICAL_EQUALITY_COMPARISON]** Type Safety Hazard (Physical Equality): Function 'p1' in 'C_isa_sail_templates' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_sail_templates.ml:167:1`

### #304 PHYSICAL_EQUALITY_SMELL on `C_isa_sail_templates.b2`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_sail_templates.ml:168:1`
- **Summary:** Type Safety Hazard (Physical Equality): Function 'b2' in 'C_isa_sail_templates' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs

#### Evidence Trail:
- `+80%` **[PHYSICAL_EQUALITY_COMPARISON]** Type Safety Hazard (Physical Equality): Function 'b2' in 'C_isa_sail_templates' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_sail_templates.ml:168:1`

### #305 PHYSICAL_EQUALITY_SMELL on `C_isa_sail_templates.fold`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_sail_templates.ml:333:1`
- **Summary:** Type Safety Hazard (Physical Equality): Function 'fold' in 'C_isa_sail_templates' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs

#### Evidence Trail:
- `+80%` **[PHYSICAL_EQUALITY_COMPARISON]** Type Safety Hazard (Physical Equality): Function 'fold' in 'C_isa_sail_templates' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_sail_templates.ml:333:1`

### #306 PHYSICAL_EQUALITY_SMELL on `C_ephemeral_payload_service.helper_code`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:25:1`
- **Summary:** Type Safety Hazard (Physical Equality): Function 'helper_code' in 'C_ephemeral_payload_service' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs

#### Evidence Trail:
- `+80%` **[PHYSICAL_EQUALITY_COMPARISON]** Type Safety Hazard (Physical Equality): Function 'helper_code' in 'C_ephemeral_payload_service' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:25:1`

### #307 PHYSICAL_EQUALITY_SMELL on `C_anti_debug_service.debug_helper`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_debug_service.ml:15:1`
- **Summary:** Type Safety Hazard (Physical Equality): Function 'debug_helper' in 'C_anti_debug_service' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs

#### Evidence Trail:
- `+80%` **[PHYSICAL_EQUALITY_COMPARISON]** Type Safety Hazard (Physical Equality): Function 'debug_helper' in 'C_anti_debug_service' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_debug_service.ml:15:1`

### #308 PHYSICAL_EQUALITY_SMELL on `C_hook_detect_service.hook_helper`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_hook_detect_service.ml:16:1`
- **Summary:** Type Safety Hazard (Physical Equality): Function 'hook_helper' in 'C_hook_detect_service' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs

#### Evidence Trail:
- `+80%` **[PHYSICAL_EQUALITY_COMPARISON]** Type Safety Hazard (Physical Equality): Function 'hook_helper' in 'C_hook_detect_service' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_hook_detect_service.ml:16:1`

### #309 PHYSICAL_EQUALITY_SMELL on `Make.tmpl`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_concurrent_fiber_runtime.ml:9:1`
- **Summary:** Type Safety Hazard (Physical Equality): Function 'tmpl' in 'Make' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs

#### Evidence Trail:
- `+80%` **[PHYSICAL_EQUALITY_COMPARISON]** Type Safety Hazard (Physical Equality): Function 'tmpl' in 'Make' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_concurrent_fiber_runtime.ml:9:1`

### #310 PHYSICAL_EQUALITY_SMELL on `Make.helper_code`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:22:1`
- **Summary:** Type Safety Hazard (Physical Equality): Function 'helper_code' in 'Make' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs

#### Evidence Trail:
- `+80%` **[PHYSICAL_EQUALITY_COMPARISON]** Type Safety Hazard (Physical Equality): Function 'helper_code' in 'Make' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:22:1`

### #311 PHYSICAL_EQUALITY_SMELL on `Make.debug_helper`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_debug_service.ml:12:1`
- **Summary:** Type Safety Hazard (Physical Equality): Function 'debug_helper' in 'Make' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs

#### Evidence Trail:
- `+80%` **[PHYSICAL_EQUALITY_COMPARISON]** Type Safety Hazard (Physical Equality): Function 'debug_helper' in 'Make' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_debug_service.ml:12:1`

### #312 PHYSICAL_EQUALITY_SMELL on `Make.hook_helper`
- **Category:** `type_safety`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_hook_detect_service.ml:13:1`
- **Summary:** Type Safety Hazard (Physical Equality): Function 'hook_helper' in 'Make' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs

#### Evidence Trail:
- `+80%` **[PHYSICAL_EQUALITY_COMPARISON]** Type Safety Hazard (Physical Equality): Function 'hook_helper' in 'Make' uses physical pointer equality (`==` / `!=`); use structural value equality (`=` / `<>`) to avoid subtle value comparison bugs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_hook_detect_service.ml:13:1`

### #313 GOD_MODULE_SRP on `Vectis_cc`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/bin/vectis_cc.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'Vectis_cc' defines 68 functions across 248 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'Vectis_cc' defines 68 functions across 248 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/bin/vectis_cc.ml:1:1`

### #314 GOD_MODULE_SRP on `Main`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/bin/main.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'Main' defines 81 functions across 356 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'Main' defines 81 functions across 356 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/bin/main.ml:1:1`

### #315 GOD_MODULE_SRP on `Vectis_egraph`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_egraph.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'Vectis_egraph' defines 51 functions across 293 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'Vectis_egraph' defines 51 functions across 293 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/vectis_egraph.ml:1:1`

### #316 GOD_MODULE_SRP on `C_visa_c_runtime`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_visa_c_runtime.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_visa_c_runtime' defines 38 functions across 393 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_visa_c_runtime' defines 38 functions across 393 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_visa_c_runtime.ml:1:1`

### #317 GOD_MODULE_SRP on `C_visa_c_handlers`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_visa_c_handlers.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_visa_c_handlers' defines 39 functions across 520 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_visa_c_handlers' defines 39 functions across 520 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_visa_c_handlers.ml:1:1`

### #318 GOD_MODULE_SRP on `C_visa_profile_service`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_profile_service.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_visa_profile_service' defines 30 functions across 207 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_visa_profile_service' defines 30 functions across 207 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_profile_service.ml:1:1`

### #319 GOD_MODULE_SRP on `C_isa_sail_templates`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_sail_templates.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_isa_sail_templates' defines 71 functions across 458 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_isa_sail_templates' defines 71 functions across 458 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_sail_templates.ml:1:1`

### #320 GOD_MODULE_SRP on `C_isa_synthesizer_service`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_isa_synthesizer_service' defines 82 functions across 468 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_isa_synthesizer_service' defines 82 functions across 468 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:1:1`

### #321 GOD_MODULE_SRP on `C_visa_spec`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_spec.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_visa_spec' defines 40 functions across 293 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_visa_spec' defines 40 functions across 293 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_spec.ml:1:1`

### #322 GOD_MODULE_SRP on `C_arm64_jit_compiler`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_arm64_jit_compiler' defines 75 functions across 336 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_arm64_jit_compiler' defines 75 functions across 336 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:1:1`

### #323 GOD_MODULE_SRP on `C_nested_vm_service`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_nested_vm_service' defines 105 functions across 363 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_nested_vm_service' defines 105 functions across 363 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:1:1`

### #324 GOD_MODULE_SRP on `C_arm64_edsl`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_edsl.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_arm64_edsl' defines 105 functions across 660 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_arm64_edsl' defines 105 functions across 660 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_edsl.ml:1:1`

### #325 GOD_MODULE_SRP on `C_decentralized_dispatcher_service`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_decentralized_dispatcher_service' defines 37 functions across 149 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_decentralized_dispatcher_service' defines 37 functions across 149 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:1:1`

### #326 GOD_MODULE_SRP on `C_visa_spec_service`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_visa_spec_service' defines 56 functions across 229 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_visa_spec_service' defines 56 functions across 229 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:1:1`

### #327 GOD_MODULE_SRP on `C_visa_stmt_compiler`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_stmt_compiler.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_visa_stmt_compiler' defines 38 functions across 217 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_visa_stmt_compiler' defines 38 functions across 217 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_stmt_compiler.ml:1:1`

### #328 GOD_MODULE_SRP on `C_virtualize_service`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_virtualize_service' defines 73 functions across 219 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_virtualize_service' defines 73 functions across 219 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:1:1`

### #329 GOD_MODULE_SRP on `C_visa_expr_compiler`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_expr_compiler.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_visa_expr_compiler' defines 34 functions across 354 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_visa_expr_compiler' defines 34 functions across 354 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_expr_compiler.ml:1:1`

### #330 GOD_MODULE_SRP on `C_merge_functions_service`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_merge_functions_service.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_merge_functions_service' defines 31 functions across 128 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_merge_functions_service' defines 31 functions across 128 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_merge_functions_service.ml:1:1`

### #331 GOD_MODULE_SRP on `C_bpm_mba_service`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_bpm_mba_service.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_bpm_mba_service' defines 32 functions across 141 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_bpm_mba_service' defines 32 functions across 141 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_bpm_mba_service.ml:1:1`

### #332 GOD_MODULE_SRP on `C_encode_literals_service`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_encode_literals_service' defines 42 functions across 151 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_encode_literals_service' defines 42 functions across 151 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:1:1`

### #333 GOD_MODULE_SRP on `C_egraph_mba_service`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_egraph_mba_service' defines 66 functions across 324 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_egraph_mba_service' defines 66 functions across 324 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:1:1`

### #334 GOD_MODULE_SRP on `C_polynomial_mba_service`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_polynomial_mba_service.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_polynomial_mba_service' defines 42 functions across 137 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_polynomial_mba_service' defines 42 functions across 137 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_polynomial_mba_service.ml:1:1`

### #335 GOD_MODULE_SRP on `C_loki_invariant_service`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_loki_invariant_service.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_loki_invariant_service' defines 49 functions across 134 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_loki_invariant_service' defines 49 functions across 134 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_loki_invariant_service.ml:1:1`

### #336 GOD_MODULE_SRP on `C_irreducible_loop_service`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_irreducible_loop_service' defines 30 functions across 137 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_irreducible_loop_service' defines 30 functions across 137 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:1:1`

### #337 GOD_MODULE_SRP on `C_dynamic_opaque_service`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_dynamic_opaque_service.ml:1:1`
- **Summary:** SRP Violation (God Module): Module 'C_dynamic_opaque_service' defines 30 functions across 116 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'C_dynamic_opaque_service' defines 30 functions across 116 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_dynamic_opaque_service.ml:1:1`

### #338 GOD_MODULE_SRP on `Make`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:4:1`
- **Summary:** SRP Violation (God Module): Module 'Make' defines 82 functions across 454 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'Make' defines 82 functions across 454 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:4:1`

### #339 GOD_MODULE_SRP on `Make`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:4:1`
- **Summary:** SRP Violation (God Module): Module 'Make' defines 75 functions across 321 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'Make' defines 75 functions across 321 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:4:1`

### #340 GOD_MODULE_SRP on `Make`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:4:1`
- **Summary:** SRP Violation (God Module): Module 'Make' defines 105 functions across 347 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'Make' defines 105 functions across 347 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:4:1`

### #341 GOD_MODULE_SRP on `Make`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:4:1`
- **Summary:** SRP Violation (God Module): Module 'Make' defines 33 functions across 112 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'Make' defines 33 functions across 112 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:4:1`

### #342 GOD_MODULE_SRP on `Make`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:6:1`
- **Summary:** SRP Violation (God Module): Module 'Make' defines 56 functions across 213 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'Make' defines 56 functions across 213 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:6:1`

### #343 GOD_MODULE_SRP on `Make`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:4:1`
- **Summary:** SRP Violation (God Module): Module 'Make' defines 73 functions across 212 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'Make' defines 73 functions across 212 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:4:1`

### #344 GOD_MODULE_SRP on `Make`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_bpm_mba_service.ml:5:1`
- **Summary:** SRP Violation (God Module): Module 'Make' defines 30 functions across 113 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'Make' defines 30 functions across 113 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_bpm_mba_service.ml:5:1`

### #345 GOD_MODULE_SRP on `Make`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:4:1`
- **Summary:** SRP Violation (God Module): Module 'Make' defines 40 functions across 140 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'Make' defines 40 functions across 140 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:4:1`

### #346 GOD_MODULE_SRP on `Make`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:4:1`
- **Summary:** SRP Violation (God Module): Module 'Make' defines 64 functions across 309 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'Make' defines 64 functions across 309 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:4:1`

### #347 GOD_MODULE_SRP on `Make`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_polynomial_mba_service.ml:4:1`
- **Summary:** SRP Violation (God Module): Module 'Make' defines 40 functions across 120 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'Make' defines 40 functions across 120 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_polynomial_mba_service.ml:4:1`

### #348 GOD_MODULE_SRP on `Make`
- **Category:** `principle`
- **Confidence:** **85%** [VERY_HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_loki_invariant_service.ml:4:1`
- **Summary:** SRP Violation (God Module): Module 'Make' defines 46 functions across 108 lines of code, indicating multiple mixed domain responsibilities

#### Evidence Trail:
- `+85%` **[SRP_GOD_MODULE]** SRP Violation (God Module): Module 'Make' defines 46 functions across 108 lines of code, indicating multiple mixed domain responsibilities -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_loki_invariant_service.ml:4:1`

### #349 CYCLOMATIC_COMPLEXITY_KISS on `C_visa_c_handlers.f_vor1`
- **Category:** `principle`
- **Confidence:** **75%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_visa_c_handlers.ml:129:1`
- **Summary:** KISS Violation (High Complexity): Function 'f_vor1' in 'C_visa_c_handlers' has cyclomatic complexity of 15; decompose nested pattern matches into helper functions

#### Evidence Trail:
- `+75%` **[KISS_HIGH_MATCH_COMPLEXITY]** KISS Violation (High Complexity): Function 'f_vor1' in 'C_visa_c_handlers' has cyclomatic complexity of 15; decompose nested pattern matches into helper functions -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_visa_c_handlers.ml:129:1`

### #350 DUPLICATE_CODE_DRY on `Cil_branch_resolver.intermediate_stream`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/infrastructure/encoders/cil/cil_branch_resolver.ml:29:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Cil_branch_resolver.intermediate_stream, Arm64_branch_resolver.intermediate_stream

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Cil_branch_resolver.intermediate_stream, Arm64_branch_resolver.intermediate_stream -> `/Volumes/External/Code/vectis/lib/infrastructure/encoders/cil/cil_branch_resolver.ml:29:1`

### #351 DUPLICATE_CODE_DRY on `System_entropy_adapter.choose`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/infrastructure/random/system_entropy_adapter.ml:22:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): System_entropy_adapter.choose, Adapter.choose

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): System_entropy_adapter.choose, Adapter.choose -> `/Volumes/External/Code/vectis/lib/infrastructure/random/system_entropy_adapter.ml:22:1`

### #352 DUPLICATE_CODE_DRY on `Vectis_state_masking.b`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:9:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_state_masking.b, KeySchedule.b

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_state_masking.b, KeySchedule.b -> `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:9:1`

### #353 DUPLICATE_CODE_DRY on `Vectis_state_masking.k1`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:16:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_state_masking.k1, KeySchedule.k1

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_state_masking.k1, KeySchedule.k1 -> `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:16:1`

### #354 DUPLICATE_CODE_DRY on `Vectis_state_masking.offset`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:41:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_state_masking.offset, StateMasking.offset

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_state_masking.offset, StateMasking.offset -> `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:41:1`

### #355 DUPLICATE_CODE_DRY on `Vectis_state_masking.mask_value`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:44:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_state_masking.mask_value, StateMasking.mask_value

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_state_masking.mask_value, StateMasking.mask_value -> `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:44:1`

### #356 DUPLICATE_CODE_DRY on `Vectis_state_masking.unmask_value`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:50:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_state_masking.unmask_value, StateMasking.unmask_value

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_state_masking.unmask_value, StateMasking.unmask_value -> `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:50:1`

### #357 DUPLICATE_CODE_DRY on `Vectis_state_masking.ep`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:52:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_state_masking.ep, StateMasking.ep

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_state_masking.ep, StateMasking.ep -> `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:52:1`

### #358 DUPLICATE_CODE_DRY on `Vectis_state_masking.acc`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:91:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_state_masking.acc, Stepper.acc

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_state_masking.acc, Stepper.acc -> `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:91:1`

### #359 DUPLICATE_CODE_DRY on `Vectis_state_masking.invariant`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:94:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_state_masking.invariant, Stepper.invariant

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_state_masking.invariant, Stepper.invariant -> `/Volumes/External/Code/vectis/lib/domain/vectis_state_masking.ml:94:1`

### #360 DUPLICATE_CODE_DRY on `Vectis_egraph.find`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_egraph.ml:33:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 3 location(s): Vectis_egraph.find, C_egraph_mba_service.find, Make.find

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 3 location(s): Vectis_egraph.find, C_egraph_mba_service.find, Make.find -> `/Volumes/External/Code/vectis/lib/domain/vectis_egraph.ml:33:1`

### #361 DUPLICATE_CODE_DRY on `Vectis_egraph.cnode`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_egraph.ml:51:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 3 location(s): Vectis_egraph.cnode, C_egraph_mba_service.cnode, Make.cnode

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 3 location(s): Vectis_egraph.cnode, C_egraph_mba_service.cnode, Make.cnode -> `/Volumes/External/Code/vectis/lib/domain/vectis_egraph.ml:51:1`

### #362 DUPLICATE_CODE_DRY on `Vectis_egraph.new_id`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_egraph.ml:55:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 3 location(s): Vectis_egraph.new_id, C_egraph_mba_service.new_id, Make.new_id

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 3 location(s): Vectis_egraph.new_id, C_egraph_mba_service.new_id, Make.new_id -> `/Volumes/External/Code/vectis/lib/domain/vectis_egraph.ml:55:1`

### #363 DUPLICATE_CODE_DRY on `Cfg.find_block`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/cfg.ml:21:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Cfg.find_block, CFG.find_block

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Cfg.find_block, CFG.find_block -> `/Volumes/External/Code/vectis/lib/domain/cfg.ml:21:1`

### #364 DUPLICATE_CODE_DRY on `Vectis_neural_rewriter.edge_cases`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_neural_rewriter.ml:24:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_neural_rewriter.edge_cases, Verifier.edge_cases

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_neural_rewriter.edge_cases, Verifier.edge_cases -> `/Volumes/External/Code/vectis/lib/domain/vectis_neural_rewriter.ml:24:1`

### #365 DUPLICATE_CODE_DRY on `Vectis_neural_rewriter.collect`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_neural_rewriter.ml:39:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_neural_rewriter.collect, Verifier.collect

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_neural_rewriter.collect, Verifier.collect -> `/Volumes/External/Code/vectis/lib/domain/vectis_neural_rewriter.ml:39:1`

### #366 DUPLICATE_CODE_DRY on `Vectis_neural_rewriter.v2`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_neural_rewriter.ml:52:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_neural_rewriter.v2, Verifier.v2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_neural_rewriter.v2, Verifier.v2 -> `/Volumes/External/Code/vectis/lib/domain/vectis_neural_rewriter.ml:52:1`

### #367 DUPLICATE_CODE_DRY on `Vectis_neural_rewriter.generate_heuristic_candidates`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_neural_rewriter.ml:105:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_neural_rewriter.generate_heuristic_candidates, CandidateGenerator.generate_heuristic_candidates

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_neural_rewriter.generate_heuristic_candidates, CandidateGenerator.generate_heuristic_candidates -> `/Volumes/External/Code/vectis/lib/domain/vectis_neural_rewriter.ml:105:1`

### #368 DUPLICATE_CODE_DRY on `Vectis_neural_rewriter.rewrite`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_neural_rewriter.ml:159:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_neural_rewriter.rewrite, Engine.rewrite

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_neural_rewriter.rewrite, Engine.rewrite -> `/Volumes/External/Code/vectis/lib/domain/vectis_neural_rewriter.ml:159:1`

### #369 DUPLICATE_CODE_DRY on `Vectis_neural_rewriter.candidates`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_neural_rewriter.ml:173:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_neural_rewriter.candidates, Engine.candidates

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_neural_rewriter.candidates, Engine.candidates -> `/Volumes/External/Code/vectis/lib/domain/vectis_neural_rewriter.ml:173:1`

### #370 DUPLICATE_CODE_DRY on `Vectis_neural_rewriter.valid_candidates`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_neural_rewriter.ml:174:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_neural_rewriter.valid_candidates, Engine.valid_candidates

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_neural_rewriter.valid_candidates, Engine.valid_candidates -> `/Volumes/External/Code/vectis/lib/domain/vectis_neural_rewriter.ml:174:1`

### #371 DUPLICATE_CODE_DRY on `Vectis_neural_rewriter.best`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_neural_rewriter.ml:169:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_neural_rewriter.best, Engine.best

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_neural_rewriter.best, Engine.best -> `/Volumes/External/Code/vectis/lib/domain/vectis_neural_rewriter.ml:169:1`

### #372 DUPLICATE_CODE_DRY on `Vectis_neural_rewriter.cid`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/vectis_neural_rewriter.ml:184:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_neural_rewriter.cid, Engine.cid

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Vectis_neural_rewriter.cid, Engine.cid -> `/Volumes/External/Code/vectis/lib/domain/vectis_neural_rewriter.ml:184:1`

### #373 DUPLICATE_CODE_DRY on `Flattening_service.scratch_reg`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:8:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.scratch_reg, Make.scratch_reg

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.scratch_reg, Make.scratch_reg -> `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:8:1`

### #374 DUPLICATE_CODE_DRY on `Flattening_service.state_id`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:24:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.state_id, Make.state_id

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.state_id, Make.state_id -> `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:24:1`

### #375 DUPLICATE_CODE_DRY on `Flattening_service.next_label`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:26:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.next_label, Make.next_label

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.next_label, Make.next_label -> `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:26:1`

### #376 DUPLICATE_CODE_DRY on `Flattening_service.next_idx`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:32:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.next_idx, Make.next_idx

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.next_idx, Make.next_idx -> `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:32:1`

### #377 DUPLICATE_CODE_DRY on `Flattening_service.find_state_by_label`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:41:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.find_state_by_label, Make.find_state_by_label

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.find_state_by_label, Make.find_state_by_label -> `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:41:1`

### #378 DUPLICATE_CODE_DRY on `Flattening_service.filtered_instrs`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:53:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.filtered_instrs, Make.filtered_instrs

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.filtered_instrs, Make.filtered_instrs -> `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:53:1`

### #379 DUPLICATE_CODE_DRY on `Flattening_service.has_ret`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:60:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.has_ret, Make.has_ret

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.has_ret, Make.has_ret -> `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:60:1`

### #380 DUPLICATE_CODE_DRY on `Flattening_service.instructions`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:63:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.instructions, Make.instructions

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.instructions, Make.instructions -> `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:63:1`

### #381 DUPLICATE_CODE_DRY on `Flattening_service.target_state`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:69:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.target_state, Make.target_state

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.target_state, Make.target_state -> `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:69:1`

### #382 DUPLICATE_CODE_DRY on `Flattening_service.dispatcher_instrs`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:83:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.dispatcher_instrs, Make.dispatcher_instrs

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.dispatcher_instrs, Make.dispatcher_instrs -> `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:83:1`

### #383 DUPLICATE_CODE_DRY on `Flattening_service.dispatcher_block`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:94:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.dispatcher_block, Make.dispatcher_block

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.dispatcher_block, Make.dispatcher_block -> `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:94:1`

### #384 DUPLICATE_CODE_DRY on `Flattening_service.entry_trampoline`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:100:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.entry_trampoline, Make.entry_trampoline

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Flattening_service.entry_trampoline, Make.entry_trampoline -> `/Volumes/External/Code/vectis/lib/domain/services/native/flattening_service.ml:100:1`

### #385 DUPLICATE_CODE_DRY on `Mba_service.variant`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/mba_service.ml:63:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Mba_service.variant, Make.variant

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Mba_service.variant, Make.variant -> `/Volumes/External/Code/vectis/lib/domain/services/native/mba_service.ml:63:1`

### #386 DUPLICATE_CODE_DRY on `Mba_service.new_instructions`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/mba_service.ml:85:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Mba_service.new_instructions, Make.new_instructions

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Mba_service.new_instructions, Make.new_instructions -> `/Volumes/External/Code/vectis/lib/domain/services/native/mba_service.ml:85:1`

### #387 DUPLICATE_CODE_DRY on `Opaque_predicate_service.junk_words`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/opaque_predicate_service.ml:12:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Opaque_predicate_service.junk_words, Make.junk_words

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Opaque_predicate_service.junk_words, Make.junk_words -> `/Volumes/External/Code/vectis/lib/domain/services/native/opaque_predicate_service.ml:12:1`

### #388 DUPLICATE_CODE_DRY on `Opaque_predicate_service.predicate_prologue`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/opaque_predicate_service.ml:22:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Opaque_predicate_service.predicate_prologue, Make.predicate_prologue

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Opaque_predicate_service.predicate_prologue, Make.predicate_prologue -> `/Volumes/External/Code/vectis/lib/domain/services/native/opaque_predicate_service.ml:22:1`

### #389 DUPLICATE_CODE_DRY on `Opaque_predicate_service.dead_id`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/native/opaque_predicate_service.ml:31:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Opaque_predicate_service.dead_id, Make.dead_id

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Opaque_predicate_service.dead_id, Make.dead_id -> `/Volumes/External/Code/vectis/lib/domain/services/native/opaque_predicate_service.ml:31:1`

### #390 DUPLICATE_CODE_DRY on `C_concurrent_fiber_runtime.s`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_concurrent_fiber_runtime.ml:12:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_concurrent_fiber_runtime.s, Make.s

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_concurrent_fiber_runtime.s, Make.s -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_concurrent_fiber_runtime.ml:12:1`

### #391 DUPLICATE_CODE_DRY on `C_concurrent_fiber_runtime.tmpl`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_concurrent_fiber_runtime.ml:13:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_concurrent_fiber_runtime.tmpl, Make.tmpl

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_concurrent_fiber_runtime.tmpl, Make.tmpl -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_concurrent_fiber_runtime.ml:13:1`

### #392 DUPLICATE_CODE_DRY on `C_concurrent_fiber_runtime.with_tag`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_concurrent_fiber_runtime.ml:65:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_concurrent_fiber_runtime.with_tag, Make.with_tag

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_concurrent_fiber_runtime.with_tag, Make.with_tag -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/emitter/c_concurrent_fiber_runtime.ml:65:1`

### #393 DUPLICATE_CODE_DRY on `C_isa_synthesizer_service.blocks`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:21:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.blocks, Make.blocks

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.blocks, Make.blocks -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:21:1`

### #394 DUPLICATE_CODE_DRY on `C_isa_synthesizer_service.shift_of`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:23:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.shift_of, Make.shift_of

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.shift_of, Make.shift_of -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:23:1`

### #395 DUPLICATE_CODE_DRY on `C_isa_synthesizer_service.generate_random_visa`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:44:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.generate_random_visa, Make.generate_random_visa

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.generate_random_visa, Make.generate_random_visa -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:44:1`

### #396 DUPLICATE_CODE_DRY on `C_isa_synthesizer_service.isa_name`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:48:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.isa_name, Make.isa_name

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.isa_name, Make.isa_name -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:48:1`

### #397 DUPLICATE_CODE_DRY on `C_isa_synthesizer_service.pack_key`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:102:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 4 location(s): C_isa_synthesizer_service.pack_key, C_isa_synthesizer_service.vkey_seed, Make.pack_key

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 4 location(s): C_isa_synthesizer_service.pack_key, C_isa_synthesizer_service.vkey_seed, Make.pack_key -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:102:1`

### #398 DUPLICATE_CODE_DRY on `C_isa_synthesizer_service.d`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:105:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.d, Make.d

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.d, Make.d -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:105:1`

### #399 DUPLICATE_CODE_DRY on `C_isa_synthesizer_service.opcodes`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:112:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.opcodes, Make.opcodes

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.opcodes, Make.opcodes -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:112:1`

### #400 DUPLICATE_CODE_DRY on `C_isa_synthesizer_service.spec`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:153:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.spec, Make.spec

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.spec, Make.spec -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:153:1`

### #401 DUPLICATE_CODE_DRY on `C_isa_synthesizer_service.json_str`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:331:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.json_str, Make.json_str

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.json_str, Make.json_str -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:331:1`

### #402 DUPLICATE_CODE_DRY on `C_isa_synthesizer_service.sail_str`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:345:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.sail_str, Make.sail_str

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.sail_str, Make.sail_str -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:345:1`

### #403 DUPLICATE_CODE_DRY on `C_isa_synthesizer_service.vm_name`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:324:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.vm_name, Make.vm_name

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.vm_name, Make.vm_name -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:324:1`

### #404 DUPLICATE_CODE_DRY on `C_isa_synthesizer_service.generate_rolling_vkey`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:274:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.generate_rolling_vkey, Make.generate_rolling_vkey

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.generate_rolling_vkey, Make.generate_rolling_vkey -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:274:1`

### #405 DUPLICATE_CODE_DRY on `C_isa_synthesizer_service.lcg_mult`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:285:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.lcg_mult, Make.lcg_mult

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.lcg_mult, Make.lcg_mult -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:285:1`

### #406 DUPLICATE_CODE_DRY on `C_isa_synthesizer_service.lcg_delta`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:290:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.lcg_delta, Make.lcg_delta

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.lcg_delta, Make.lcg_delta -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:290:1`

### #407 DUPLICATE_CODE_DRY on `C_isa_synthesizer_service.generate_ephemeral_vm`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:320:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.generate_ephemeral_vm, Make.generate_ephemeral_vm

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.generate_ephemeral_vm, Make.generate_ephemeral_vm -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:320:1`

### #408 DUPLICATE_CODE_DRY on `C_isa_synthesizer_service.oc`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:353:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.oc, Make.oc

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.oc, Make.oc -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:353:1`

### #409 DUPLICATE_CODE_DRY on `C_isa_synthesizer_service.visa_name`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:365:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.visa_name, Make.visa_name

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.visa_name, Make.visa_name -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:365:1`

### #410 DUPLICATE_CODE_DRY on `C_isa_synthesizer_service.synthesize_8vcpu_cascade`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:389:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.synthesize_8vcpu_cascade, Make.synthesize_8vcpu_cascade

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_isa_synthesizer_service.synthesize_8vcpu_cascade, Make.synthesize_8vcpu_cascade -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_isa_synthesizer_service.ml:389:1`

### #411 DUPLICATE_CODE_DRY on `C_visa_decoy_generator.funct6_choices`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_decoy_generator.ml:8:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_decoy_generator.funct6_choices, Make.funct6_choices

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_decoy_generator.funct6_choices, Make.funct6_choices -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_decoy_generator.ml:8:1`

### #412 DUPLICATE_CODE_DRY on `C_visa_decoy_generator.funct6`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_decoy_generator.ml:14:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_decoy_generator.funct6, Make.funct6

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_decoy_generator.funct6, Make.funct6 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_decoy_generator.ml:14:1`

### #413 DUPLICATE_CODE_DRY on `C_visa_decoy_generator.vd`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_decoy_generator.ml:19:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_decoy_generator.vd, Make.vd

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_decoy_generator.vd, Make.vd -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/specs/c_visa_decoy_generator.ml:19:1`

### #414 DUPLICATE_CODE_DRY on `C_self_modifying_vm_service.should_transform`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:7:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.should_transform, Make.should_transform

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.should_transform, Make.should_transform -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:7:1`

### #415 DUPLICATE_CODE_DRY on `C_self_modifying_vm_service.transform_function`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:14:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.transform_function, Make.transform_function

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.transform_function, Make.transform_function -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:14:1`

### #416 DUPLICATE_CODE_DRY on `C_self_modifying_vm_service.array_type`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:25:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.array_type, Make.array_type

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.array_type, Make.array_type -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:25:1`

### #417 DUPLICATE_CODE_DRY on `C_self_modifying_vm_service.bc_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:26:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 4 location(s): C_self_modifying_vm_service.bc_var, C_virtualize_service.bc_var, Make.bc_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 4 location(s): C_self_modifying_vm_service.bc_var, C_virtualize_service.bc_var, Make.bc_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:26:1`

### #418 DUPLICATE_CODE_DRY on `C_self_modifying_vm_service.init_entries`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:29:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.init_entries, Make.init_entries

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.init_entries, Make.init_entries -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:29:1`

### #419 DUPLICATE_CODE_DRY on `C_self_modifying_vm_service.int_formals`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:37:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 4 location(s): C_self_modifying_vm_service.int_formals, C_jitify_service.int_formals, Make.int_formals

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 4 location(s): C_self_modifying_vm_service.int_formals, C_jitify_service.int_formals, Make.int_formals -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:37:1`

### #420 DUPLICATE_CODE_DRY on `C_self_modifying_vm_service.init_pc`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:43:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 4 location(s): C_self_modifying_vm_service.init_pc, C_virtualize_service.init_pc, Make.init_pc

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 4 location(s): C_self_modifying_vm_service.init_pc, C_virtualize_service.init_pc, Make.init_pc -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:43:1`

### #421 DUPLICATE_CODE_DRY on `C_self_modifying_vm_service.init_acc`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:44:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.init_acc, Make.init_acc

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.init_acc, Make.init_acc -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:44:1`

### #422 DUPLICATE_CODE_DRY on `C_self_modifying_vm_service.break_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:51:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.break_stmt, Make.break_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.break_stmt, Make.break_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:51:1`

### #423 DUPLICATE_CODE_DRY on `C_self_modifying_vm_service.read_raw`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:56:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 6 location(s): C_self_modifying_vm_service.read_raw, C_virtualize_service.reg_idx_exp, C_virtualize_service.c_byte0

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 6 location(s): C_self_modifying_vm_service.read_raw, C_virtualize_service.reg_idx_exp, C_virtualize_service.c_byte0 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:56:1`

### #424 DUPLICATE_CODE_DRY on `C_self_modifying_vm_service.decrypt_op`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:57:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.decrypt_op, Make.decrypt_op

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.decrypt_op, Make.decrypt_op -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:57:1`

### #425 DUPLICATE_CODE_DRY on `C_self_modifying_vm_service.re_enc`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:59:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.re_enc, Make.re_enc

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.re_enc, Make.re_enc -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:59:1`

### #426 DUPLICATE_CODE_DRY on `C_self_modifying_vm_service.write_back`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:60:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.write_back, Make.write_back

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.write_back, Make.write_back -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:60:1`

### #427 DUPLICATE_CODE_DRY on `C_self_modifying_vm_service.exec_step`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:62:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.exec_step, Make.exec_step

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.exec_step, Make.exec_step -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:62:1`

### #428 DUPLICATE_CODE_DRY on `C_self_modifying_vm_service.inc_pc`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:65:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 8 location(s): C_self_modifying_vm_service.inc_pc, C_virtualize_service.inc_pc, C_virtualize_service.inc_pc_arg

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 8 location(s): C_self_modifying_vm_service.inc_pc, C_virtualize_service.inc_pc, C_virtualize_service.inc_pc_arg -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:65:1`

### #429 DUPLICATE_CODE_DRY on `C_self_modifying_vm_service.loop_body`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:67:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.loop_body, Make.loop_body

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.loop_body, Make.loop_body -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:67:1`

### #430 DUPLICATE_CODE_DRY on `C_self_modifying_vm_service.sm_loop`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:68:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.sm_loop, Make.sm_loop

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.sm_loop, Make.sm_loop -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:68:1`

### #431 DUPLICATE_CODE_DRY on `C_self_modifying_vm_service.ret_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:69:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.ret_stmt, Make.ret_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.ret_stmt, Make.ret_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:69:1`

### #432 DUPLICATE_CODE_DRY on `C_self_modifying_vm_service.funcs`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:75:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.funcs, C_nested_vm_service.funcs

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_modifying_vm_service.funcs, C_nested_vm_service.funcs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:75:1`

### #433 DUPLICATE_CODE_DRY on `C_rolling_vkey_service.should_transform`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:5:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.should_transform, Make.should_transform

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.should_transform, Make.should_transform -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:5:1`

### #434 DUPLICATE_CODE_DRY on `C_rolling_vkey_service.int_formals`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:12:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 4 location(s): C_rolling_vkey_service.int_formals, C_ephemeral_payload_service.int_formals, Make.int_formals

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 4 location(s): C_rolling_vkey_service.int_formals, C_ephemeral_payload_service.int_formals, Make.int_formals -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:12:1`

### #435 DUPLICATE_CODE_DRY on `C_rolling_vkey_service.func_count`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:18:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.func_count, Make.func_count

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.func_count, Make.func_count -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:18:1`

### #436 DUPLICATE_CODE_DRY on `C_rolling_vkey_service.prog_name`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:25:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.prog_name, Make.prog_name

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.prog_name, Make.prog_name -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:25:1`

### #437 DUPLICATE_CODE_DRY on `C_rolling_vkey_service.vkey_seed`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:28:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 4 location(s): C_rolling_vkey_service.vkey_seed, C_rolling_vkey_service.lcg_delta, Make.vkey_seed

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 4 location(s): C_rolling_vkey_service.vkey_seed, C_rolling_vkey_service.lcg_delta, Make.vkey_seed -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:28:1`

### #438 DUPLICATE_CODE_DRY on `C_rolling_vkey_service.lcg_mult`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:30:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.lcg_mult, Make.lcg_mult

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.lcg_mult, Make.lcg_mult -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:30:1`

### #439 DUPLICATE_CODE_DRY on `C_rolling_vkey_service.op_pool`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:35:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.op_pool, Make.op_pool

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.op_pool, Make.op_pool -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:35:1`

### #440 DUPLICATE_CODE_DRY on `C_rolling_vkey_service.shuffled`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:38:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.shuffled, Make.shuffled

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.shuffled, Make.shuffled -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:38:1`

### #441 DUPLICATE_CODE_DRY on `C_rolling_vkey_service.raw_ops`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:42:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.raw_ops, Make.raw_ops

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.raw_ops, Make.raw_ops -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:42:1`

### #442 DUPLICATE_CODE_DRY on `C_rolling_vkey_service.term`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:52:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.term, Make.term

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.term, Make.term -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:52:1`

### #443 DUPLICATE_CODE_DRY on `C_rolling_vkey_service.init_list`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:58:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.init_list, Make.init_list

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.init_list, Make.init_list -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:58:1`

### #444 DUPLICATE_CODE_DRY on `C_rolling_vkey_service.arr_type`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:62:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.arr_type, Make.arr_type

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.arr_type, Make.arr_type -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:62:1`

### #445 DUPLICATE_CODE_DRY on `C_rolling_vkey_service.gvar`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:63:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.gvar, Make.gvar

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_rolling_vkey_service.gvar, Make.gvar -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:63:1`

### #446 DUPLICATE_CODE_DRY on `C_rolling_vkey_service.ginit`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:65:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 4 location(s): C_rolling_vkey_service.ginit, C_ephemeral_payload_service.ginit, Make.ginit

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 4 location(s): C_rolling_vkey_service.ginit, C_ephemeral_payload_service.ginit, Make.ginit -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_rolling_vkey_service.ml:65:1`

### #447 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.b1`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:13:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.b1, Make.b1

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.b1, Make.b1 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:13:1`

### #448 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.b2`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:14:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.b2, Make.b2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.b2, Make.b2 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:14:1`

### #449 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.b3`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:15:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.b3, Make.b3

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.b3, Make.b3 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:15:1`

### #450 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.movz`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:22:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.movz, Make.movz

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.movz, Make.movz -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:22:1`

### #451 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.movk`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:25:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.movk, Make.movk

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.movk, Make.movk -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:25:1`

### #452 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.enc_mov_reg`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:28:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_mov_reg, Make.enc_mov_reg

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_mov_reg, Make.enc_mov_reg -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:28:1`

### #453 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.enc_add`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:31:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_add, Make.enc_add

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_add, Make.enc_add -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:31:1`

### #454 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.imm12`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:78:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.imm12, Make.imm12

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.imm12, Make.imm12 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:78:1`

### #455 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.enc_sub`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:38:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_sub, Make.enc_sub

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_sub, Make.enc_sub -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:38:1`

### #456 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.enc_mul`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:45:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_mul, Make.enc_mul

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_mul, Make.enc_mul -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:45:1`

### #457 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.enc_and`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:48:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_and, Make.enc_and

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_and, Make.enc_and -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:48:1`

### #458 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.enc_orr`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:51:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_orr, Make.enc_orr

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_orr, Make.enc_orr -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:51:1`

### #459 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.enc_eor`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:54:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_eor, Make.enc_eor

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_eor, Make.enc_eor -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:54:1`

### #460 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.enc_mvn`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:57:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_mvn, Make.enc_mvn

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_mvn, Make.enc_mvn -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:57:1`

### #461 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.enc_neg`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:60:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_neg, Make.enc_neg

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_neg, Make.enc_neg -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:60:1`

### #462 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.imms`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:71:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.imms, Make.imms

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.imms, Make.imms -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:71:1`

### #463 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.enc_cmp`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:74:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_cmp, Make.enc_cmp

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_cmp, Make.enc_cmp -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:74:1`

### #464 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.inv_code`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:83:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.inv_code, Make.inv_code

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.inv_code, Make.inv_code -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:83:1`

### #465 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.code`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:162:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.code, Make.code

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.code, Make.code -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:162:1`

### #466 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.imm`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:102:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.imm, Make.imm

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.imm, Make.imm -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:102:1`

### #467 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.enc_b_uncond`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:105:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_b_uncond, Make.enc_b_uncond

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_b_uncond, Make.enc_b_uncond -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:105:1`

### #468 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.enc_hint`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:113:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_hint, Make.enc_hint

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.enc_hint, Make.enc_hint -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:113:1`

### #469 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.gen_decoy_insn`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:120:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.gen_decoy_insn, Make.gen_decoy_insn

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.gen_decoy_insn, Make.gen_decoy_insn -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:120:1`

### #470 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.sled_len`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:132:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.sled_len, Make.sled_len

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.sled_len, Make.sled_len -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:132:1`

### #471 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.compile_exp`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:147:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.compile_exp, Make.compile_exp

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.compile_exp, Make.compile_exp -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:147:1`

### #472 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.combine`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:167:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.combine, Make.combine

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.combine, Make.combine -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:167:1`

### #473 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.else_code`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:236:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.else_code, Make.else_code

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.else_code, Make.else_code -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:236:1`

### #474 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.compile_stmts`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:208:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.compile_stmts, Make.compile_stmts

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.compile_stmts, Make.compile_stmts -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:208:1`

### #475 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.eval_code`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:213:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.eval_code, Make.eval_code

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.eval_code, Make.eval_code -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:213:1`

### #476 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.dest_r`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:221:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.dest_r, Make.dest_r

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.dest_r, Make.dest_r -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:221:1`

### #477 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.new_r`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:224:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.new_r, Make.new_r

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.new_r, Make.new_r -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:224:1`

### #478 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.saved_r`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:256:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.saved_r, Make.saved_r

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.saved_r, Make.saved_r -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:256:1`

### #479 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.complete_items`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:271:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.complete_items, Make.complete_items

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.complete_items, Make.complete_items -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:271:1`

### #480 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.word_pos`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:294:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.word_pos, Make.word_pos

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.word_pos, Make.word_pos -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:294:1`

### #481 DUPLICATE_CODE_DRY on `C_arm64_jit_compiler.final_words`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:303:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.final_words, Make.final_words

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_arm64_jit_compiler.final_words, Make.final_words -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_arm64_jit_compiler.ml:303:1`

### #482 DUPLICATE_CODE_DRY on `C_nested_vm_service.should_transform`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:7:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.should_transform, Make.should_transform

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.should_transform, Make.should_transform -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:7:1`

### #483 DUPLICATE_CODE_DRY on `C_nested_vm_service.transform_function`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:18:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.transform_function, Make.transform_function

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.transform_function, Make.transform_function -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:18:1`

### #484 DUPLICATE_CODE_DRY on `C_nested_vm_service.outer_bc_name`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:22:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_bc_name, Make.outer_bc_name

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_bc_name, Make.outer_bc_name -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:22:1`

### #485 DUPLICATE_CODE_DRY on `C_nested_vm_service.inner_bc_name`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:23:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_bc_name, Make.inner_bc_name

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_bc_name, Make.inner_bc_name -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:23:1`

### #486 DUPLICATE_CODE_DRY on `C_nested_vm_service.outer_ops`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:29:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 4 location(s): C_nested_vm_service.outer_ops, C_nested_vm_service.inner_ops, Make.outer_ops

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 4 location(s): C_nested_vm_service.outer_ops, C_nested_vm_service.inner_ops, Make.outer_ops -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:29:1`

### #487 DUPLICATE_CODE_DRY on `C_nested_vm_service.raw_inner`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:46:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.raw_inner, Make.raw_inner

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.raw_inner, Make.raw_inner -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:46:1`

### #488 DUPLICATE_CODE_DRY on `C_nested_vm_service.raw_outer`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:66:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.raw_outer, Make.raw_outer

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.raw_outer, Make.raw_outer -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:66:1`

### #489 DUPLICATE_CODE_DRY on `C_nested_vm_service.packed_inner`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:74:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.packed_inner, Make.packed_inner

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.packed_inner, Make.packed_inner -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:74:1`

### #490 DUPLICATE_CODE_DRY on `C_nested_vm_service.packed_outer`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:77:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.packed_outer, Make.packed_outer

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.packed_outer, Make.packed_outer -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:77:1`

### #491 DUPLICATE_CODE_DRY on `C_nested_vm_service.outer_arr_ty`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:82:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_arr_ty, Make.outer_arr_ty

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_arr_ty, Make.outer_arr_ty -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:82:1`

### #492 DUPLICATE_CODE_DRY on `C_nested_vm_service.inner_arr_ty`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:83:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_arr_ty, Make.inner_arr_ty

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_arr_ty, Make.inner_arr_ty -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:83:1`

### #493 DUPLICATE_CODE_DRY on `C_nested_vm_service.outer_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:85:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_var, Make.outer_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_var, Make.outer_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:85:1`

### #494 DUPLICATE_CODE_DRY on `C_nested_vm_service.inner_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:87:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_var, Make.inner_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_var, Make.inner_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:87:1`

### #495 DUPLICATE_CODE_DRY on `C_nested_vm_service.outer_inits`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:90:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_inits, Make.outer_inits

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_inits, Make.outer_inits -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:90:1`

### #496 DUPLICATE_CODE_DRY on `C_nested_vm_service.inner_inits`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:93:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_inits, Make.inner_inits

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_inits, Make.inner_inits -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:93:1`

### #497 DUPLICATE_CODE_DRY on `C_nested_vm_service.vregs`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:110:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.vregs, Make.vregs

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.vregs, Make.vregs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:110:1`

### #498 DUPLICATE_CODE_DRY on `C_nested_vm_service.init_outer_pc`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:120:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.init_outer_pc, Make.init_outer_pc

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.init_outer_pc, Make.init_outer_pc -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:120:1`

### #499 DUPLICATE_CODE_DRY on `C_nested_vm_service.init_outer_run`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:121:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.init_outer_run, Make.init_outer_run

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.init_outer_run, Make.init_outer_run -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:121:1`

### #500 DUPLICATE_CODE_DRY on `C_nested_vm_service.init_inner_key`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:122:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.init_inner_key, Make.init_inner_key

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.init_inner_key, Make.init_inner_key -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:122:1`

### #501 DUPLICATE_CODE_DRY on `C_nested_vm_service.init_res`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:123:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.init_res, Make.init_res

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.init_res, Make.init_res -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:123:1`

### #502 DUPLICATE_CODE_DRY on `C_nested_vm_service.inner_fetch_raw`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:128:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_fetch_raw, Make.inner_fetch_raw

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_fetch_raw, Make.inner_fetch_raw -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:128:1`

### #503 DUPLICATE_CODE_DRY on `C_nested_vm_service.inner_key_formula`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:129:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_key_formula, Make.inner_key_formula

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_key_formula, Make.inner_key_formula -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:129:1`

### #504 DUPLICATE_CODE_DRY on `C_nested_vm_service.inner_decrypt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:133:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_decrypt, Make.inner_decrypt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_decrypt, Make.inner_decrypt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:133:1`

### #505 DUPLICATE_CODE_DRY on `C_nested_vm_service.inner_inc_pc`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:136:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 6 location(s): C_nested_vm_service.inner_inc_pc, C_nested_vm_service.inc2, C_nested_vm_service.inc3

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 6 location(s): C_nested_vm_service.inner_inc_pc, C_nested_vm_service.inc2, C_nested_vm_service.inc3 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:136:1`

### #506 DUPLICATE_CODE_DRY on `C_nested_vm_service.fetch_arg`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:142:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.fetch_arg, Make.fetch_arg

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.fetch_arg, Make.fetch_arg -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:142:1`

### #507 DUPLICATE_CODE_DRY on `C_nested_vm_service.inc1`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:293:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 4 location(s): C_nested_vm_service.inc1, C_nested_vm_service.outer_inc_pc, Make.inc1

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 4 location(s): C_nested_vm_service.inc1, C_nested_vm_service.outer_inc_pc, Make.inc1 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:293:1`

### #508 DUPLICATE_CODE_DRY on `C_nested_vm_service.fetch_dst`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:198:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.fetch_dst, Make.fetch_dst

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.fetch_dst, Make.fetch_dst -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:198:1`

### #509 DUPLICATE_CODE_DRY on `C_nested_vm_service.val_to_load`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:154:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.val_to_load, Make.val_to_load

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.val_to_load, Make.val_to_load -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:154:1`

### #510 DUPLICATE_CODE_DRY on `C_nested_vm_service.store_reg`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:187:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.store_reg, Make.store_reg

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.store_reg, Make.store_reg -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:187:1`

### #511 DUPLICATE_CODE_DRY on `C_nested_vm_service.st`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:317:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.st, Make.st

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.st, Make.st -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:317:1`

### #512 DUPLICATE_CODE_DRY on `C_nested_vm_service.fetch_imm`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:175:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.fetch_imm, Make.fetch_imm

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.fetch_imm, Make.fetch_imm -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:175:1`

### #513 DUPLICATE_CODE_DRY on `C_nested_vm_service.fetch_s1`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:204:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 4 location(s): C_nested_vm_service.fetch_s1, C_nested_vm_service.fetch_src, Make.fetch_s1

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 4 location(s): C_nested_vm_service.fetch_s1, C_nested_vm_service.fetch_src, Make.fetch_s1 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:204:1`

### #514 DUPLICATE_CODE_DRY on `C_nested_vm_service.fetch_s2`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:210:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.fetch_s2, Make.fetch_s2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.fetch_s2, Make.fetch_s2 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:210:1`

### #515 DUPLICATE_CODE_DRY on `C_nested_vm_service.store`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:219:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.store, Make.store

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.store, Make.store -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:219:1`

### #516 DUPLICATE_CODE_DRY on `C_nested_vm_service.res_set`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:239:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.res_set, Make.res_set

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.res_set, Make.res_set -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:239:1`

### #517 DUPLICATE_CODE_DRY on `C_nested_vm_service.stop_inner`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:240:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.stop_inner, Make.stop_inner

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.stop_inner, Make.stop_inner -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:240:1`

### #518 DUPLICATE_CODE_DRY on `C_nested_vm_service.inner_switch`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:247:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_switch, Make.inner_switch

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_switch, Make.inner_switch -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:247:1`

### #519 DUPLICATE_CODE_DRY on `C_nested_vm_service.inner_break_guard`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:253:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_break_guard, Make.inner_break_guard

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_break_guard, Make.inner_break_guard -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:253:1`

### #520 DUPLICATE_CODE_DRY on `C_nested_vm_service.inner_loop_body`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:258:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_loop_body, Make.inner_loop_body

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_loop_body, Make.inner_loop_body -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:258:1`

### #521 DUPLICATE_CODE_DRY on `C_nested_vm_service.inner_loop`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:259:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_loop, Make.inner_loop

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.inner_loop, Make.inner_loop -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:259:1`

### #522 DUPLICATE_CODE_DRY on `C_nested_vm_service.outer_fetch_raw`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:264:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_fetch_raw, Make.outer_fetch_raw

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_fetch_raw, Make.outer_fetch_raw -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:264:1`

### #523 DUPLICATE_CODE_DRY on `C_nested_vm_service.outer_key_formula`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:265:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_key_formula, Make.outer_key_formula

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_key_formula, Make.outer_key_formula -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:265:1`

### #524 DUPLICATE_CODE_DRY on `C_nested_vm_service.outer_decrypt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:269:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_decrypt, Make.outer_decrypt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_decrypt, Make.outer_decrypt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:269:1`

### #525 DUPLICATE_CODE_DRY on `C_nested_vm_service.init_in_pc`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:278:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.init_in_pc, Make.init_in_pc

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.init_in_pc, Make.init_in_pc -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:278:1`

### #526 DUPLICATE_CODE_DRY on `C_nested_vm_service.init_in_run`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:279:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.init_in_run, Make.init_in_run

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.init_in_run, Make.init_in_run -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:279:1`

### #527 DUPLICATE_CODE_DRY on `C_nested_vm_service.fetch_delta`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:288:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.fetch_delta, Make.fetch_delta

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.fetch_delta, Make.fetch_delta -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:288:1`

### #528 DUPLICATE_CODE_DRY on `C_nested_vm_service.rotate`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:294:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.rotate, Make.rotate

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.rotate, Make.rotate -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:294:1`

### #529 DUPLICATE_CODE_DRY on `C_nested_vm_service.stop_out`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:315:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.stop_out, Make.stop_out

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.stop_out, Make.stop_out -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:315:1`

### #530 DUPLICATE_CODE_DRY on `C_nested_vm_service.outer_switch`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:322:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_switch, Make.outer_switch

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_switch, Make.outer_switch -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:322:1`

### #531 DUPLICATE_CODE_DRY on `C_nested_vm_service.outer_break_guard`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:327:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_break_guard, Make.outer_break_guard

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_break_guard, Make.outer_break_guard -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:327:1`

### #532 DUPLICATE_CODE_DRY on `C_nested_vm_service.outer_loop_body`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:332:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_loop_body, Make.outer_loop_body

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_loop_body, Make.outer_loop_body -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:332:1`

### #533 DUPLICATE_CODE_DRY on `C_nested_vm_service.outer_loop`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:333:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_loop, Make.outer_loop

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.outer_loop, Make.outer_loop -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:333:1`

### #534 DUPLICATE_CODE_DRY on `C_nested_vm_service.ret_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:335:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.ret_stmt, Make.ret_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_nested_vm_service.ret_stmt, Make.ret_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_nested_vm_service.ml:335:1`

### #535 DUPLICATE_CODE_DRY on `C_jitify_service.should_transform`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:7:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_jitify_service.should_transform, Make.should_transform

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_jitify_service.should_transform, Make.should_transform -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:7:1`

### #536 DUPLICATE_CODE_DRY on `C_jitify_service.transform_function`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:15:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_jitify_service.transform_function, Make.transform_function

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_jitify_service.transform_function, Make.transform_function -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:15:1`

### #537 DUPLICATE_CODE_DRY on `C_jitify_service.polyglot_table`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:22:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_jitify_service.polyglot_table, Make.polyglot_table

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_jitify_service.polyglot_table, Make.polyglot_table -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:22:1`

### #538 DUPLICATE_CODE_DRY on `C_jitify_service.variant_idx`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:57:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_jitify_service.variant_idx, Make.variant_idx

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_jitify_service.variant_idx, Make.variant_idx -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:57:1`

### #539 DUPLICATE_CODE_DRY on `C_jitify_service.array_type`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:61:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_jitify_service.array_type, Make.array_type

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_jitify_service.array_type, Make.array_type -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:61:1`

### #540 DUPLICATE_CODE_DRY on `C_jitify_service.buf_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:62:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_jitify_service.buf_var, Make.buf_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_jitify_service.buf_var, Make.buf_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:62:1`

### #541 DUPLICATE_CODE_DRY on `C_jitify_service.inits`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:65:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_jitify_service.inits, Make.inits

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_jitify_service.inits, Make.inits -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:65:1`

### #542 DUPLICATE_CODE_DRY on `C_jitify_service.arg_val`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:75:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_jitify_service.arg_val, Make.arg_val

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_jitify_service.arg_val, Make.arg_val -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:75:1`

### #543 DUPLICATE_CODE_DRY on `C_jitify_service.compute_jit`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:80:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_jitify_service.compute_jit, Make.compute_jit

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_jitify_service.compute_jit, Make.compute_jit -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:80:1`

### #544 DUPLICATE_CODE_DRY on `C_jitify_service.ret_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:83:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_jitify_service.ret_stmt, Make.ret_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_jitify_service.ret_stmt, Make.ret_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_jitify_service.ml:83:1`

### #545 DUPLICATE_CODE_DRY on `C_micro_dispatcher_service.should_transform`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_micro_dispatcher_service.ml:7:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 8 location(s): C_micro_dispatcher_service.should_transform, C_vpc_path_invalidation_service.should_transform, C_loki_invariant_service.should_transform

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 8 location(s): C_micro_dispatcher_service.should_transform, C_vpc_path_invalidation_service.should_transform, C_loki_invariant_service.should_transform -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_micro_dispatcher_service.ml:7:1`

### #546 DUPLICATE_CODE_DRY on `C_micro_dispatcher_service.r3`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_micro_dispatcher_service.ml:17:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_micro_dispatcher_service.r3, Make.r3

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_micro_dispatcher_service.r3, Make.r3 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_micro_dispatcher_service.ml:17:1`

### #547 DUPLICATE_CODE_DRY on `C_micro_dispatcher_service.st`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_micro_dispatcher_service.ml:31:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_micro_dispatcher_service.st, Make.st

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_micro_dispatcher_service.st, Make.st -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_micro_dispatcher_service.ml:31:1`

### #548 DUPLICATE_CODE_DRY on `C_micro_dispatcher_service.final_list`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_micro_dispatcher_service.ml:37:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_micro_dispatcher_service.final_list, Make.final_list

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_micro_dispatcher_service.final_list, Make.final_list -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_micro_dispatcher_service.ml:37:1`

### #549 DUPLICATE_CODE_DRY on `C_micro_dispatcher_service.goto_next`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_micro_dispatcher_service.ml:43:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_micro_dispatcher_service.goto_next, Make.goto_next

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_micro_dispatcher_service.goto_next, Make.goto_next -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_micro_dispatcher_service.ml:43:1`

### #550 DUPLICATE_CODE_DRY on `C_micro_dispatcher_service.trap_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_micro_dispatcher_service.ml:48:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_micro_dispatcher_service.trap_stmt, Make.trap_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_micro_dispatcher_service.trap_stmt, Make.trap_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_micro_dispatcher_service.ml:48:1`

### #551 DUPLICATE_CODE_DRY on `C_vcpu_context_scramble_service.is_target_func`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:5:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 4 location(s): C_vcpu_context_scramble_service.is_target_func, C_loop_to_recursion_service.is_target_func, Make.is_target_func

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 4 location(s): C_vcpu_context_scramble_service.is_target_func, C_loop_to_recursion_service.is_target_func, Make.is_target_func -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:5:1`

### #552 DUPLICATE_CODE_DRY on `C_vcpu_context_scramble_service.func_count`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:12:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_vcpu_context_scramble_service.func_count, Make.func_count

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_vcpu_context_scramble_service.func_count, Make.func_count -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:12:1`

### #553 DUPLICATE_CODE_DRY on `C_vcpu_context_scramble_service.type_name`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:19:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_vcpu_context_scramble_service.type_name, Make.type_name

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_vcpu_context_scramble_service.type_name, Make.type_name -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:19:1`

### #554 DUPLICATE_CODE_DRY on `C_vcpu_context_scramble_service.base_fields`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:22:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_vcpu_context_scramble_service.base_fields, Make.base_fields

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_vcpu_context_scramble_service.base_fields, Make.base_fields -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:22:1`

### #555 DUPLICATE_CODE_DRY on `C_vcpu_context_scramble_service.h_b`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:37:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_vcpu_context_scramble_service.h_b, Make.h_b

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_vcpu_context_scramble_service.h_b, Make.h_b -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:37:1`

### #556 DUPLICATE_CODE_DRY on `C_vcpu_context_scramble_service.struct_def`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:42:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_vcpu_context_scramble_service.struct_def, Make.struct_def

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_vcpu_context_scramble_service.struct_def, Make.struct_def -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:42:1`

### #557 DUPLICATE_CODE_DRY on `C_vcpu_context_scramble_service.fn_impl`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:53:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_vcpu_context_scramble_service.fn_impl, Make.fn_impl

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_vcpu_context_scramble_service.fn_impl, Make.fn_impl -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vcpu_context_scramble_service.ml:53:1`

### #558 DUPLICATE_CODE_DRY on `C_decentralized_dispatcher_service.clean_labels`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:8:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.clean_labels, Make.clean_labels

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.clean_labels, Make.clean_labels -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:8:1`

### #559 DUPLICATE_CODE_DRY on `C_decentralized_dispatcher_service.strip_breaks`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:9:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.strip_breaks, Make.strip_breaks

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.strip_breaks, Make.strip_breaks -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:9:1`

### #560 DUPLICATE_CODE_DRY on `C_decentralized_dispatcher_service.new_stmts`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:13:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.new_stmts, Make.new_stmts

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.new_stmts, Make.new_stmts -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:13:1`

### #561 DUPLICATE_CODE_DRY on `C_decentralized_dispatcher_service.cleaned`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:17:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.cleaned, Make.cleaned

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.cleaned, Make.cleaned -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:17:1`

### #562 DUPLICATE_CODE_DRY on `C_decentralized_dispatcher_service.build_binary_dispatcher`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:22:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.build_binary_dispatcher, Make.build_binary_dispatcher

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.build_binary_dispatcher, Make.build_binary_dispatcher -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:22:1`

### #563 DUPLICATE_CODE_DRY on `C_decentralized_dispatcher_service.right_cases`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:33:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.right_cases, Make.right_cases

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.right_cases, Make.right_cases -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:33:1`

### #564 DUPLICATE_CODE_DRY on `C_decentralized_dispatcher_service.right_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:37:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.right_stmt, Make.right_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.right_stmt, Make.right_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:37:1`

### #565 DUPLICATE_CODE_DRY on `C_decentralized_dispatcher_service.decoy_state`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:43:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.decoy_state, Make.decoy_state

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.decoy_state, Make.decoy_state -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:43:1`

### #566 DUPLICATE_CODE_DRY on `C_decentralized_dispatcher_service.decoy_sink`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:44:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.decoy_sink, Make.decoy_sink

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.decoy_sink, Make.decoy_sink -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:44:1`

### #567 DUPLICATE_CODE_DRY on `C_decentralized_dispatcher_service.dh_x_sq`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:45:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.dh_x_sq, Make.dh_x_sq

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.dh_x_sq, Make.dh_x_sq -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:45:1`

### #568 DUPLICATE_CODE_DRY on `C_decentralized_dispatcher_service.assign_sq`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:48:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.assign_sq, Make.assign_sq

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.assign_sq, Make.assign_sq -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:48:1`

### #569 DUPLICATE_CODE_DRY on `C_decentralized_dispatcher_service.fake_body`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:62:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.fake_body, Make.fake_body

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.fake_body, Make.fake_body -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:62:1`

### #570 DUPLICATE_CODE_DRY on `C_decentralized_dispatcher_service.case_st`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:68:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.case_st, Make.case_st

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.case_st, Make.case_st -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:68:1`

### #571 DUPLICATE_CODE_DRY on `C_decentralized_dispatcher_service.decoy_switch`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:73:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.decoy_switch, Make.decoy_switch

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.decoy_switch, Make.decoy_switch -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:73:1`

### #572 DUPLICATE_CODE_DRY on `C_decentralized_dispatcher_service.find_case_labels`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:88:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.find_case_labels, Make.find_case_labels

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.find_case_labels, Make.find_case_labels -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:88:1`

### #573 DUPLICATE_CODE_DRY on `C_decentralized_dispatcher_service.v`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:93:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.v, Make.v

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.v, Make.v -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:93:1`

### #574 DUPLICATE_CODE_DRY on `C_decentralized_dispatcher_service.sorted_cases`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:107:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.sorted_cases, Make.sorted_cases

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.sorted_cases, Make.sorted_cases -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:107:1`

### #575 DUPLICATE_CODE_DRY on `C_decentralized_dispatcher_service.transform_function`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:117:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.transform_function, C_relational_morph_service.transform_function

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_decentralized_dispatcher_service.transform_function, C_relational_morph_service.transform_function -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:117:1`

### #576 DUPLICATE_CODE_DRY on `C_decentralized_dispatcher_service.funcs`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:125:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 3 location(s): C_decentralized_dispatcher_service.funcs, C_relational_morph_service.funcs, C_irreducible_loop_service.funcs

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 3 location(s): C_decentralized_dispatcher_service.funcs, C_relational_morph_service.funcs, C_irreducible_loop_service.funcs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_decentralized_dispatcher_service.ml:125:1`

### #577 DUPLICATE_CODE_DRY on `C_vpc_path_invalidation_service.sum_exp`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vpc_path_invalidation_service.ml:21:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_vpc_path_invalidation_service.sum_exp, Make.sum_exp

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_vpc_path_invalidation_service.sum_exp, Make.sum_exp -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vpc_path_invalidation_service.ml:21:1`

### #578 DUPLICATE_CODE_DRY on `C_vpc_path_invalidation_service.acc_v`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vpc_path_invalidation_service.ml:45:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_vpc_path_invalidation_service.acc_v, Make.acc_v

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_vpc_path_invalidation_service.acc_v, Make.acc_v -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vpc_path_invalidation_service.ml:45:1`

### #579 DUPLICATE_CODE_DRY on `C_vpc_path_invalidation_service.init_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vpc_path_invalidation_service.ml:47:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_vpc_path_invalidation_service.init_stmt, Make.init_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_vpc_path_invalidation_service.init_stmt, Make.init_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vpc_path_invalidation_service.ml:47:1`

### #580 DUPLICATE_CODE_DRY on `C_vpc_path_invalidation_service.multiplier`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vpc_path_invalidation_service.ml:62:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_vpc_path_invalidation_service.multiplier, Make.multiplier

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_vpc_path_invalidation_service.multiplier, Make.multiplier -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vpc_path_invalidation_service.ml:62:1`

### #581 DUPLICATE_CODE_DRY on `C_vpc_path_invalidation_service.magic_prime`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vpc_path_invalidation_service.ml:63:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_vpc_path_invalidation_service.magic_prime, Make.magic_prime

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_vpc_path_invalidation_service.magic_prime, Make.magic_prime -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/hardening/c_vpc_path_invalidation_service.ml:63:1`

### #582 DUPLICATE_CODE_DRY on `C_visa_spec_service.already_injected`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:14:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.already_injected, Make.already_injected

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.already_injected, Make.already_injected -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:14:1`

### #583 DUPLICATE_CODE_DRY on `C_visa_spec_service.flag_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:22:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.flag_var, Make.flag_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.flag_var, Make.flag_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:22:1`

### #584 DUPLICATE_CODE_DRY on `C_visa_spec_service.should_transform`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:27:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.should_transform, Make.should_transform

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.should_transform, Make.should_transform -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:27:1`

### #585 DUPLICATE_CODE_DRY on `C_visa_spec_service.get_in_reg`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:40:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.get_in_reg, Make.get_in_reg

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.get_in_reg, Make.get_in_reg -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:40:1`

### #586 DUPLICATE_CODE_DRY on `C_visa_spec_service.max_in_reg`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:44:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.max_in_reg, Make.max_in_reg

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.max_in_reg, Make.max_in_reg -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:44:1`

### #587 DUPLICATE_CODE_DRY on `C_visa_spec_service.next_vreg`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:47:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.next_vreg, Make.next_vreg

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.next_vreg, Make.next_vreg -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:47:1`

### #588 DUPLICATE_CODE_DRY on `C_visa_spec_service.get_vreg`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:55:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.get_vreg, Make.get_vreg

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.get_vreg, Make.get_vreg -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:55:1`

### #589 DUPLICATE_CODE_DRY on `C_visa_spec_service.r`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:58:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.r, Make.r

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.r, Make.r -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:58:1`

### #590 DUPLICATE_CODE_DRY on `C_visa_spec_service.primes`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:69:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.primes, Make.primes

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.primes, Make.primes -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:69:1`

### #591 DUPLICATE_CODE_DRY on `C_visa_spec_service.coprime_primes`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:70:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.coprime_primes, Make.coprime_primes

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.coprime_primes, Make.coprime_primes -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:70:1`

### #592 DUPLICATE_CODE_DRY on `C_visa_spec_service.idx`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:76:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.idx, Make.idx

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.idx, Make.idx -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:76:1`

### #593 DUPLICATE_CODE_DRY on `C_visa_spec_service.affine_s`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:79:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.affine_s, Make.affine_s

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.affine_s, Make.affine_s -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:79:1`

### #594 DUPLICATE_CODE_DRY on `C_visa_spec_service.slot`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:88:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.slot, Make.slot

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.slot, Make.slot -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:88:1`

### #595 DUPLICATE_CODE_DRY on `C_visa_spec_service.type_to_str`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:93:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.type_to_str, Make.type_to_str

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.type_to_str, Make.type_to_str -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:93:1`

### #596 DUPLICATE_CODE_DRY on `C_visa_spec_service.virtualize_function`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:107:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.virtualize_function, Make.virtualize_function

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.virtualize_function, Make.virtualize_function -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:107:1`

### #597 DUPLICATE_CODE_DRY on `C_visa_spec_service.isa_annotation`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:114:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.isa_annotation, Make.isa_annotation

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.isa_annotation, Make.isa_annotation -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:114:1`

### #598 DUPLICATE_CODE_DRY on `C_visa_spec_service.spec`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:121:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.spec, Make.spec

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.spec, Make.spec -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:121:1`

### #599 DUPLICATE_CODE_DRY on `C_visa_spec_service.vbc_name`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:129:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.vbc_name, Make.vbc_name

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.vbc_name, Make.vbc_name -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:129:1`

### #600 DUPLICATE_CODE_DRY on `C_visa_spec_service.ptr_formals`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:130:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.ptr_formals, Make.ptr_formals

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.ptr_formals, Make.ptr_formals -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:130:1`

### #601 DUPLICATE_CODE_DRY on `C_visa_spec_service.has_ptr_param`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:131:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.has_ptr_param, Make.has_ptr_param

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.has_ptr_param, Make.has_ptr_param -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:131:1`

### #602 DUPLICATE_CODE_DRY on `C_visa_spec_service.n_words`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:137:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.n_words, Make.n_words

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.n_words, Make.n_words -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:137:1`

### #603 DUPLICATE_CODE_DRY on `C_visa_spec_service.array_type`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:144:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.array_type, Make.array_type

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.array_type, Make.array_type -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:144:1`

### #604 DUPLICATE_CODE_DRY on `C_visa_spec_service.vbc_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:145:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.vbc_var, Make.vbc_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.vbc_var, Make.vbc_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:145:1`

### #605 DUPLICATE_CODE_DRY on `C_visa_spec_service.u64`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:150:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.u64, Make.u64

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.u64, Make.u64 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:150:1`

### #606 DUPLICATE_CODE_DRY on `C_visa_spec_service.ptr_arg`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:159:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.ptr_arg, Make.ptr_arg

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.ptr_arg, Make.ptr_arg -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:159:1`

### #607 DUPLICATE_CODE_DRY on `C_visa_spec_service.ret_type_str`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:162:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.ret_type_str, Make.ret_type_str

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.ret_type_str, Make.ret_type_str -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:162:1`

### #608 DUPLICATE_CODE_DRY on `C_visa_spec_service.reg_mask_base`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:165:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.reg_mask_base, Make.reg_mask_base

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.reg_mask_base, Make.reg_mask_base -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:165:1`

### #609 DUPLICATE_CODE_DRY on `C_visa_spec_service.reg_mask_step`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:168:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.reg_mask_step, Make.reg_mask_step

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.reg_mask_step, Make.reg_mask_step -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:168:1`

### #610 DUPLICATE_CODE_DRY on `C_visa_spec_service.target_reg`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:175:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.target_reg, Make.target_reg

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.target_reg, Make.target_reg -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:175:1`

### #611 DUPLICATE_CODE_DRY on `C_visa_spec_service.fn_params`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:185:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.fn_params, Make.fn_params

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.fn_params, Make.fn_params -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:185:1`

### #612 DUPLICATE_CODE_DRY on `C_visa_spec_service.fn_body_impl`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:191:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.fn_body_impl, Make.fn_body_impl

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.fn_body_impl, Make.fn_body_impl -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:191:1`

### #613 DUPLICATE_CODE_DRY on `C_visa_spec_service.new_globals`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:199:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.new_globals, Make.new_globals

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_spec_service.new_globals, Make.new_globals -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_spec_service.ml:199:1`

### #614 DUPLICATE_CODE_DRY on `C_visa_stmt_compiler.extract_ptr_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_stmt_compiler.ml:87:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_stmt_compiler.extract_ptr_var, C_visa_expr_compiler.extract_ptr_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_stmt_compiler.extract_ptr_var, C_visa_expr_compiler.extract_ptr_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_stmt_compiler.ml:87:1`

### #615 DUPLICATE_CODE_DRY on `C_virtualize_service.virtualize_function`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:19:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.virtualize_function, Make.virtualize_function

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.virtualize_function, Make.virtualize_function -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:19:1`

### #616 DUPLICATE_CODE_DRY on `C_virtualize_service.bc_name`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:23:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.bc_name, Make.bc_name

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.bc_name, Make.bc_name -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:23:1`

### #617 DUPLICATE_CODE_DRY on `C_virtualize_service.raw_bytes`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:27:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.raw_bytes, Make.raw_bytes

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.raw_bytes, Make.raw_bytes -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:27:1`

### #618 DUPLICATE_CODE_DRY on `C_virtualize_service.init_val`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:70:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.init_val, Make.init_val

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.init_val, Make.init_val -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:70:1`

### #619 DUPLICATE_CODE_DRY on `C_virtualize_service.init_info`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:74:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.init_info, Make.init_info

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.init_info, Make.init_info -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:74:1`

### #620 DUPLICATE_CODE_DRY on `C_virtualize_service.regs_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:78:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.regs_var, Make.regs_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.regs_var, Make.regs_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:78:1`

### #621 DUPLICATE_CODE_DRY on `C_virtualize_service.stack_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:79:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.stack_var, Make.stack_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.stack_var, Make.stack_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:79:1`

### #622 DUPLICATE_CODE_DRY on `C_virtualize_service.init_sp`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:86:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.init_sp, Make.init_sp

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.init_sp, Make.init_sp -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:86:1`

### #623 DUPLICATE_CODE_DRY on `C_virtualize_service.init_running`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:88:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.init_running, Make.init_running

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.init_running, Make.init_running -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:88:1`

### #624 DUPLICATE_CODE_DRY on `C_virtualize_service.fetch_op`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:91:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.fetch_op, Make.fetch_op

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.fetch_op, Make.fetch_op -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:91:1`

### #625 DUPLICATE_CODE_DRY on `C_virtualize_service.arg_val`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:100:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.arg_val, Make.arg_val

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.arg_val, Make.arg_val -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:100:1`

### #626 DUPLICATE_CODE_DRY on `C_virtualize_service.push`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:142:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.push, Make.push

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.push, Make.push -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:142:1`

### #627 DUPLICATE_CODE_DRY on `C_virtualize_service.inc_sp`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:172:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.inc_sp, Make.inc_sp

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.inc_sp, Make.inc_sp -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:172:1`

### #628 DUPLICATE_CODE_DRY on `C_virtualize_service.blk`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:184:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.blk, Make.blk

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.blk, Make.blk -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:184:1`

### #629 DUPLICATE_CODE_DRY on `C_virtualize_service.st`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:185:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.st, Make.st

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.st, Make.st -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:185:1`

### #630 DUPLICATE_CODE_DRY on `C_virtualize_service.dec_sp`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:180:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 6 location(s): C_virtualize_service.dec_sp, C_virtualize_service.dec_sp1, C_virtualize_service.dec_sp2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 6 location(s): C_virtualize_service.dec_sp, C_virtualize_service.dec_sp1, C_virtualize_service.dec_sp2 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:180:1`

### #631 DUPLICATE_CODE_DRY on `C_virtualize_service.popped_val`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:119:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 8 location(s): C_virtualize_service.popped_val, C_virtualize_service.val_b, C_virtualize_service.val_a

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 8 location(s): C_virtualize_service.popped_val, C_virtualize_service.val_b, C_virtualize_service.val_a -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:119:1`

### #632 DUPLICATE_CODE_DRY on `C_virtualize_service.store`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:120:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.store, Make.store

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.store, Make.store -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:120:1`

### #633 DUPLICATE_CODE_DRY on `C_virtualize_service.inc_pc_const`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:144:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.inc_pc_const, Make.inc_pc_const

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.inc_pc_const, Make.inc_pc_const -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:144:1`

### #634 DUPLICATE_CODE_DRY on `C_virtualize_service.push_sum`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:157:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.push_sum, Make.push_sum

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.push_sum, Make.push_sum -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:157:1`

### #635 DUPLICATE_CODE_DRY on `C_virtualize_service.push_xor`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:171:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.push_xor, Make.push_xor

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.push_xor, Make.push_xor -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:171:1`

### #636 DUPLICATE_CODE_DRY on `C_virtualize_service.save_res`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:182:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.save_res, Make.save_res

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.save_res, Make.save_res -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:182:1`

### #637 DUPLICATE_CODE_DRY on `C_virtualize_service.stop_running`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:183:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.stop_running, Make.stop_running

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.stop_running, Make.stop_running -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:183:1`

### #638 DUPLICATE_CODE_DRY on `C_virtualize_service.switch_body`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:190:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.switch_body, Make.switch_body

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.switch_body, Make.switch_body -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:190:1`

### #639 DUPLICATE_CODE_DRY on `C_virtualize_service.switch_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:193:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.switch_stmt, Make.switch_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.switch_stmt, Make.switch_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:193:1`

### #640 DUPLICATE_CODE_DRY on `C_virtualize_service.while_loop`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:196:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.while_loop, Make.while_loop

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.while_loop, Make.while_loop -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:196:1`

### #641 DUPLICATE_CODE_DRY on `C_virtualize_service.ret_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:201:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.ret_stmt, Make.ret_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_virtualize_service.ret_stmt, Make.ret_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_virtualize_service.ml:201:1`

### #642 DUPLICATE_CODE_DRY on `C_visa_expr_compiler.f3`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_expr_compiler.ml:20:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_expr_compiler.f3, Make.f3

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_expr_compiler.f3, Make.f3 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_expr_compiler.ml:20:1`

### #643 DUPLICATE_CODE_DRY on `C_visa_expr_compiler.v32`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_expr_compiler.ml:27:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_expr_compiler.v32, Make.v32

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_visa_expr_compiler.v32, Make.v32 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/compiler/c_visa_expr_compiler.ml:27:1`

### #644 DUPLICATE_CODE_DRY on `C_bogus_calls_service.other_funcs`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_bogus_calls_service.ml:11:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_bogus_calls_service.other_funcs, Make.other_funcs

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_bogus_calls_service.other_funcs, Make.other_funcs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_bogus_calls_service.ml:11:1`

### #645 DUPLICATE_CODE_DRY on `C_bogus_calls_service.dummy_args`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_bogus_calls_service.ml:14:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_bogus_calls_service.dummy_args, Make.dummy_args

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_bogus_calls_service.dummy_args, Make.dummy_args -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_bogus_calls_service.ml:14:1`

### #646 DUPLICATE_CODE_DRY on `C_bogus_calls_service.bogus_call`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_bogus_calls_service.ml:21:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_bogus_calls_service.bogus_call, Make.bogus_call

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_bogus_calls_service.bogus_call, Make.bogus_call -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_bogus_calls_service.ml:21:1`

### #647 DUPLICATE_CODE_DRY on `C_bogus_calls_service.init_x`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_bogus_calls_service.ml:25:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_bogus_calls_service.init_x, Make.init_x

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_bogus_calls_service.init_x, Make.init_x -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/inter_procedural/c_bogus_calls_service.ml:25:1`

### #648 DUPLICATE_CODE_DRY on `C_struct_permute_service.permute_and_pad_struct`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_struct_permute_service.ml:7:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_struct_permute_service.permute_and_pad_struct, Make.permute_and_pad_struct

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_struct_permute_service.permute_and_pad_struct, Make.permute_and_pad_struct -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_struct_permute_service.ml:7:1`

### #649 DUPLICATE_CODE_DRY on `C_struct_permute_service.pad_field`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_struct_permute_service.ml:11:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_struct_permute_service.pad_field, Make.pad_field

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_struct_permute_service.pad_field, Make.pad_field -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_struct_permute_service.ml:11:1`

### #650 DUPLICATE_CODE_DRY on `C_struct_permute_service.padded_fields`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_struct_permute_service.ml:22:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_struct_permute_service.padded_fields, Make.padded_fields

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_struct_permute_service.padded_fields, Make.padded_fields -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_struct_permute_service.ml:22:1`

### #651 DUPLICATE_CODE_DRY on `C_bpm_mba_service.stages`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_bpm_mba_service.ml:12:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_bpm_mba_service.stages, Make.stages

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_bpm_mba_service.stages, Make.stages -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_bpm_mba_service.ml:12:1`

### #652 DUPLICATE_CODE_DRY on `C_bpm_mba_service.u32_const`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_bpm_mba_service.ml:20:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_bpm_mba_service.u32_const, Make.u32_const

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_bpm_mba_service.u32_const, Make.u32_const -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_bpm_mba_service.ml:20:1`

### #653 DUPLICATE_CODE_DRY on `C_bpm_mba_service.idx`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_bpm_mba_service.ml:44:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_bpm_mba_service.idx, Make.idx

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_bpm_mba_service.idx, Make.idx -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_bpm_mba_service.ml:44:1`

### #654 DUPLICATE_CODE_DRY on `C_bpm_mba_service.apply_perm`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_bpm_mba_service.ml:50:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_bpm_mba_service.apply_perm, Make.apply_perm

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_bpm_mba_service.apply_perm, Make.apply_perm -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_bpm_mba_service.ml:50:1`

### #655 DUPLICATE_CODE_DRY on `C_bpm_mba_service.apply_inv_perm`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_bpm_mba_service.ml:54:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_bpm_mba_service.apply_inv_perm, Make.apply_inv_perm

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_bpm_mba_service.apply_inv_perm, Make.apply_inv_perm -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_bpm_mba_service.ml:54:1`

### #656 DUPLICATE_CODE_DRY on `C_mba_service.and_part`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:96:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_mba_service.and_part, Make.and_part

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_mba_service.and_part, Make.and_part -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:96:1`

### #657 DUPLICATE_CODE_DRY on `C_mba_service.shift_part`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:62:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_mba_service.shift_part, Make.shift_part

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_mba_service.shift_part, Make.shift_part -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:62:1`

### #658 DUPLICATE_CODE_DRY on `C_mba_service.and_p`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:28:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_mba_service.and_p, Make.and_p

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_mba_service.and_p, Make.and_p -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:28:1`

### #659 DUPLICATE_CODE_DRY on `C_mba_service.carry2`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:36:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_mba_service.carry2, Make.carry2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_mba_service.carry2, Make.carry2 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:36:1`

### #660 DUPLICATE_CODE_DRY on `C_mba_service.andxy`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:48:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_mba_service.andxy, Make.andxy

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_mba_service.andxy, Make.andxy -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:48:1`

### #661 DUPLICATE_CODE_DRY on `C_mba_service.right_part`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:103:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_mba_service.right_part, Make.right_part

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_mba_service.right_part, Make.right_part -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:103:1`

### #662 DUPLICATE_CODE_DRY on `C_mba_service.two_nxandy`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:84:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_mba_service.two_nxandy, Make.two_nxandy

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_mba_service.two_nxandy, Make.two_nxandy -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:84:1`

### #663 DUPLICATE_CODE_DRY on `C_mba_service.and2`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:113:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_mba_service.and2, Make.and2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_mba_service.and2, Make.and2 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_mba_service.ml:113:1`

### #664 DUPLICATE_CODE_DRY on `C_float_mba_service.scale_factor`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_float_mba_service.ml:10:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_float_mba_service.scale_factor, Make.scale_factor

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_float_mba_service.scale_factor, Make.scale_factor -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_float_mba_service.ml:10:1`

### #665 DUPLICATE_CODE_DRY on `C_encode_literals_service.total_len`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:18:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.total_len, Make.total_len

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.total_len, Make.total_len -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:18:1`

### #666 DUPLICATE_CODE_DRY on `C_encode_literals_service.enc_bytes`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:23:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.enc_bytes, Make.enc_bytes

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.enc_bytes, Make.enc_bytes -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:23:1`

### #667 DUPLICATE_CODE_DRY on `C_encode_literals_service.enc_init_list`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:39:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.enc_init_list, Make.enc_init_list

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.enc_init_list, Make.enc_init_list -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:39:1`

### #668 DUPLICATE_CODE_DRY on `C_encode_literals_service.enc_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:42:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.enc_var, Make.enc_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.enc_var, Make.enc_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:42:1`

### #669 DUPLICATE_CODE_DRY on `C_encode_literals_service.dec_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:47:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.dec_var, Make.dec_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.dec_var, Make.dec_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:47:1`

### #670 DUPLICATE_CODE_DRY on `C_encode_literals_service.init_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:52:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.init_var, Make.init_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.init_var, Make.init_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:52:1`

### #671 DUPLICATE_CODE_DRY on `C_encode_literals_service.dec_ptr`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:65:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.dec_ptr, Make.dec_ptr

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.dec_ptr, Make.dec_ptr -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:65:1`

### #672 DUPLICATE_CODE_DRY on `C_encode_literals_service.enc_v`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:83:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.enc_v, Make.enc_v

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.enc_v, Make.enc_v -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:83:1`

### #673 DUPLICATE_CODE_DRY on `C_encode_literals_service.dec_v`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:88:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.dec_v, Make.dec_v

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.dec_v, Make.dec_v -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:88:1`

### #674 DUPLICATE_CODE_DRY on `C_encode_literals_service.init_v`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:93:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.init_v, Make.init_v

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.init_v, Make.init_v -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:93:1`

### #675 DUPLICATE_CODE_DRY on `C_encode_literals_service.idx_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:107:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.idx_var, Make.idx_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.idx_var, Make.idx_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:107:1`

### #676 DUPLICATE_CODE_DRY on `C_encode_literals_service.assign_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:113:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.assign_stmt, Make.assign_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.assign_stmt, Make.assign_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:113:1`

### #677 DUPLICATE_CODE_DRY on `C_encode_literals_service.incr_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:114:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.incr_stmt, Make.incr_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.incr_stmt, Make.incr_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:114:1`

### #678 DUPLICATE_CODE_DRY on `C_encode_literals_service.cond_exp`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:119:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.cond_exp, Make.cond_exp

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.cond_exp, Make.cond_exp -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:119:1`

### #679 DUPLICATE_CODE_DRY on `C_encode_literals_service.if_loop`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:121:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.if_loop, Make.if_loop

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.if_loop, Make.if_loop -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:121:1`

### #680 DUPLICATE_CODE_DRY on `C_encode_literals_service.loop_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:124:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.loop_stmt, Make.loop_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.loop_stmt, Make.loop_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:124:1`

### #681 DUPLICATE_CODE_DRY on `C_encode_literals_service.init_idx`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:126:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.init_idx, Make.init_idx

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.init_idx, Make.init_idx -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:126:1`

### #682 DUPLICATE_CODE_DRY on `C_encode_literals_service.set_init_done`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:127:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.set_init_done, Make.set_init_done

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_literals_service.set_init_done, Make.set_init_done -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_literals_service.ml:127:1`

### #683 DUPLICATE_CODE_DRY on `C_homomorphic_service.next_x`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_homomorphic_service.ml:11:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 6 location(s): C_homomorphic_service.next_x, C_polynomial_mba_service.next_x, C_loki_invariant_service.next_x

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 6 location(s): C_homomorphic_service.next_x, C_polynomial_mba_service.next_x, C_loki_invariant_service.next_x -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_homomorphic_service.ml:11:1`

### #684 DUPLICATE_CODE_DRY on `C_homomorphic_service.u64`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_homomorphic_service.ml:17:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_homomorphic_service.u64, Make.u64

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_homomorphic_service.u64, Make.u64 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_homomorphic_service.ml:17:1`

### #685 DUPLICATE_CODE_DRY on `C_homomorphic_service.e1_h`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_homomorphic_service.ml:36:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_homomorphic_service.e1_h, Make.e1_h

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_homomorphic_service.e1_h, Make.e1_h -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_homomorphic_service.ml:36:1`

### #686 DUPLICATE_CODE_DRY on `C_homomorphic_service.e2_h`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_homomorphic_service.ml:37:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_homomorphic_service.e2_h, Make.e2_h

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_homomorphic_service.e2_h, Make.e2_h -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_homomorphic_service.ml:37:1`

### #687 DUPLICATE_CODE_DRY on `C_homomorphic_service.sum_h`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_homomorphic_service.ml:40:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_homomorphic_service.sum_h, Make.sum_h

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_homomorphic_service.sum_h, Make.sum_h -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_homomorphic_service.ml:40:1`

### #688 DUPLICATE_CODE_DRY on `C_encode_data_service.is_splittable`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_data_service.ml:5:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_data_service.is_splittable, Make.is_splittable

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_data_service.is_splittable, Make.is_splittable -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_data_service.ml:5:1`

### #689 DUPLICATE_CODE_DRY on `C_encode_data_service.sum_exp`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_data_service.ml:20:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_data_service.sum_exp, Make.sum_exp

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_data_service.sum_exp, Make.sum_exp -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_data_service.ml:20:1`

### #690 DUPLICATE_CODE_DRY on `C_encode_data_service.temp_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_data_service.ml:30:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_data_service.temp_var, Make.temp_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_data_service.temp_var, Make.temp_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_data_service.ml:30:1`

### #691 DUPLICATE_CODE_DRY on `C_encode_data_service.shift_exp`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_data_service.ml:32:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_data_service.shift_exp, Make.shift_exp

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_data_service.shift_exp, Make.shift_exp -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_data_service.ml:32:1`

### #692 DUPLICATE_CODE_DRY on `C_encode_data_service.diff_exp`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_data_service.ml:33:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_data_service.diff_exp, Make.diff_exp

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_encode_data_service.diff_exp, Make.diff_exp -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_encode_data_service.ml:33:1`

### #693 DUPLICATE_CODE_DRY on `C_egraph_mba_service.create_egraph`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:22:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.create_egraph, Make.create_egraph

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.create_egraph, Make.create_egraph -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:22:1`

### #694 DUPLICATE_CODE_DRY on `C_egraph_mba_service.canon_node`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:41:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.canon_node, Make.canon_node

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.canon_node, Make.canon_node -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:41:1`

### #695 DUPLICATE_CODE_DRY on `C_egraph_mba_service.nodes2`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:66:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.nodes2, Make.nodes2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.nodes2, Make.nodes2 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:66:1`

### #696 DUPLICATE_CODE_DRY on `C_egraph_mba_service.insert_exp`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:72:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.insert_exp, Make.insert_exp

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.insert_exp, Make.insert_exp -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:72:1`

### #697 DUPLICATE_CODE_DRY on `C_egraph_mba_service.c1`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:86:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.c1, Make.c1

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.c1, Make.c1 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:86:1`

### #698 DUPLICATE_CODE_DRY on `C_egraph_mba_service.c2`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:80:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.c2, Make.c2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.c2, Make.c2 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:80:1`

### #699 DUPLICATE_CODE_DRY on `C_egraph_mba_service.apply_rules_on_node`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:92:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.apply_rules_on_node, Make.apply_rules_on_node

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.apply_rules_on_node, Make.apply_rules_on_node -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:92:1`

### #700 DUPLICATE_CODE_DRY on `C_egraph_mba_service.sum1_c`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:101:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.sum1_c, Make.sum1_c

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.sum1_c, Make.sum1_c -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:101:1`

### #701 DUPLICATE_CODE_DRY on `C_egraph_mba_service.sum2_c`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:106:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.sum2_c, Make.sum2_c

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.sum2_c, Make.sum2_c -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:106:1`

### #702 DUPLICATE_CODE_DRY on `C_egraph_mba_service.sub2`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:113:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.sub2, Make.sub2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.sub2, Make.sub2 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:113:1`

### #703 DUPLICATE_CODE_DRY on `C_egraph_mba_service.sum3_c`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:117:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.sum3_c, Make.sum3_c

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.sum3_c, Make.sum3_c -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:117:1`

### #704 DUPLICATE_CODE_DRY on `C_egraph_mba_service.diff1_c`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:128:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.diff1_c, Make.diff1_c

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.diff1_c, Make.diff1_c -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:128:1`

### #705 DUPLICATE_CODE_DRY on `C_egraph_mba_service.diff2_c`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:134:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.diff2_c, Make.diff2_c

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.diff2_c, Make.diff2_c -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:134:1`

### #706 DUPLICATE_CODE_DRY on `C_egraph_mba_service.diff3_c`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:140:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.diff3_c, Make.diff3_c

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.diff3_c, Make.diff3_c -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:140:1`

### #707 DUPLICATE_CODE_DRY on `C_egraph_mba_service.xor1_c`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:148:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.xor1_c, Make.xor1_c

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.xor1_c, Make.xor1_c -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:148:1`

### #708 DUPLICATE_CODE_DRY on `C_egraph_mba_service.xor2_c`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:156:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.xor2_c, Make.xor2_c

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.xor2_c, Make.xor2_c -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:156:1`

### #709 DUPLICATE_CODE_DRY on `C_egraph_mba_service.xor3_c`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:160:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.xor3_c, Make.xor3_c

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.xor3_c, Make.xor3_c -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:160:1`

### #710 DUPLICATE_CODE_DRY on `C_egraph_mba_service.and1_c`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:168:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.and1_c, Make.and1_c

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.and1_c, Make.and1_c -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:168:1`

### #711 DUPLICATE_CODE_DRY on `C_egraph_mba_service.and2_c`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:173:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.and2_c, Make.and2_c

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.and2_c, Make.and2_c -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:173:1`

### #712 DUPLICATE_CODE_DRY on `C_egraph_mba_service.or1_c`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:181:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.or1_c, Make.or1_c

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.or1_c, Make.or1_c -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:181:1`

### #713 DUPLICATE_CODE_DRY on `C_egraph_mba_service.or2_c`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:186:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.or2_c, Make.or2_c

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.or2_c, Make.or2_c -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:186:1`

### #714 DUPLICATE_CODE_DRY on `C_egraph_mba_service.expand_egraph`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:192:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.expand_egraph, Make.expand_egraph

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.expand_egraph, Make.expand_egraph -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:192:1`

### #715 DUPLICATE_CODE_DRY on `C_egraph_mba_service.all_classes`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:195:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.all_classes, Make.all_classes

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.all_classes, Make.all_classes -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:195:1`

### #716 DUPLICATE_CODE_DRY on `C_egraph_mba_service.score_node`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:206:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.score_node, Make.score_node

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.score_node, Make.score_node -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:206:1`

### #717 DUPLICATE_CODE_DRY on `C_egraph_mba_service.op_weight`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:213:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.op_weight, Make.op_weight

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.op_weight, Make.op_weight -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:213:1`

### #718 DUPLICATE_CODE_DRY on `C_egraph_mba_service.r`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:238:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.r, Make.r

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.r, Make.r -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:238:1`

### #719 DUPLICATE_CODE_DRY on `C_egraph_mba_service.nodes`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:242:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.nodes, Make.nodes

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.nodes, Make.nodes -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:242:1`

### #720 DUPLICATE_CODE_DRY on `C_egraph_mba_service.best`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:232:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.best, Make.best

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.best, Make.best -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:232:1`

### #721 DUPLICATE_CODE_DRY on `C_egraph_mba_service.pick_node`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:246:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.pick_node, Make.pick_node

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.pick_node, Make.pick_node -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:246:1`

### #722 DUPLICATE_CODE_DRY on `C_egraph_mba_service.scored`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:251:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.scored, Make.scored

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.scored, Make.scored -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:251:1`

### #723 DUPLICATE_CODE_DRY on `C_egraph_mba_service.res_exp`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:258:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.res_exp, Make.res_exp

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.res_exp, Make.res_exp -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:258:1`

### #724 DUPLICATE_CODE_DRY on `C_egraph_mba_service.e_sub`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:266:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.e_sub, Make.e_sub

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.e_sub, Make.e_sub -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:266:1`

### #725 DUPLICATE_CODE_DRY on `C_egraph_mba_service.e2`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:270:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.e2, Make.e2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.e2, Make.e2 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:270:1`

### #726 DUPLICATE_CODE_DRY on `C_egraph_mba_service.root_id`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:281:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.root_id, Make.root_id

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_egraph_mba_service.root_id, Make.root_id -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_egraph_mba_service.ml:281:1`

### #727 DUPLICATE_CODE_DRY on `C_lut_arithmetic_service.name`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_lut_arithmetic_service.ml:9:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_lut_arithmetic_service.name, Make.name

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_lut_arithmetic_service.name, Make.name -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_lut_arithmetic_service.ml:9:1`

### #728 DUPLICATE_CODE_DRY on `C_lut_arithmetic_service.init_val`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_lut_arithmetic_service.ml:19:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_lut_arithmetic_service.init_val, Make.init_val

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_lut_arithmetic_service.init_val, Make.init_val -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_lut_arithmetic_service.ml:19:1`

### #729 DUPLICATE_CODE_DRY on `C_lut_arithmetic_service.init_info`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_lut_arithmetic_service.ml:22:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_lut_arithmetic_service.init_info, Make.init_info

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_lut_arithmetic_service.init_info, Make.init_info -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_lut_arithmetic_service.ml:22:1`

### #730 DUPLICATE_CODE_DRY on `C_polynomial_mba_service.u64`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_polynomial_mba_service.ml:17:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_polynomial_mba_service.u64, Make.u64

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_polynomial_mba_service.u64, Make.u64 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_polynomial_mba_service.ml:17:1`

### #731 DUPLICATE_CODE_DRY on `C_polynomial_mba_service.recovered`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_polynomial_mba_service.ml:41:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_polynomial_mba_service.recovered, Make.recovered

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_polynomial_mba_service.recovered, Make.recovered -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_polynomial_mba_service.ml:41:1`

### #732 DUPLICATE_CODE_DRY on `C_polynomial_mba_service.sum_part`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_polynomial_mba_service.ml:53:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_polynomial_mba_service.sum_part, Make.sum_part

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_polynomial_mba_service.sum_part, Make.sum_part -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_polynomial_mba_service.ml:53:1`

### #733 DUPLICATE_CODE_DRY on `C_polynomial_mba_service.res`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_polynomial_mba_service.ml:102:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_polynomial_mba_service.res, Make.res

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_polynomial_mba_service.res, Make.res -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_polynomial_mba_service.ml:102:1`

### #734 DUPLICATE_CODE_DRY on `C_polynomial_mba_service.sub_part`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_polynomial_mba_service.ml:73:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_polynomial_mba_service.sub_part, Make.sub_part

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_polynomial_mba_service.sub_part, Make.sub_part -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_polynomial_mba_service.ml:73:1`

### #735 DUPLICATE_CODE_DRY on `C_loki_invariant_service.p_all`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_loki_invariant_service.ml:43:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_loki_invariant_service.p_all, Make.p_all

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_loki_invariant_service.p_all, Make.p_all -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_loki_invariant_service.ml:43:1`

### #736 DUPLICATE_CODE_DRY on `C_loki_invariant_service.diff2`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_loki_invariant_service.ml:52:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_loki_invariant_service.diff2, Make.diff2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_loki_invariant_service.diff2, Make.diff2 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_loki_invariant_service.ml:52:1`

### #737 DUPLICATE_CODE_DRY on `C_loki_invariant_service.diff`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_loki_invariant_service.ml:74:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_loki_invariant_service.diff, Make.diff

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_loki_invariant_service.diff, Make.diff -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_loki_invariant_service.ml:74:1`

### #738 DUPLICATE_CODE_DRY on `C_loki_invariant_service.v1`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_loki_invariant_service.ml:100:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 4 location(s): C_loki_invariant_service.v1, C_loki_invariant_service.v2, Make.v1

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 4 location(s): C_loki_invariant_service.v1, C_loki_invariant_service.v2, Make.v1 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/data_encoding/c_loki_invariant_service.ml:100:1`

### #739 DUPLICATE_CODE_DRY on `C_annotation_service.s`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/annotations/c_annotation_service.ml:6:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_annotation_service.s, AnnotationHelper.s

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_annotation_service.s, AnnotationHelper.s -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/annotations/c_annotation_service.ml:6:1`

### #740 DUPLICATE_CODE_DRY on `C_annotation_service.raw_list`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/annotations/c_annotation_service.ml:18:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_annotation_service.raw_list, AnnotationHelper.raw_list

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_annotation_service.raw_list, AnnotationHelper.raw_list -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/annotations/c_annotation_service.ml:18:1`

### #741 DUPLICATE_CODE_DRY on `C_annotation_service.sub_list`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/annotations/c_annotation_service.ml:21:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_annotation_service.sub_list, AnnotationHelper.sub_list

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_annotation_service.sub_list, AnnotationHelper.sub_list -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/annotations/c_annotation_service.ml:21:1`

### #742 DUPLICATE_CODE_DRY on `C_annotation_service.type_attrs`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/annotations/c_annotation_service.ml:27:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_annotation_service.type_attrs, AnnotationHelper.type_attrs

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_annotation_service.type_attrs, AnnotationHelper.type_attrs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/annotations/c_annotation_service.ml:27:1`

### #743 DUPLICATE_CODE_DRY on `C_annotation_service.all_attrs`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/annotations/c_annotation_service.ml:32:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_annotation_service.all_attrs, AnnotationHelper.all_attrs

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_annotation_service.all_attrs, AnnotationHelper.all_attrs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/annotations/c_annotation_service.ml:32:1`

### #744 DUPLICATE_CODE_DRY on `C_annotation_service.raw_annotations`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/annotations/c_annotation_service.ml:41:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_annotation_service.raw_annotations, AnnotationHelper.raw_annotations

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_annotation_service.raw_annotations, AnnotationHelper.raw_annotations -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/annotations/c_annotation_service.ml:41:1`

### #745 DUPLICATE_CODE_DRY on `C_annotation_service.tokens`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/annotations/c_annotation_service.ml:55:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_annotation_service.tokens, AnnotationHelper.tokens

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_annotation_service.tokens, AnnotationHelper.tokens -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/annotations/c_annotation_service.ml:55:1`

### #746 DUPLICATE_CODE_DRY on `C_annotation_service.should_skip_all`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/annotations/c_annotation_service.ml:74:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_annotation_service.should_skip_all, AnnotationHelper.should_skip_all

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_annotation_service.should_skip_all, AnnotationHelper.should_skip_all -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/annotations/c_annotation_service.ml:74:1`

### #747 DUPLICATE_CODE_DRY on `C_ghost_code_service.new_stmts`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_ghost_code_service.ml:9:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 4 location(s): C_ghost_code_service.new_stmts, C_opcode_equalize_service.new_stmts, Make.new_stmts

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 4 location(s): C_ghost_code_service.new_stmts, C_opcode_equalize_service.new_stmts, Make.new_stmts -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_ghost_code_service.ml:9:1`

### #748 DUPLICATE_CODE_DRY on `C_ghost_code_service.k1`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_ghost_code_service.ml:22:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_ghost_code_service.k1, Make.k1

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_ghost_code_service.k1, Make.k1 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_ghost_code_service.ml:22:1`

### #749 DUPLICATE_CODE_DRY on `C_ghost_code_service.k2`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_ghost_code_service.ml:23:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 4 location(s): C_ghost_code_service.k2, C_opcode_equalize_service.k1, Make.k2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 4 location(s): C_ghost_code_service.k2, C_opcode_equalize_service.k1, Make.k2 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_ghost_code_service.ml:23:1`

### #750 DUPLICATE_CODE_DRY on `C_ghost_code_service.op4`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_ghost_code_service.ml:27:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_ghost_code_service.op4, Make.op4

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_ghost_code_service.op4, Make.op4 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_ghost_code_service.ml:27:1`

### #751 DUPLICATE_CODE_DRY on `C_ghost_code_service.k`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_ghost_code_service.ml:36:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_ghost_code_service.k, Make.k

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_ghost_code_service.k, Make.k -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_ghost_code_service.ml:36:1`

### #752 DUPLICATE_CODE_DRY on `C_relational_morph_service.morphed`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_relational_morph_service.ml:66:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_relational_morph_service.morphed, Make.morphed

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_relational_morph_service.morphed, Make.morphed -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_relational_morph_service.ml:66:1`

### #753 DUPLICATE_CODE_DRY on `C_relational_morph_service.not_ge`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_relational_morph_service.ml:36:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_relational_morph_service.not_ge, Make.not_ge

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_relational_morph_service.not_ge, Make.not_ge -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_relational_morph_service.ml:36:1`

### #754 DUPLICATE_CODE_DRY on `C_relational_morph_service.not_le`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_relational_morph_service.ml:48:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_relational_morph_service.not_le, Make.not_le

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_relational_morph_service.not_le, Make.not_le -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_relational_morph_service.ml:48:1`

### #755 DUPLICATE_CODE_DRY on `C_relational_morph_service.safe_div`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_relational_morph_service.ml:75:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_relational_morph_service.safe_div, Make.safe_div

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_relational_morph_service.safe_div, Make.safe_div -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_relational_morph_service.ml:75:1`

### #756 DUPLICATE_CODE_DRY on `C_opcode_equalize_service.k2`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_opcode_equalize_service.ml:19:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_opcode_equalize_service.k2, Make.k2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_opcode_equalize_service.k2, Make.k2 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_opcode_equalize_service.ml:19:1`

### #757 DUPLICATE_CODE_DRY on `C_opcode_equalize_service.op3`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_opcode_equalize_service.ml:24:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_opcode_equalize_service.op3, Make.op3

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_opcode_equalize_service.op3, Make.op3 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_opcode_equalize_service.ml:24:1`

### #758 DUPLICATE_CODE_DRY on `C_instruction_subst_service.minus_one`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_instruction_subst_service.ml:32:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_instruction_subst_service.minus_one, Make.minus_one

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_instruction_subst_service.minus_one, Make.minus_one -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_instruction_subst_service.ml:32:1`

### #759 DUPLICATE_CODE_DRY on `C_instruction_subst_service.two`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_instruction_subst_service.ml:94:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_instruction_subst_service.two, Make.two

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_instruction_subst_service.two, Make.two -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_instruction_subst_service.ml:94:1`

### #760 DUPLICATE_CODE_DRY on `C_live_range_split_service.v_phase2`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_live_range_split_service.ml:14:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_live_range_split_service.v_phase2, Make.v_phase2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_live_range_split_service.v_phase2, Make.v_phase2 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_live_range_split_service.ml:14:1`

### #761 DUPLICATE_CODE_DRY on `C_live_range_split_service.new_stmts`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_live_range_split_service.ml:22:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_live_range_split_service.new_stmts, Make.new_stmts

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_live_range_split_service.new_stmts, Make.new_stmts -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_live_range_split_service.ml:22:1`

### #762 DUPLICATE_CODE_DRY on `C_anti_slicing_entanglement_service.new_stmts`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:25:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_slicing_entanglement_service.new_stmts, Make.new_stmts

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_slicing_entanglement_service.new_stmts, Make.new_stmts -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:25:1`

### #763 DUPLICATE_CODE_DRY on `C_anti_slicing_entanglement_service.new_instrs`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:30:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_slicing_entanglement_service.new_instrs, Make.new_instrs

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_slicing_entanglement_service.new_instrs, Make.new_instrs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:30:1`

### #764 DUPLICATE_CODE_DRY on `C_anti_slicing_entanglement_service.typ`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:36:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_slicing_entanglement_service.typ, Make.typ

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_slicing_entanglement_service.typ, Make.typ -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:36:1`

### #765 DUPLICATE_CODE_DRY on `C_anti_slicing_entanglement_service.phantom_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:40:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_slicing_entanglement_service.phantom_var, Make.phantom_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_slicing_entanglement_service.phantom_var, Make.phantom_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:40:1`

### #766 DUPLICATE_CODE_DRY on `C_anti_slicing_entanglement_service.k`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:48:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 6 location(s): C_anti_slicing_entanglement_service.k, C_anti_slicing_entanglement_service.k1, C_anti_slicing_entanglement_service.k2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 6 location(s): C_anti_slicing_entanglement_service.k, C_anti_slicing_entanglement_service.k1, C_anti_slicing_entanglement_service.k2 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:48:1`

### #767 DUPLICATE_CODE_DRY on `C_anti_slicing_entanglement_service.and_not`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:52:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_slicing_entanglement_service.and_not, Make.and_not

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_slicing_entanglement_service.and_not, Make.and_not -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:52:1`

### #768 DUPLICATE_CODE_DRY on `C_anti_slicing_entanglement_service.op2`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:74:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_slicing_entanglement_service.op2, Make.op2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_slicing_entanglement_service.op2, Make.op2 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:74:1`

### #769 DUPLICATE_CODE_DRY on `C_anti_slicing_entanglement_service.e_undo`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:73:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_slicing_entanglement_service.e_undo, Make.e_undo

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_slicing_entanglement_service.e_undo, Make.e_undo -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_anti_slicing_entanglement_service.ml:73:1`

### #770 DUPLICATE_CODE_DRY on `C_loop_to_recursion_service.helper_count`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_loop_to_recursion_service.ml:12:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_to_recursion_service.helper_count, Make.helper_count

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_to_recursion_service.helper_count, Make.helper_count -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_loop_to_recursion_service.ml:12:1`

### #771 DUPLICATE_CODE_DRY on `C_loop_to_recursion_service.helper_name`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_loop_to_recursion_service.ml:19:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_to_recursion_service.helper_name, Make.helper_name

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_to_recursion_service.helper_name, Make.helper_name -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_loop_to_recursion_service.ml:19:1`

### #772 DUPLICATE_CODE_DRY on `C_loop_to_recursion_service.helper_code`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_loop_to_recursion_service.ml:20:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_to_recursion_service.helper_code, Make.helper_code

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_to_recursion_service.helper_code, Make.helper_code -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/morphing/c_loop_to_recursion_service.ml:20:1`

### #773 DUPLICATE_CODE_DRY on `C_ephemeral_payload_service.should_transform`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:7:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_ephemeral_payload_service.should_transform, Make.should_transform

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_ephemeral_payload_service.should_transform, Make.should_transform -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:7:1`

### #774 DUPLICATE_CODE_DRY on `C_ephemeral_payload_service.helper_code`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:25:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_ephemeral_payload_service.helper_code, Make.helper_code

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_ephemeral_payload_service.helper_code, Make.helper_code -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:25:1`

### #775 DUPLICATE_CODE_DRY on `C_ephemeral_payload_service.payload_name`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:95:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_ephemeral_payload_service.payload_name, Make.payload_name

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_ephemeral_payload_service.payload_name, Make.payload_name -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:95:1`

### #776 DUPLICATE_CODE_DRY on `C_ephemeral_payload_service.arr_type`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:106:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_ephemeral_payload_service.arr_type, Make.arr_type

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_ephemeral_payload_service.arr_type, Make.arr_type -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:106:1`

### #777 DUPLICATE_CODE_DRY on `C_ephemeral_payload_service.init_list`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:107:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_ephemeral_payload_service.init_list, Make.init_list

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_ephemeral_payload_service.init_list, Make.init_list -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:107:1`

### #778 DUPLICATE_CODE_DRY on `C_ephemeral_payload_service.gvar`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:108:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_ephemeral_payload_service.gvar, Make.gvar

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_ephemeral_payload_service.gvar, Make.gvar -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:108:1`

### #779 DUPLICATE_CODE_DRY on `C_ephemeral_payload_service.fn_impl`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:113:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_ephemeral_payload_service.fn_impl, Make.fn_impl

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_ephemeral_payload_service.fn_impl, Make.fn_impl -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_ephemeral_payload_service.ml:113:1`

### #780 DUPLICATE_CODE_DRY on `C_api_hash_resolver_service.byte`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_api_hash_resolver_service.ml:8:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_api_hash_resolver_service.byte, Make.byte

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_api_hash_resolver_service.byte, Make.byte -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_api_hash_resolver_service.ml:8:1`

### #781 DUPLICATE_CODE_DRY on `C_api_hash_resolver_service.mask`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_api_hash_resolver_service.ml:11:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_api_hash_resolver_service.mask, Make.mask

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_api_hash_resolver_service.mask, Make.mask -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_api_hash_resolver_service.ml:11:1`

### #782 DUPLICATE_CODE_DRY on `C_api_hash_resolver_service.resolver_helper`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_api_hash_resolver_service.ml:32:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_api_hash_resolver_service.resolver_helper, Make.resolver_helper

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_api_hash_resolver_service.resolver_helper, Make.resolver_helper -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_api_hash_resolver_service.ml:32:1`

### #783 DUPLICATE_CODE_DRY on `C_api_hash_resolver_service.resolve_fn`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_api_hash_resolver_service.ml:64:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_api_hash_resolver_service.resolve_fn, Make.resolve_fn

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_api_hash_resolver_service.resolve_fn, Make.resolve_fn -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_api_hash_resolver_service.ml:64:1`

### #784 DUPLICATE_CODE_DRY on `C_api_hash_resolver_service.resolved_ptr`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_api_hash_resolver_service.ml:70:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_api_hash_resolver_service.resolved_ptr, Make.resolved_ptr

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_api_hash_resolver_service.resolved_ptr, Make.resolved_ptr -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_api_hash_resolver_service.ml:70:1`

### #785 DUPLICATE_CODE_DRY on `C_api_hash_resolver_service.call_resolve`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_api_hash_resolver_service.ml:76:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_api_hash_resolver_service.call_resolve, Make.call_resolve

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_api_hash_resolver_service.call_resolve, Make.call_resolve -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_api_hash_resolver_service.ml:76:1`

### #786 DUPLICATE_CODE_DRY on `C_api_hash_resolver_service.cast_fn_ptr`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_api_hash_resolver_service.ml:82:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_api_hash_resolver_service.cast_fn_ptr, Make.cast_fn_ptr

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_api_hash_resolver_service.cast_fn_ptr, Make.cast_fn_ptr -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/loader/c_api_hash_resolver_service.ml:82:1`

### #787 DUPLICATE_CODE_DRY on `C_rename_symbols_service.buf`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/symbols/c_rename_symbols_service.ml:11:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_rename_symbols_service.buf, Make.buf

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_rename_symbols_service.buf, Make.buf -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/symbols/c_rename_symbols_service.ml:11:1`

### #788 DUPLICATE_CODE_DRY on `C_threaded_implicit_flow_service.pth_proto`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_threaded_implicit_flow_service.ml:15:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_threaded_implicit_flow_service.pth_proto, Make.pth_proto

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_threaded_implicit_flow_service.pth_proto, Make.pth_proto -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_threaded_implicit_flow_service.ml:15:1`

### #789 DUPLICATE_CODE_DRY on `C_threaded_implicit_flow_service.transform_stmts`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_threaded_implicit_flow_service.ml:39:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 10 location(s): C_threaded_implicit_flow_service.transform_stmts, C_sigfpe_flow_service.transform_stmts, C_sigill_flow_service.transform_stmts

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 10 location(s): C_threaded_implicit_flow_service.transform_stmts, C_sigfpe_flow_service.transform_stmts, C_sigill_flow_service.transform_stmts -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_threaded_implicit_flow_service.ml:39:1`

### #790 DUPLICATE_CODE_DRY on `C_threaded_implicit_flow_service.set_res`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_threaded_implicit_flow_service.ml:47:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_threaded_implicit_flow_service.set_res, Make.set_res

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_threaded_implicit_flow_service.set_res, Make.set_res -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_threaded_implicit_flow_service.ml:47:1`

### #791 DUPLICATE_CODE_DRY on `C_threaded_implicit_flow_service.if_res`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_threaded_implicit_flow_service.ml:50:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_threaded_implicit_flow_service.if_res, Make.if_res

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_threaded_implicit_flow_service.if_res, Make.if_res -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_threaded_implicit_flow_service.ml:50:1`

### #792 DUPLICATE_CODE_DRY on `C_threaded_implicit_flow_service.vis`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_threaded_implicit_flow_service.ml:66:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_threaded_implicit_flow_service.vis, Make.vis

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_threaded_implicit_flow_service.vis, Make.vis -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_threaded_implicit_flow_service.ml:66:1`

### #793 DUPLICATE_CODE_DRY on `C_sigfpe_flow_service.sig_proto`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:15:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigfpe_flow_service.sig_proto, Make.sig_proto

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigfpe_flow_service.sig_proto, Make.sig_proto -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:15:1`

### #794 DUPLICATE_CODE_DRY on `C_sigfpe_flow_service.denom_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:35:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigfpe_flow_service.denom_var, Make.denom_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigfpe_flow_service.denom_var, Make.denom_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:35:1`

### #795 DUPLICATE_CODE_DRY on `C_sigfpe_flow_service.set_denom`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:41:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigfpe_flow_service.set_denom, Make.set_denom

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigfpe_flow_service.set_denom, Make.set_denom -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:41:1`

### #796 DUPLICATE_CODE_DRY on `C_sigfpe_flow_service.raise_fn`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:46:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 4 location(s): C_sigfpe_flow_service.raise_fn, C_sigill_flow_service.raise_fn, Make.raise_fn

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 4 location(s): C_sigfpe_flow_service.raise_fn, C_sigill_flow_service.raise_fn, Make.raise_fn -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:46:1`

### #797 DUPLICATE_CODE_DRY on `C_sigfpe_flow_service.trigger_fpe`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:47:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigfpe_flow_service.trigger_fpe, Make.trigger_fpe

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigfpe_flow_service.trigger_fpe, Make.trigger_fpe -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:47:1`

### #798 DUPLICATE_CODE_DRY on `C_sigfpe_flow_service.signal_fn`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:54:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 6 location(s): C_sigfpe_flow_service.signal_fn, C_sigill_flow_service.signal_fn, C_implicit_flow_service.signal_fn

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 6 location(s): C_sigfpe_flow_service.signal_fn, C_sigill_flow_service.signal_fn, C_implicit_flow_service.signal_fn -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:54:1`

### #799 DUPLICATE_CODE_DRY on `C_sigfpe_flow_service.handler_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:55:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigfpe_flow_service.handler_var, Make.handler_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigfpe_flow_service.handler_var, Make.handler_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:55:1`

### #800 DUPLICATE_CODE_DRY on `C_sigfpe_flow_service.call_signal`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:56:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigfpe_flow_service.call_signal, Make.call_signal

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigfpe_flow_service.call_signal, Make.call_signal -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:56:1`

### #801 DUPLICATE_CODE_DRY on `C_sigfpe_flow_service.sigsetjmp_fn`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:62:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 6 location(s): C_sigfpe_flow_service.sigsetjmp_fn, C_sigill_flow_service.sigsetjmp_fn, C_implicit_flow_service.sigsetjmp_fn

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 6 location(s): C_sigfpe_flow_service.sigsetjmp_fn, C_sigill_flow_service.sigsetjmp_fn, C_implicit_flow_service.sigsetjmp_fn -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:62:1`

### #802 DUPLICATE_CODE_DRY on `C_sigfpe_flow_service.call_setjmp`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:65:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 6 location(s): C_sigfpe_flow_service.call_setjmp, C_sigill_flow_service.call_setjmp, C_implicit_flow_service.call_setjmp

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 6 location(s): C_sigfpe_flow_service.call_setjmp, C_sigill_flow_service.call_setjmp, C_implicit_flow_service.call_setjmp -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:65:1`

### #803 DUPLICATE_CODE_DRY on `C_sigfpe_flow_service.is_first_entry`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:70:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 6 location(s): C_sigfpe_flow_service.is_first_entry, C_sigill_flow_service.is_first_entry, C_implicit_flow_service.is_first_entry

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 6 location(s): C_sigfpe_flow_service.is_first_entry, C_sigill_flow_service.is_first_entry, C_implicit_flow_service.is_first_entry -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:70:1`

### #804 DUPLICATE_CODE_DRY on `C_sigfpe_flow_service.normal_branch_block`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:72:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigfpe_flow_service.normal_branch_block, Make.normal_branch_block

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigfpe_flow_service.normal_branch_block, Make.normal_branch_block -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:72:1`

### #805 DUPLICATE_CODE_DRY on `C_sigfpe_flow_service.fpe_if`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:75:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigfpe_flow_service.fpe_if, Make.fpe_if

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigfpe_flow_service.fpe_if, Make.fpe_if -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:75:1`

### #806 DUPLICATE_CODE_DRY on `C_sigfpe_flow_service.vis`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:92:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigfpe_flow_service.vis, Make.vis

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigfpe_flow_service.vis, Make.vis -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigfpe_flow_service.ml:92:1`

### #807 DUPLICATE_CODE_DRY on `C_sigill_flow_service.sig_proto`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigill_flow_service.ml:15:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigill_flow_service.sig_proto, Make.sig_proto

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigill_flow_service.sig_proto, Make.sig_proto -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigill_flow_service.ml:15:1`

### #808 DUPLICATE_CODE_DRY on `C_sigill_flow_service.handler_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigill_flow_service.ml:37:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigill_flow_service.handler_var, Make.handler_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigill_flow_service.handler_var, Make.handler_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigill_flow_service.ml:37:1`

### #809 DUPLICATE_CODE_DRY on `C_sigill_flow_service.call_signal`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigill_flow_service.ml:38:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigill_flow_service.call_signal, Make.call_signal

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigill_flow_service.call_signal, Make.call_signal -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigill_flow_service.ml:38:1`

### #810 DUPLICATE_CODE_DRY on `C_sigill_flow_service.trigger_ill`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigill_flow_service.ml:54:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigill_flow_service.trigger_ill, Make.trigger_ill

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigill_flow_service.trigger_ill, Make.trigger_ill -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigill_flow_service.ml:54:1`

### #811 DUPLICATE_CODE_DRY on `C_sigill_flow_service.ill_if`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigill_flow_service.ml:64:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigill_flow_service.ill_if, Make.ill_if

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigill_flow_service.ill_if, Make.ill_if -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigill_flow_service.ml:64:1`

### #812 DUPLICATE_CODE_DRY on `C_sigill_flow_service.vis`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigill_flow_service.ml:81:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigill_flow_service.vis, Make.vis

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_sigill_flow_service.vis, Make.vis -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_sigill_flow_service.ml:81:1`

### #813 DUPLICATE_CODE_DRY on `C_implicit_flow_service.sig_proto`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:14:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_implicit_flow_service.sig_proto, Make.sig_proto

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_implicit_flow_service.sig_proto, Make.sig_proto -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:14:1`

### #814 DUPLICATE_CODE_DRY on `C_implicit_flow_service.ptr_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:36:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_implicit_flow_service.ptr_var, Make.ptr_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_implicit_flow_service.ptr_var, Make.ptr_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:36:1`

### #815 DUPLICATE_CODE_DRY on `C_implicit_flow_service.question_exp`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:41:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_implicit_flow_service.question_exp, Make.question_exp

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_implicit_flow_service.question_exp, Make.question_exp -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:41:1`

### #816 DUPLICATE_CODE_DRY on `C_implicit_flow_service.set_ptr`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:42:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_implicit_flow_service.set_ptr, Make.set_ptr

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_implicit_flow_service.set_ptr, Make.set_ptr -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:42:1`

### #817 DUPLICATE_CODE_DRY on `C_implicit_flow_service.set_deref`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:48:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_implicit_flow_service.set_deref, Make.set_deref

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_implicit_flow_service.set_deref, Make.set_deref -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:48:1`

### #818 DUPLICATE_CODE_DRY on `C_implicit_flow_service.handler_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:54:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_implicit_flow_service.handler_var, Make.handler_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_implicit_flow_service.handler_var, Make.handler_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:54:1`

### #819 DUPLICATE_CODE_DRY on `C_implicit_flow_service.call_signal`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:55:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_implicit_flow_service.call_signal, Make.call_signal

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_implicit_flow_service.call_signal, Make.call_signal -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:55:1`

### #820 DUPLICATE_CODE_DRY on `C_implicit_flow_service.implicit_if`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:76:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_implicit_flow_service.implicit_if, Make.implicit_if

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_implicit_flow_service.implicit_if, Make.implicit_if -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:76:1`

### #821 DUPLICATE_CODE_DRY on `C_implicit_flow_service.vis`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:92:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_implicit_flow_service.vis, Make.vis

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_implicit_flow_service.vis, Make.vis -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_implicit_flow_service.ml:92:1`

### #822 DUPLICATE_CODE_DRY on `C_syscall_error_flow_service.unistd_proto`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_syscall_error_flow_service.ml:15:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_syscall_error_flow_service.unistd_proto, Make.unistd_proto

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_syscall_error_flow_service.unistd_proto, Make.unistd_proto -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_syscall_error_flow_service.ml:15:1`

### #823 DUPLICATE_CODE_DRY on `C_syscall_error_flow_service.sys_path_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_syscall_error_flow_service.ml:30:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_syscall_error_flow_service.sys_path_var, Make.sys_path_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_syscall_error_flow_service.sys_path_var, Make.sys_path_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_syscall_error_flow_service.ml:30:1`

### #824 DUPLICATE_CODE_DRY on `C_syscall_error_flow_service.set_path`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_syscall_error_flow_service.ml:38:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_syscall_error_flow_service.set_path, Make.set_path

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_syscall_error_flow_service.set_path, Make.set_path -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_syscall_error_flow_service.ml:38:1`

### #825 DUPLICATE_CODE_DRY on `C_syscall_error_flow_service.access_fn`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_syscall_error_flow_service.ml:43:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_syscall_error_flow_service.access_fn, Make.access_fn

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_syscall_error_flow_service.access_fn, Make.access_fn -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_syscall_error_flow_service.ml:43:1`

### #826 DUPLICATE_CODE_DRY on `C_syscall_error_flow_service.call_access`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_syscall_error_flow_service.ml:44:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_syscall_error_flow_service.call_access, Make.call_access

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_syscall_error_flow_service.call_access, Make.call_access -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/implicit_flow/c_syscall_error_flow_service.ml:44:1`

### #827 DUPLICATE_CODE_DRY on `C_flattening_service.unwrap_blocks`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:10:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_flattening_service.unwrap_blocks, Make.unwrap_blocks

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_flattening_service.unwrap_blocks, Make.unwrap_blocks -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:10:1`

### #828 DUPLICATE_CODE_DRY on `C_flattening_service.orig_stmts`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:25:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_flattening_service.orig_stmts, Make.orig_stmts

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_flattening_service.orig_stmts, Make.orig_stmts -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:25:1`

### #829 DUPLICATE_CODE_DRY on `C_flattening_service.states`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:32:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_flattening_service.states, Make.states

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_flattening_service.states, Make.states -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:32:1`

### #830 DUPLICATE_CODE_DRY on `C_flattening_service.case_label`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:42:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_flattening_service.case_label, Make.case_label

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_flattening_service.case_label, Make.case_label -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:42:1`

### #831 DUPLICATE_CODE_DRY on `C_flattening_service.set_next_state`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:47:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_flattening_service.set_next_state, Make.set_next_state

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_flattening_service.set_next_state, Make.set_next_state -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:47:1`

### #832 DUPLICATE_CODE_DRY on `C_flattening_service.block_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:51:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_flattening_service.block_stmt, Make.block_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_flattening_service.block_stmt, Make.block_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:51:1`

### #833 DUPLICATE_CODE_DRY on `C_flattening_service.switch_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:64:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_flattening_service.switch_stmt, Make.switch_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_flattening_service.switch_stmt, Make.switch_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:64:1`

### #834 DUPLICATE_CODE_DRY on `C_flattening_service.if_check`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:70:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_flattening_service.if_check, Make.if_check

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_flattening_service.if_check, Make.if_check -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:70:1`

### #835 DUPLICATE_CODE_DRY on `C_flattening_service.loop_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:73:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_flattening_service.loop_stmt, Make.loop_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_flattening_service.loop_stmt, Make.loop_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_flattening_service.ml:73:1`

### #836 DUPLICATE_CODE_DRY on `C_diophantine_opaque_service.transform_stmts`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_diophantine_opaque_service.ml:12:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_diophantine_opaque_service.transform_stmts, Make.transform_stmts

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_diophantine_opaque_service.transform_stmts, Make.transform_stmts -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_diophantine_opaque_service.ml:12:1`

### #837 DUPLICATE_CODE_DRY on `C_diophantine_opaque_service.trap_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_diophantine_opaque_service.ml:36:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_diophantine_opaque_service.trap_stmt, Make.trap_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_diophantine_opaque_service.trap_stmt, Make.trap_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_diophantine_opaque_service.ml:36:1`

### #838 DUPLICATE_CODE_DRY on `C_diophantine_opaque_service.trap_if`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_diophantine_opaque_service.ml:38:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_diophantine_opaque_service.trap_if, Make.trap_if

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_diophantine_opaque_service.trap_if, Make.trap_if -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_diophantine_opaque_service.ml:38:1`

### #839 DUPLICATE_CODE_DRY on `C_loop_unroll_service.jitter_instr1`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_unroll_service.ml:12:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_unroll_service.jitter_instr1, Make.jitter_instr1

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_unroll_service.jitter_instr1, Make.jitter_instr1 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_unroll_service.ml:12:1`

### #840 DUPLICATE_CODE_DRY on `C_loop_unroll_service.jitter_instr2`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_unroll_service.ml:15:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_unroll_service.jitter_instr2, Make.jitter_instr2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_unroll_service.jitter_instr2, Make.jitter_instr2 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_unroll_service.ml:15:1`

### #841 DUPLICATE_CODE_DRY on `C_loop_unroll_service.cloned_stmts`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_unroll_service.ml:19:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_unroll_service.cloned_stmts, Make.cloned_stmts

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_unroll_service.cloned_stmts, Make.cloned_stmts -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_unroll_service.ml:19:1`

### #842 DUPLICATE_CODE_DRY on `C_loop_unroll_service.unrolled_stmts`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_unroll_service.ml:22:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_unroll_service.unrolled_stmts, Make.unrolled_stmts

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_unroll_service.unrolled_stmts, Make.unrolled_stmts -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_unroll_service.ml:22:1`

### #843 DUPLICATE_CODE_DRY on `C_loop_unroll_service.funcs`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_unroll_service.ml:33:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_unroll_service.funcs, C_loop_fission_service.funcs

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_unroll_service.funcs, C_loop_fission_service.funcs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_unroll_service.ml:33:1`

### #844 DUPLICATE_CODE_DRY on `C_basic_block_split_service.is_terminator`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:7:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_basic_block_split_service.is_terminator, Make.is_terminator

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_basic_block_split_service.is_terminator, Make.is_terminator -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:7:1`

### #845 DUPLICATE_CODE_DRY on `C_basic_block_split_service.apply_split`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:12:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_basic_block_split_service.apply_split, Make.apply_split

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_basic_block_split_service.apply_split, Make.apply_split -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:12:1`

### #846 DUPLICATE_CODE_DRY on `C_basic_block_split_service.orig_stmts`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:17:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_basic_block_split_service.orig_stmts, Make.orig_stmts

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_basic_block_split_service.orig_stmts, Make.orig_stmts -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:17:1`

### #847 DUPLICATE_CODE_DRY on `C_basic_block_split_service.process_stmts`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:21:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_basic_block_split_service.process_stmts, Make.process_stmts

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_basic_block_split_service.process_stmts, Make.process_stmts -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:21:1`

### #848 DUPLICATE_CODE_DRY on `C_basic_block_split_service.lbl_name`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:28:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_basic_block_split_service.lbl_name, Make.lbl_name

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_basic_block_split_service.lbl_name, Make.lbl_name -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:28:1`

### #849 DUPLICATE_CODE_DRY on `C_basic_block_split_service.target_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:29:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_basic_block_split_service.target_stmt, Make.target_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_basic_block_split_service.target_stmt, Make.target_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:29:1`

### #850 DUPLICATE_CODE_DRY on `C_basic_block_split_service.goto_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:31:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_basic_block_split_service.goto_stmt, Make.goto_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_basic_block_split_service.goto_stmt, Make.goto_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_basic_block_split_service.ml:31:1`

### #851 DUPLICATE_CODE_DRY on `C_irreducible_loop_service.loop_counter`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:5:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.loop_counter, Make.loop_counter

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.loop_counter, Make.loop_counter -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:5:1`

### #852 DUPLICATE_CODE_DRY on `C_irreducible_loop_service.irred_phase`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:21:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.irred_phase, Make.irred_phase

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.irred_phase, Make.irred_phase -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:21:1`

### #853 DUPLICATE_CODE_DRY on `C_irreducible_loop_service.irred_exit_code`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:22:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.irred_exit_code, Make.irred_exit_code

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.irred_exit_code, Make.irred_exit_code -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:22:1`

### #854 DUPLICATE_CODE_DRY on `C_irreducible_loop_service.lbl_stmt_a`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:25:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.lbl_stmt_a, Make.lbl_stmt_a

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.lbl_stmt_a, Make.lbl_stmt_a -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:25:1`

### #855 DUPLICATE_CODE_DRY on `C_irreducible_loop_service.lbl_stmt_b`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:28:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.lbl_stmt_b, Make.lbl_stmt_b

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.lbl_stmt_b, Make.lbl_stmt_b -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:28:1`

### #856 DUPLICATE_CODE_DRY on `C_irreducible_loop_service.lbl_stmt_exit1`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:31:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.lbl_stmt_exit1, Make.lbl_stmt_exit1

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.lbl_stmt_exit1, Make.lbl_stmt_exit1 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:31:1`

### #857 DUPLICATE_CODE_DRY on `C_irreducible_loop_service.lbl_stmt_exit2`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:34:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.lbl_stmt_exit2, Make.lbl_stmt_exit2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.lbl_stmt_exit2, Make.lbl_stmt_exit2 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:34:1`

### #858 DUPLICATE_CODE_DRY on `C_irreducible_loop_service.lbl_stmt_merge`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:37:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.lbl_stmt_merge, Make.lbl_stmt_merge

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.lbl_stmt_merge, Make.lbl_stmt_merge -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:37:1`

### #859 DUPLICATE_CODE_DRY on `C_irreducible_loop_service.patch_stmts`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:42:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.patch_stmts, Make.patch_stmts

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.patch_stmts, Make.patch_stmts -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:42:1`

### #860 DUPLICATE_CODE_DRY on `C_irreducible_loop_service.init_phase`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:61:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.init_phase, Make.init_phase

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.init_phase, Make.init_phase -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:61:1`

### #861 DUPLICATE_CODE_DRY on `C_irreducible_loop_service.dispatch_entry`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:65:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.dispatch_entry, Make.dispatch_entry

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.dispatch_entry, Make.dispatch_entry -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:65:1`

### #862 DUPLICATE_CODE_DRY on `C_irreducible_loop_service.exit1_handler`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:77:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.exit1_handler, Make.exit1_handler

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.exit1_handler, Make.exit1_handler -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:77:1`

### #863 DUPLICATE_CODE_DRY on `C_irreducible_loop_service.exit2_handler`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:84:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.exit2_handler, Make.exit2_handler

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_irreducible_loop_service.exit2_handler, Make.exit2_handler -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_irreducible_loop_service.ml:84:1`

### #864 DUPLICATE_CODE_DRY on `C_opaque_service.int_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_opaque_service.ml:10:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_opaque_service.int_var, Make.int_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_opaque_service.int_var, Make.int_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_opaque_service.ml:10:1`

### #865 DUPLICATE_CODE_DRY on `C_opaque_service.m2`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_opaque_service.ml:28:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_opaque_service.m2, Make.m2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_opaque_service.m2, Make.m2 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_opaque_service.ml:28:1`

### #866 DUPLICATE_CODE_DRY on `C_opaque_service.ank`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_opaque_service.ml:36:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_opaque_service.ank, Make.ank

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_opaque_service.ank, Make.ank -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_opaque_service.ml:36:1`

### #867 DUPLICATE_CODE_DRY on `C_opaque_service.sump1`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_opaque_service.ml:43:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_opaque_service.sump1, Make.sump1

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_opaque_service.sump1, Make.sump1 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_opaque_service.ml:43:1`

### #868 DUPLICATE_CODE_DRY on `C_opaque_service.rhs`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_opaque_service.ml:52:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_opaque_service.rhs, Make.rhs

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_opaque_service.rhs, Make.rhs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_opaque_service.ml:52:1`

### #869 DUPLICATE_CODE_DRY on `C_opaque_service.junk_instr`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_opaque_service.ml:56:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_opaque_service.junk_instr, Make.junk_instr

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_opaque_service.junk_instr, Make.junk_instr -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_opaque_service.ml:56:1`

### #870 DUPLICATE_CODE_DRY on `C_indirect_jump_service.apply_indirect_jumps`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:5:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_indirect_jump_service.apply_indirect_jumps, Make.apply_indirect_jumps

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_indirect_jump_service.apply_indirect_jumps, Make.apply_indirect_jumps -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:5:1`

### #871 DUPLICATE_CODE_DRY on `C_indirect_jump_service.next_state_id`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:19:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_indirect_jump_service.next_state_id, Make.next_state_id

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_indirect_jump_service.next_state_id, Make.next_state_id -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:19:1`

### #872 DUPLICATE_CODE_DRY on `C_indirect_jump_service.update_state`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:22:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_indirect_jump_service.update_state, Make.update_state

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_indirect_jump_service.update_state, Make.update_state -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:22:1`

### #873 DUPLICATE_CODE_DRY on `C_indirect_jump_service.case_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:26:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_indirect_jump_service.case_stmt, Make.case_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_indirect_jump_service.case_stmt, Make.case_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:26:1`

### #874 DUPLICATE_CODE_DRY on `C_indirect_jump_service.switch_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:31:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_indirect_jump_service.switch_stmt, Make.switch_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_indirect_jump_service.switch_stmt, Make.switch_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:31:1`

### #875 DUPLICATE_CODE_DRY on `C_indirect_jump_service.dispatch_loop`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:36:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_indirect_jump_service.dispatch_loop, Make.dispatch_loop

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_indirect_jump_service.dispatch_loop, Make.dispatch_loop -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:36:1`

### #876 DUPLICATE_CODE_DRY on `C_indirect_jump_service.init_state`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:39:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_indirect_jump_service.init_state, Make.init_state

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_indirect_jump_service.init_state, Make.init_state -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_indirect_jump_service.ml:39:1`

### #877 DUPLICATE_CODE_DRY on `C_loop_fission_service.split`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_fission_service.ml:13:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_fission_service.split, Make.split

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_fission_service.split, Make.split -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_fission_service.ml:13:1`

### #878 DUPLICATE_CODE_DRY on `C_loop_fission_service.set_phase1`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_fission_service.ml:20:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 4 location(s): C_loop_fission_service.set_phase1, C_loop_fission_service.init_phase, Make.set_phase1

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 4 location(s): C_loop_fission_service.set_phase1, C_loop_fission_service.init_phase, Make.set_phase1 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_fission_service.ml:20:1`

### #879 DUPLICATE_CODE_DRY on `C_loop_fission_service.set_phase2`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_fission_service.ml:21:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_fission_service.set_phase2, Make.set_phase2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_fission_service.set_phase2, Make.set_phase2 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_fission_service.ml:21:1`

### #880 DUPLICATE_CODE_DRY on `C_loop_fission_service.if_phase1`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_fission_service.ml:23:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_fission_service.if_phase1, Make.if_phase1

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_loop_fission_service.if_phase1, Make.if_phase1 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_loop_fission_service.ml:23:1`

### #881 DUPLICATE_CODE_DRY on `C_dynamic_opaque_service.int_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_dynamic_opaque_service.ml:9:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_dynamic_opaque_service.int_var, Make.int_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_dynamic_opaque_service.int_var, Make.int_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_dynamic_opaque_service.ml:9:1`

### #882 DUPLICATE_CODE_DRY on `C_dynamic_opaque_service.m2`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_dynamic_opaque_service.ml:63:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_dynamic_opaque_service.m2, Make.m2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_dynamic_opaque_service.m2, Make.m2 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_dynamic_opaque_service.ml:63:1`

### #883 DUPLICATE_CODE_DRY on `C_dynamic_opaque_service.sump1`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_dynamic_opaque_service.ml:53:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_dynamic_opaque_service.sump1, Make.sump1

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_dynamic_opaque_service.sump1, Make.sump1 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_dynamic_opaque_service.ml:53:1`

### #884 DUPLICATE_CODE_DRY on `C_dynamic_opaque_service.reco`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_dynamic_opaque_service.ml:75:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_dynamic_opaque_service.reco, Make.reco

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_dynamic_opaque_service.reco, Make.reco -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_dynamic_opaque_service.ml:75:1`

### #885 DUPLICATE_CODE_DRY on `C_dynamic_opaque_service.junk_instr`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_dynamic_opaque_service.ml:87:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_dynamic_opaque_service.junk_instr, Make.junk_instr

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_dynamic_opaque_service.junk_instr, Make.junk_instr -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/control_flow/c_dynamic_opaque_service.ml:87:1`

### #886 DUPLICATE_CODE_DRY on `C_self_checksum_service.checksum_helper`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_self_checksum_service.ml:15:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_checksum_service.checksum_helper, Make.checksum_helper

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_checksum_service.checksum_helper, Make.checksum_helper -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_self_checksum_service.ml:15:1`

### #887 DUPLICATE_CODE_DRY on `C_self_checksum_service.crc_fn`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_self_checksum_service.ml:30:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_checksum_service.crc_fn, Make.crc_fn

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_checksum_service.crc_fn, Make.crc_fn -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_self_checksum_service.ml:30:1`

### #888 DUPLICATE_CODE_DRY on `C_self_checksum_service.call_crc`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_self_checksum_service.ml:33:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_checksum_service.call_crc, Make.call_crc

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_checksum_service.call_crc, Make.call_crc -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_self_checksum_service.ml:33:1`

### #889 DUPLICATE_CODE_DRY on `C_self_checksum_service.poison_expr`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_self_checksum_service.ml:38:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_checksum_service.poison_expr, Make.poison_expr

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_checksum_service.poison_expr, Make.poison_expr -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_self_checksum_service.ml:38:1`

### #890 DUPLICATE_CODE_DRY on `C_self_checksum_service.rewrite_returns`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_self_checksum_service.ml:47:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_checksum_service.rewrite_returns, Make.rewrite_returns

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_self_checksum_service.rewrite_returns, Make.rewrite_returns -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_self_checksum_service.ml:47:1`

### #891 DUPLICATE_CODE_DRY on `C_anti_vtil_aliasing_service.should_transform`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_vtil_aliasing_service.ml:7:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_vtil_aliasing_service.should_transform, Make.should_transform

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_vtil_aliasing_service.should_transform, Make.should_transform -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_vtil_aliasing_service.ml:7:1`

### #892 DUPLICATE_CODE_DRY on `C_anti_vtil_aliasing_service.locals`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_vtil_aliasing_service.ml:15:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_vtil_aliasing_service.locals, Make.locals

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_vtil_aliasing_service.locals, Make.locals -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_vtil_aliasing_service.ml:15:1`

### #893 DUPLICATE_CODE_DRY on `C_anti_vtil_aliasing_service.frame_name`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_vtil_aliasing_service.ml:26:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_vtil_aliasing_service.frame_name, Make.frame_name

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_vtil_aliasing_service.frame_name, Make.frame_name -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_vtil_aliasing_service.ml:26:1`

### #894 DUPLICATE_CODE_DRY on `C_anti_vtil_aliasing_service.visitor`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_vtil_aliasing_service.ml:40:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_vtil_aliasing_service.visitor, Make.visitor

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_vtil_aliasing_service.visitor, Make.visitor -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_vtil_aliasing_service.ml:40:1`

### #895 DUPLICATE_CODE_DRY on `C_anti_vtil_aliasing_service.offset_exp`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_vtil_aliasing_service.ml:48:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_vtil_aliasing_service.offset_exp, Make.offset_exp

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_vtil_aliasing_service.offset_exp, Make.offset_exp -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_vtil_aliasing_service.ml:48:1`

### #896 DUPLICATE_CODE_DRY on `C_anti_disassembly_service.init_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_disassembly_service.ml:12:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_disassembly_service.init_var, Make.init_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_disassembly_service.init_var, Make.init_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_disassembly_service.ml:12:1`

### #897 DUPLICATE_CODE_DRY on `C_anti_disassembly_service.false_cond`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_disassembly_service.ml:13:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_disassembly_service.false_cond, Make.false_cond

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_disassembly_service.false_cond, Make.false_cond -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_disassembly_service.ml:13:1`

### #898 DUPLICATE_CODE_DRY on `C_anti_disassembly_service.ret_exp_opt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_disassembly_service.ml:15:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_disassembly_service.ret_exp_opt, Make.ret_exp_opt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_disassembly_service.ret_exp_opt, Make.ret_exp_opt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_disassembly_service.ml:15:1`

### #899 DUPLICATE_CODE_DRY on `C_anti_debug_service.debug_helper`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_debug_service.ml:15:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_debug_service.debug_helper, Make.debug_helper

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_debug_service.debug_helper, Make.debug_helper -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_debug_service.ml:15:1`

### #900 DUPLICATE_CODE_DRY on `C_anti_debug_service.enforce_fn`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_debug_service.ml:70:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_debug_service.enforce_fn, Make.enforce_fn

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_debug_service.enforce_fn, Make.enforce_fn -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_debug_service.ml:70:1`

### #901 DUPLICATE_CODE_DRY on `C_anti_debug_service.call_enforce`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_debug_service.ml:71:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_debug_service.call_enforce, Make.call_enforce

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_anti_debug_service.call_enforce, Make.call_enforce -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_anti_debug_service.ml:71:1`

### #902 DUPLICATE_CODE_DRY on `C_eh_shadowing_service.arr_ty`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_eh_shadowing_service.ml:16:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_eh_shadowing_service.arr_ty, Make.arr_ty

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_eh_shadowing_service.arr_ty, Make.arr_ty -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_eh_shadowing_service.ml:16:1`

### #903 DUPLICATE_CODE_DRY on `C_eh_shadowing_service.table_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_eh_shadowing_service.ml:17:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_eh_shadowing_service.table_var, Make.table_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_eh_shadowing_service.table_var, Make.table_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_eh_shadowing_service.ml:17:1`

### #904 DUPLICATE_CODE_DRY on `C_eh_shadowing_service.b`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_eh_shadowing_service.ml:22:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_eh_shadowing_service.b, Make.b

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_eh_shadowing_service.b, Make.b -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_eh_shadowing_service.ml:22:1`

### #905 DUPLICATE_CODE_DRY on `C_eh_shadowing_service.table_global`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_eh_shadowing_service.ml:26:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_eh_shadowing_service.table_global, Make.table_global

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_eh_shadowing_service.table_global, Make.table_global -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_eh_shadowing_service.ml:26:1`

### #906 DUPLICATE_CODE_DRY on `C_eh_shadowing_service.personality_var`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_eh_shadowing_service.ml:29:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_eh_shadowing_service.personality_var, Make.personality_var

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_eh_shadowing_service.personality_var, Make.personality_var -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_eh_shadowing_service.ml:29:1`

### #907 DUPLICATE_CODE_DRY on `C_eh_shadowing_service.pers_fundec`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_eh_shadowing_service.ml:38:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_eh_shadowing_service.pers_fundec, Make.pers_fundec

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_eh_shadowing_service.pers_fundec, Make.pers_fundec -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_eh_shadowing_service.ml:38:1`

### #908 DUPLICATE_CODE_DRY on `C_eh_shadowing_service.ret_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_eh_shadowing_service.ml:40:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_eh_shadowing_service.ret_stmt, Make.ret_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_eh_shadowing_service.ret_stmt, Make.ret_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_eh_shadowing_service.ml:40:1`

### #909 DUPLICATE_CODE_DRY on `C_eh_shadowing_service.asm_templates`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_eh_shadowing_service.ml:49:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_eh_shadowing_service.asm_templates, Make.asm_templates

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_eh_shadowing_service.asm_templates, Make.asm_templates -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_eh_shadowing_service.ml:49:1`

### #910 DUPLICATE_CODE_DRY on `C_hook_detect_service.hook_helper`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_hook_detect_service.ml:16:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_hook_detect_service.hook_helper, Make.hook_helper

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_hook_detect_service.hook_helper, Make.hook_helper -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_hook_detect_service.ml:16:1`

### #911 DUPLICATE_CODE_DRY on `C_hook_detect_service.hook_fn`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_hook_detect_service.ml:30:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_hook_detect_service.hook_fn, Make.hook_fn

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_hook_detect_service.hook_fn, Make.hook_fn -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_hook_detect_service.ml:30:1`

### #912 DUPLICATE_CODE_DRY on `C_hook_detect_service.call_hook_check`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_hook_detect_service.ml:33:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_hook_detect_service.call_hook_check, Make.call_hook_check

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_hook_detect_service.call_hook_check, Make.call_hook_check -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_hook_detect_service.ml:33:1`

### #913 DUPLICATE_CODE_DRY on `C_hook_detect_service.hook_cond`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_hook_detect_service.ml:37:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_hook_detect_service.hook_cond, Make.hook_cond

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_hook_detect_service.hook_cond, Make.hook_cond -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_hook_detect_service.ml:37:1`

### #914 DUPLICATE_CODE_DRY on `C_timing_check_service.timing_helper`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_timing_check_service.ml:15:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_timing_check_service.timing_helper, Make.timing_helper

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_timing_check_service.timing_helper, Make.timing_helper -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_timing_check_service.ml:15:1`

### #915 DUPLICATE_CODE_DRY on `C_timing_check_service.time_fn`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_timing_check_service.ml:36:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_timing_check_service.time_fn, Make.time_fn

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_timing_check_service.time_fn, Make.time_fn -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_timing_check_service.ml:36:1`

### #916 DUPLICATE_CODE_DRY on `C_timing_check_service.call_t1`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_timing_check_service.ml:40:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_timing_check_service.call_t1, Make.call_t1

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_timing_check_service.call_t1, Make.call_t1 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_timing_check_service.ml:40:1`

### #917 DUPLICATE_CODE_DRY on `C_timing_check_service.call_t2`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_timing_check_service.ml:41:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_timing_check_service.call_t2, Make.call_t2

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_timing_check_service.call_t2, Make.call_t2 -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_timing_check_service.ml:41:1`

### #918 DUPLICATE_CODE_DRY on `C_timing_check_service.delta_exp`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_timing_check_service.ml:43:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_timing_check_service.delta_exp, Make.delta_exp

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_timing_check_service.delta_exp, Make.delta_exp -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_timing_check_service.ml:43:1`

### #919 DUPLICATE_CODE_DRY on `C_timing_check_service.check_stmt`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_timing_check_service.ml:44:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): C_timing_check_service.check_stmt, Make.check_stmt

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): C_timing_check_service.check_stmt, Make.check_stmt -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/anti_analysis/c_timing_check_service.ml:44:1`

### #920 DUPLICATE_CODE_DRY on `Make.funcs`
- **Category:** `principle`
- **Confidence:** **80%** [HIGH]
- **Primary Location:** `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:72:1`
- **Summary:** DRY Violation: Identical function logic duplicated across 2 location(s): Make.funcs, Make.funcs

#### Evidence Trail:
- `+80%` **[DRY_CODE_DUPLICATION]** DRY Violation: Identical function logic duplicated across 2 location(s): Make.funcs, Make.funcs -> `/Volumes/External/Code/vectis/lib/domain/services/c_source/virtualization/tiers/c_self_modifying_vm_service.ml:72:1`
