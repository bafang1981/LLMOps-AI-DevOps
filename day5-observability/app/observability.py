import json
import uuid
from datetime import datetime, timezone
from typing import Dict, Any

from app.config import (
    MODEL_NAME,
    PROMPT_VERSION,
    COST_PER_1000_PROMPT_TOKENS,
    COST_PER_1000_COMPLETION_TOKENS,
)

METRICS = {
    "total_requests": 0,
    "successful_requests": 0,
    "failed_requests": 0,
    "total_prompt_tokens": 0,
    "total_completion_tokens": 0,
    "total_estimated_cost": 0.0,
    "last_latency_ms": 0,
}


def generate_request_id() -> str:
    return str(uuid.uuid4())


def estimate_cost(prompt_tokens: int, completion_tokens: int) -> float:
    prompt_cost = (prompt_tokens / 1000) * COST_PER_1000_PROMPT_TOKENS
    completion_cost = (completion_tokens / 1000) * COST_PER_1000_COMPLETION_TOKENS
    return round(prompt_cost + completion_cost, 6)


def update_metrics(status, latency_ms, prompt_tokens, completion_tokens, estimated_cost) -> None:
    METRICS["total_requests"] += 1
    METRICS["last_latency_ms"] = latency_ms
    METRICS["total_prompt_tokens"] += prompt_tokens
    METRICS["total_completion_tokens"] += completion_tokens
    METRICS["total_estimated_cost"] = round(METRICS["total_estimated_cost"] + estimated_cost, 6)

    if status == "success":
        METRICS["successful_requests"] += 1
    else:
        METRICS["failed_requests"] += 1


def create_log_event(
    request_id: str,
    endpoint: str,
    status: str,
    latency_ms: int,
    prompt_tokens: int,
    completion_tokens: int,
    estimated_cost: float,
    error: str | None = None,
) -> Dict[str, Any]:
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "request_id": request_id,
        "endpoint": endpoint,
        "model": MODEL_NAME,
        "prompt_version": PROMPT_VERSION,
        "latency_ms": latency_ms,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "estimated_cost": estimated_cost,
        "status": status,
        "error": error,
    }


def write_structured_log(event: Dict[str, Any]) -> None:
    print(json.dumps(event))
