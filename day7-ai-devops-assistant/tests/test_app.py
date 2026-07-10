from fastapi.testclient import TestClient

from app.main import app
from app.agent import run_ai_devops_assistant

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_chat_knowledge_mode():
    response = client.post("/chat", json={"request": "What is LLMOps?"})
    assert response.status_code == 200
    data = response.json()
    assert data["assistant_result"]["mode"] == "knowledge"


def test_chat_incident_tool():
    response = client.post("/chat", json={"request": "The checkout API is slow with high latency."})
    assert response.status_code == 200
    data = response.json()
    assert data["assistant_result"]["selected_tool"] == "analyze_incident"


def test_chat_kubernetes_tool():
    response = client.post("/chat", json={"request": "Kubernetes pod is in CrashLoopBackOff."})
    assert response.status_code == 200
    data = response.json()
    assert data["assistant_result"]["selected_tool"] == "summarize_kubernetes_issue"


def test_agent_ticket_tool():
    result = run_ai_devops_assistant("Create an incident ticket for production error.")
    assert result["selected_tool"] == "create_incident_ticket"
