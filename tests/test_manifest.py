from src.core import manifest


def test_get_changed_files_detects_new_file():
    current_files = {
        "notes/test.md": 100.0
    }

    existing_manifest = {}

    changed = manifest.get_changed_files(
        current_files,
        existing_manifest
    )

    assert changed == ["notes/test.md"]


def test_get_changed_files_detects_modified_file():
    current_files = {
        "notes/test.md": 200.0
    }

    existing_manifest = {
        "notes/test.md": {
            "last_modified": 100.0
        }
    }

    changed = manifest.get_changed_files(
        current_files,
        existing_manifest
    )

    assert changed == ["notes/test.md"]


def test_get_changed_files_ignores_unchanged_file():
    current_files = {
        "notes/test.md": 100.0
    }

    existing_manifest = {
        "notes/test.md": {
            "last_modified": 100.0
        }
    }

    changed = manifest.get_changed_files(
        current_files,
        existing_manifest
    )

    assert changed == []