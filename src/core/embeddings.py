from langchain_community.embeddings import HuggingFaceEmbeddings
from config import CONFIG

def get_embeddings():

    return HuggingFaceEmbeddings(
        model_name=CONFIG["embedding"]["model"]
    )