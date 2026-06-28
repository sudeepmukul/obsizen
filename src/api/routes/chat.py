from fastapi import APIRouter

from src.api.schemas import (
    ChatRequest,
    ChatResponse
)

from src.core.retrieval import retrieve
from src.llm.openrouter import get_llm
from src.llm.openrouter import ask



router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat_endpoint(
    request: ChatRequest
):

    docs = retrieve(
        request.query
    )

    answer = ask(
        request.query,
        docs
    )

    sources = []

    for doc in docs:

        filename = doc.metadata.get(
            "filename",
            "Unknown"
        )

        sources.append(filename)

    return ChatResponse(
        answer=answer,
        sources=sources
    )