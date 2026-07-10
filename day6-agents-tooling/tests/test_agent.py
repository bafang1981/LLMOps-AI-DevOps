from fastapi.testclient import TestClient

from app.agent import run_agent
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_latency_routes_to_incident_tool():
    result = run_agent("The checkout API is slow and has high latency.")
    assert result["status"] == "success"
    assert result["selected_tool"] == "analyze_incident_logs"


def test_cloudwatch_routes_to_alarm_tool():
    result = run_agent("Check the CloudWatch alarm for high latency.")
    assert result["status"] == "success"
    assert result["selected_tool"] == "check_cloudwatch_alarm"


def test_kubernetes_routes_to_kubernetes_tool():
    result = run_agent("Kubernetes pod is in CrashLoopBackOff.")
    assert result["status"] == "success"
    assert result["selected_tool"] == "summarize_kubernetes_error"


def test_jira_routes_to_ticket_tool():
    result = run_agent("Create a Jira ticket for this production issue.")
    assert result["status"] == "success"
    assert result["selected_tool"] == "create_jira_ticket"


def test_agent_endpoint():
    response = client.post("/agent", json={"request": "The API has high latency."})
    assert response.status_code == 200
    assert response.json()["status"] == "success"
