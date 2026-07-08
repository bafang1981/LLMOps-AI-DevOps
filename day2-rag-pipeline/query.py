import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4.1-mini")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

VECTORSTORE_PATH = "vectorstore"

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is missing. Add it to your .env file.")


PROMPT_TEMPLATE = """
You are an AI DevOps Assistant.

Answer the user's question using only the context below.

If the answer is not found in the context, say:
"I could not find that information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""


def main():
    question = input("Ask a question about your documents: ")

    if not question.strip():
        print("Question cannot be empty.")
        return

    embeddings = OpenAIEmbeddings(
        model=EMBEDDING_MODEL,
        api_key=OPENAI_API_KEY
    )

    vectorstore = Chroma(
        persist_directory=VECTORSTORE_PATH,
        embedding_function=embeddings
    )

    results = vectorstore.similarity_search_with_score(question, k=3)

    if not results:
        print("No relevant documents found.")
        return

    context_text = "\n\n---\n\n".join([doc.page_content for doc, score in results])

    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    formatted_prompt = prompt.format(
        context=context_text,
        question=question
    )

    llm = ChatOpenAI(
        model=LLM_MODEL,
        api_key=OPENAI_API_KEY,
        temperature=0.2
    )

    response = llm.invoke(formatted_prompt)

    print("\nAnswer:")
    print(response.content)

    print("\nSources used:")
    for i, (doc, score) in enumerate(results, start=1):
        source = doc.metadata.get("source", "unknown")
        print(f"{i}. {source} | similarity score: {score}")


if __name__ == "__main__":
    main()
