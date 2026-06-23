from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter
)
from config import CONFIG
from core.embeddings import get_embeddings

import pickle
import os


headers_to_split_on = [
    ("#", "title"),
    ("##", "section"),
    ("###", "subsection")
]
markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)
from pathlib import Path


def chunk_document(doc):

    # Split by Markdown headers
    md_chunks = markdown_splitter.split_text(
        doc.page_content
    )

    # Preserve metadata
    for chunk in md_chunks:
        chunk.metadata.update(
            doc.metadata
        )

    # Recursive splitting
    recursive_splitter = (
        RecursiveCharacterTextSplitter(
            chunk_size=CONFIG["index"]["chunk_size"],
            chunk_overlap=CONFIG["index"]["chunk_overlap"]
        )
    )

    final_chunks = (
        recursive_splitter.split_documents(
            md_chunks
        )
    )

    return final_chunks

def build_index():

    print("Loading notes...LOL")

    loader = DirectoryLoader(
        path=CONFIG["vault"]["path"],
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={
            "encoding": "utf-8",
            "autodetect_encoding": True
        },
        silent_errors=True
    )

    docs = loader.load()
    from pathlib import Path

    for doc in docs:

        source = doc.metadata.get(
        "source",
        ""
    )

        path = Path(source)

        doc.metadata["filename"] = path.name

        if len(path.parts) >= 2:
            doc.metadata["folder"] = path.parent.name
        else:
            doc.metadata["folder"] = "Unknown"

    print(f"Loaded {len(docs)} notes")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CONFIG["index"]["chunk_size"],
        chunk_overlap=CONFIG["index"]["chunk_overlap"]
    )

    all_chunks = []

    for doc in docs:

        chunks = chunk_document(doc)

        all_chunks.extend(chunks)

    print(
        f"Created {len(all_chunks)} final chunks"
)

    chunks = all_chunks

    print(
    f"Created {len(chunks)} final chunks"
)
    os.makedirs("data", exist_ok=True)

    with open(
    "data/chunks.pkl",
    "wb"
    ) as f:

      pickle.dump(
        chunks,
        f
    )
    print(f"Created {len(chunks)} chunks")

    db = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory="data/obsidian_db"
    )

    print("Index built successfully!")
    from core.manifest import (
    save_manifest,
    get_vault_files
)

    current_files = get_vault_files(
        CONFIG["vault"]["path"]
)

    manifest = {}

    for file_path, modified_time in current_files.items():

        manifest[file_path] = {
            "last_modified": modified_time
    }

    save_manifest(manifest)

    return db

def update_file_in_db(
        db,
        file_path
):

    print(
        f"Updating: {file_path}"
    )

    # Remove old chunks
    db.delete(
        where={
            "source": file_path
        }
    )

    # Load file
    loader = TextLoader(
        file_path,
        encoding="utf-8"
    )

    docs = loader.load()

    if not docs:
        return

    doc = docs[0]

    path = Path(file_path)

    doc.metadata["filename"] = path.name
    doc.metadata["folder"] = path.parent.name

    # Chunk document
    chunks = chunk_document(doc)

    if not chunks:

        print(
        f"Skipping empty file: {file_path}"
    )

        return

    db.add_documents(chunks)

    print(
    f"Added {len(chunks)} chunks"
)
    

    
    
    
