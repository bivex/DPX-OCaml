"""Tests for Scanning and Detection Services in DPX-OCaml."""

from __future__ import annotations

from pattern_detector.bootstrap.container import create_container


def test_scanning_service_memory():
    sources = {
        "lib/buffer.ml": """
        type t = { buf : string }
        let create cap = { buf = String.make cap ' ' }
        let to_string t = t.buf
        """
    }
    container = create_container()
    scanner = container.get_scanner()
    report = scanner.scan_sources(sources)

    assert report.scanned_files_count == 1
    assert report.total_detections_count >= 1
    assert any(d.pattern_type.value == "abstract_data_type_interface" for d in report.detections)
