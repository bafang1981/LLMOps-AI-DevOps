import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.observability import (
    METRICS,
    generate_request_id,
    estimate_cost,
    update_metrics,
    create_log_event,
    write_structured_log,
)
from app.config import MODEL_NAME, PROMPT_VERSION


app = FastAPI(
    title="Day 5 LLMOps Observability API",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    question: str


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "day5-observability"
    }


@app.get("/metrics")
def get_metrics():
    return METRICS


@app.post("/chat")
def chat(request: ChatRequest):
    request_id = generate_request_id()
    start_time = time.time()

    if not request.question.strip():
        latency_ms = int((time.time() - start_time) * 1000)
        estimated_cost = 0.0

        update_metrics("failed", latency_ms, 0, 0, estimated_cost)

        log_event = create_log_event(
            request_id=request_id,
            endpoint="/chat",
            status="failed",
            latency_ms=latency_ms,
            prompt_tokens=0,
            completion_tokens=0,
            estimated_cost=estimated_cost,
            error="Question cannot be empty."
        )
        write_structured_log(log_event)

        raise HTTPException(status_code=400, detail="Question cannot be empty.")

    simulated_answer = (
        "This is a simulated LLM response. In production, this endpoint would call "
        "an LLM provider and record real token usage, latency, and cost."
    )

    prompt_tokens = len(request.question.split()) + 20
    completion_tokens = len(simulated_answer.split())
    estimated_cost = estimate_cost(prompt_tokens, completion_tokens)
    latency_ms = int((time.time() - start_time) * 1000)

    update_metrics("success", latency_ms, prompt_tokens, completion_tokens, estimated_cost)

    log_event = create_log_event(
        request_id=request_id,
        endpoint="/chat",
        status="success",
        latency_ms=latency_ms,
        prompt_tokens=prompt_tokens,
        completion_tokens=completion_tokens,
        estimated_cost=estimated_cost,
    )
    write_structured_log(log_event)

    return {
        "request_id": request_id,
        "answer": simulated_answer,
        "model": MODEL_NAME,
        "prompt_version": PROMPT_VERSION,
        "latency_ms": latency_ms,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "estimated_cost": estimated_cost,
        "status": "success"
    }
