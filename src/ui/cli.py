from core.retrieval import retrieve
from llm.openrouter import get_llm


def chat():

    llm = get_llm()

    print("ObsiZen Ready! Thanks for the wait UNC")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("Ask Away!Hehe: ")

        if question.lower() == "exit":
            break

        docs = retrieve(question)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
Answer ONLY from the provided notes.

NOTES:
{context}

QUESTION:
{question}
"""

        response = llm.invoke(prompt)

        print("\nANSWER:\n")
        print(response.content)

        print("\nSOURCES:")

        shown = set()

        for doc in docs:

            source = doc.metadata.get(
                "source",
                "Unknown"
            )

            filename = source.split("\\")[-1]

            if filename not in shown:
                print(f" {filename}")
                shown.add(filename)

        print("\n")