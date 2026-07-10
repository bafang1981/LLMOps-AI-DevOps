from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_service import ask_rag_question

app = FastAPI(
    title="Day 3 RAG API",
    description="A simple API for asking questions using a RAG-style LLMOps service.",
    version="1.0.0",
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "message": "Welcome to Day 3 RAG API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):
    answer = ask_rag_question(request.question)

    return {
        "question": request.question,
        "answer": answer
    }