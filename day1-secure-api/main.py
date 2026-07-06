import os
import time
import logging
from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4.1-mini")

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is missing. Add it to your .env file.")

client = OpenAI(api_key=OPENAI_API_KEY)

app = FastAPI(
    title="AI DevOps Assistant - Day 1",
    description="Secure LLM API integration with FastAPI",
    version="1.0.0"
)


class AskRequest(BaseModel):
    question: str


class AskResponse(BaseModel):
    answer: str
    model: str
    latency_ms: int
    status: str
    error: Optional[str] = None


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "day1-secure-api"
    }


@app.post("/ask", response_model=AskResponse)
def ask_llm(request: AskRequest):
    start_time = time.time()

    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")

    system_prompt = """
    You are an AI DevOps Assistant.
    Explain technical concepts clearly and practically.
    Keep answers useful for DevOps, Cloud, CI/CD, and production operations.
    """

    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": request.question}
            ],
            temperature=0.2,
            timeout=30
        )

        answer = response.choices[0].message.content
        latency_ms = int((time.time() - start_time) * 1000)

        logging.info({
            "event": "llm_request_success",
            "model": LLM_MODEL,
            "latency_ms": latency_ms
        })

        return AskResponse(
            answer=answer,
            model=LLM_MODEL,
            latency_ms=latency_ms,
            status="success"
        )

    except Exception as e:
        latency_ms = int((time.time() - start_time) * 1000)

        logging.error({
            "event": "llm_request_failed",
            "error": str(e),
            "latency_ms": latency_ms
        })

        return AskResponse(
            answer="",
            model=LLM_MODEL,
            latency_ms=latency_ms,
            status="failed",
            error=str(e)
        )
