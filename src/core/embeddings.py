from langchain_community.embeddings import HuggingFaceEmbeddings
from src.config import CONFIG

_embeddings = None


def get_embeddings():

    global _embeddings

    if _embeddings is None:

        print("Loading Embedding Model...")

        _embeddings = HuggingFaceEmbeddings(
            model_name=CONFIG["embedding"]["model"]
        )

    return _embeddings