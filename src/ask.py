import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

print("Loading vector database...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={
        "device": "cuda"
    }
)

db = Chroma(
    persist_directory="obsidian_db",
    embedding_function=embeddings
)

print("Database loaded!")

llm = ChatOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    model="deepseek/deepseek-chat"
)

print("Ready!")

while True:

    question = input("\nAsk: ")

    if question.lower() in ["exit", "quit"]:
        break

    docs = db.similarity_search(question, k=3)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Answer ONLY using the provided notes.

If the answer is not found in the notes,
say "I couldn't find that in your Obsidian vault."

NOTES:
{context}

QUESTION:
{question}
"""

    response = llm.invoke(prompt)

    print("\n" + "=" * 60)
    print("ANSWER")
    print("=" * 60)
    print(response.content)

    print("\nSOURCES:")

    shown = set()

    for doc in docs:

        source = doc.metadata.get("source", "Unknown")

        if source not in shown:
            print("-", source)
            shown.add(source)