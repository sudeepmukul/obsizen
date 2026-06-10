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

        filename = doc.metadata.get(
    "filename",
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

        md_chunks = markdown_splitter.split_text(
        doc.page_content
    )

        for chunk in md_chunks:

            chunk.metadata.update(
            doc.metadata
        )
        all_chunks.extend(md_chunks)

    print(
    f"Created {len(all_chunks)} markdown sections"
)


    recursive_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CONFIG["index"]["chunk_size"],
    chunk_overlap=CONFIG["index"]["chunk_overlap"]
)

    chunks = recursive_splitter.split_documents(
    all_chunks
)

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

    return db