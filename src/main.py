from pathlib import Path
import time

from core.indexing import build_index
from core.embeddings import get_embeddings
from core.retrieval import (
    get_db,
    get_bm25,
    get_reranker
)
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
    get_db()
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