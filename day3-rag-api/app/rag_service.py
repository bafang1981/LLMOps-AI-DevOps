import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_rag_question(question: str) -> str:
    """
    Simple Day 3 RAG-style service.
    For now, this uses a static context.
    Later, we will connect this to vector search.
    """

    context = """
    LLMOps combines DevOps practices with Large Language Model applications.
    A RAG pipeline retrieves relevant documents and uses them as context
    before sending a question to an LLM.
    Common LLMOps tools include GitHub, Docker, CI/CD, monitoring, testing,
    vector databases, and deployment platforms.
    """

    prompt = f"""
    You are an LLMOps assistant.

    Use the context below to answer the question.

    Context:
    {context}

    Question:
    {question}

    Answer clearly and professionally.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful LLMOps assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content