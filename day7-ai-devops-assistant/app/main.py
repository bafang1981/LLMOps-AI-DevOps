import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.agent import run_ai_devops_assistant
from app.config import SERVICE_NAME, MODEL_NAME, PROMPT_VERSION
from app.observability import (
    generate_request_id,
    calculate_latency_ms,
    build_observability_metadata,
)


app = FastAPI(
    title="Day 7 AI DevOps Assistant Capstone",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    request: str


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": SERVICE_NAME
    }


@app.post("/chat")
def chat(payload: ChatRequest):
    request_id = generate_request_id()
    start_time = time.time()

    if not payload.request.strip():
        latency_ms = calculate_latency_ms(start_time)
        metadata = build_observability_metadata(
            request_id=request_id,
            endpoint="/chat",
            model=MODEL_NAME,
            prompt_version=PROMPT_VERSION,
            latency_ms=latency_ms,
            status="failed"
        )
        raise HTTPException(
            status_code=400,
            detail={
                "message": "Request cannot be empty.",
                "metadata": metadata
            }
        )

    result = run_ai_devops_assistant(payload.request)
    latency_ms = calculate_latency_ms(start_time)

    metadata = build_observability_metadata(
        request_id=request_id,
        endpoint="/chat",
        model=MODEL_NAME,
        prompt_version=PROMPT_VERSION,
        latency_ms=latency_ms,
        status=result["status"]
    )

    return {
        "metadata": metadata,
        "assistant_result": result
    }
