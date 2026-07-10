import time
import uuid
from datetime import datetime, timezone


def generate_request_id() -> str:
    return str(uuid.uuid4())


def current_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def calculate_latency_ms(start_time: float) -> int:
    return int((time.time() - start_time) * 1000)


def build_observability_metadata(
    request_id: str,
    endpoint: str,
    model: str,
    prompt_version: str,
    latency_ms: int,
    status: str
) -> dict:
    return {
        "timestamp": current_timestamp(),
        "request_id": request_id,
        "endpoint": endpoint,
        "model": model,
        "prompt_version": prompt_version,
        "latency_ms": latency_ms,
        "status": status
    }
