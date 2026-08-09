from langchain_core.documents import Document

from src.core.indexing import chunk_document


def test_markdown_is_split_into_chunks():
    document = Document(
        page_content="""
# My Notes

This is some content.

## Python

Python is a programming language.

## FastAPI

FastAPI is a Python web framework.
""",
        metadata={
            "source": "test.md"
        }
    )

    chunks = chunk_document(document)

    assert len(chunks) > 0


def test_chunk_preserves_metadata():
    document = Document(
        page_content="""
# My Notes

This is test content.
""",
        metadata={
            "source": "test.md",
            "filename": "test.md"
        }
    )

    chunks = chunk_document(document)

    assert len(chunks) > 0

    for chunk in chunks:
        assert chunk.metadata["source"] == "test.md"
        assert chunk.metadata["filename"] == "test.md"