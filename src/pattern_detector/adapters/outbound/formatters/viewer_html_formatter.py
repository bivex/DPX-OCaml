"""Single-file HTML exporter: renders the interactive Architecture Viewer.

Injects the viewer snapshot (``architecture.json``) and the vendored
Cytoscape.js bundle into ``assets/viewer_template.html`` so that the result is
one self-contained ``.html`` document — openable offline, no CDN, no server.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

_ASSETS_DIR = Path(__file__).parent / "assets"
_TEMPLATE_PATH = _ASSETS_DIR / "viewer_template.html"
_CYTOSCAPE_PATH = _ASSETS_DIR / "cytoscape.min.js"

_CYTOSCAPE_PLACEHOLDER = "__DPX_CYTOSCAPE_JS__"
_SNAPSHOT_PLACEHOLDER = "__DPX_SNAPSHOT_JSON__"


def _script_safe(payload: str) -> str:
    """Escape content for embedding verbatim inside a ``<script>`` tag.

    Only the closing-tag sequence matters: ``</`` would terminate the script
    element early. Escaping it as ``<\\/`` is valid JS (and JSON, since ``\\/``
    is a permitted escape) and cannot occur inside a JSON string literal's
    structural syntax.
    """
    return payload.replace("</", "<\\/")


class ViewerHtmlFormatter:
    """Renders the self-contained viewer HTML from a snapshot dict."""

    def render(self, snapshot: dict[str, Any]) -> str:
        template = _TEMPLATE_PATH.read_text(encoding="utf-8")
        cytoscape_js = _CYTOSCAPE_PATH.read_text(encoding="utf-8")
        snapshot_json = _script_safe(json.dumps(snapshot, ensure_ascii=False))

        html = (
            template.replace(_CYTOSCAPE_PLACEHOLDER, _script_safe(cytoscape_js))
            .replace(_SNAPSHOT_PLACEHOLDER, snapshot_json)
        )
        if _CYTOSCAPE_PLACEHOLDER in html or _SNAPSHOT_PLACEHOLDER in html:
            msg = "viewer template placeholders not fully substituted"
            raise ValueError(msg)
        return html
