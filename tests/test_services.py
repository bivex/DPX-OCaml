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


def test_file_source_provider_exclude_dirs(tmp_path):
    from pattern_detector.adapters.outbound.persistence.file_source_provider import FileSourceProvider

    src_dir = tmp_path / "lib"
    src_dir.mkdir()
    (src_dir / "main.ml").write_text("let x = 1")

    test_dir = tmp_path / "test"
    test_dir.mkdir()
    (test_dir / "test.ml").write_text("let t = 2")

    provider = FileSourceProvider()
    sources_all = provider.get_sources(str(tmp_path))
    assert len(sources_all) == 2

    sources_filtered = provider.get_sources(str(tmp_path), exclude_dirs=["test"])
    assert len(sources_filtered) == 1
    assert str(src_dir / "main.ml") in sources_filtered
