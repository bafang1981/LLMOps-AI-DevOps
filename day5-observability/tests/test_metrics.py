from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    data = response.json()
    assert "total_requests" in data
    assert "successful_requests" in data
    assert "failed_requests" in data


def test_chat_success():
    response = client.post("/chat", json={"question": "Why is observability important for LLMOps?"})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "request_id" in data
    assert "latency_ms" in data
    assert "estimated_cost" in data
