import json
import os

MANIFEST_PATH = "data/index_manifest.json"


def load_manifest():

    if not os.path.exists(MANIFEST_PATH):
        return {}

    with open(MANIFEST_PATH, "r") as f:
        return json.load(f)


def save_manifest(manifest):

    os.makedirs("data", exist_ok=True)

    with open(MANIFEST_PATH, "w") as f:
        json.dump(
            manifest,
            f,
            indent=4
        )
from pathlib import Path


def get_vault_files(vault_path):

    files = {}

    for path in Path(vault_path).rglob("*.md"):

        files[str(path)] = path.stat().st_mtime

    return files
def get_changed_files(
        current_files,
        manifest
):

    changed = []

    for path, modified_time in current_files.items():

        if path not in manifest:
            changed.append(path)

        elif (
            modified_time >
            manifest[path]["last_modified"]
        ):
            changed.append(path)

    return changed
def update_manifest(
        changed_files,
        current_files,
        manifest
):

    for file_path in changed_files:

        manifest[file_path] = {
            "last_modified":
            current_files[file_path]
        }

    save_manifest(manifest)