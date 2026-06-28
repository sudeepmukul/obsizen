from pathlib import Path
import time

from core.indexing import build_index
from core.embeddings import get_embeddings
from core.retrieval import (
    get_db,
    get_bm25,
    get_reranker
)
from core.manifest import (
    load_manifest,
    get_vault_files,
    get_changed_files,
    update_manifest
)

from src.config import CONFIG
from core.indexing import update_file_in_db
from ui.cli import chat

INDEX_PATH = Path("data/obsidian_db")

if __name__ == "__main__":

    # Build index if missing
    if not INDEX_PATH.exists():

        print("No index found.")
        print("Building index...\n")

        build_index()

    # Startup timer
    start_time = time.time()

    print("\nLoading ObsiZen...\n")

    # Preload everything into memory
    get_embeddings()

    db = get_db()

    # Incremental indexing
    manifest = load_manifest()

    current_files = get_vault_files(
    CONFIG["vault"]["path"]
    )

    changed_files = get_changed_files(
        current_files,
        manifest
    )

    print(
        f"\nFound {len(changed_files)} changed files."
    )

    for file_path in changed_files:

        update_file_in_db(
            db,
            file_path
        )

    # Save updated timestamps
    update_manifest(
        changed_files,
        current_files,
        manifest
    )

    get_bm25()
    get_reranker()

    load_time = round(
        time.time() - start_time,
        2
    )

    print(
        f"\nObsiZen Ready! 🚀 "
        f"({load_time}s)\n"
    )

    chat()