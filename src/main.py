from pathlib import Path

from core.indexing import build_index
from ui.cli import chat


INDEX_PATH = Path("data/obsidian_db")

if not INDEX_PATH.exists():

    print("No index found.")
    print("Building index...\n")

    build_index()

chat()