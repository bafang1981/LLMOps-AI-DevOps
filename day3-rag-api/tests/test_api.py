from fastapi.testclient import TestClient

import main

client = TestClient(main.app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "running"


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_ask_endpoint_with_mock(monkeypatch):
    def mock_ask_rag_question(question: str) -> str:
        return "Mocked RAG answer for testing."

    monkeypatch.setattr(main, "ask_rag_question", mock_ask_rag_question)

    response = client.post("/ask", json={"question": "What is LLMOps?"})

    assert response.status_code == 200
    data = response.json()
    assert data["question"] == "What is LLMOps?"
    assert data["answer"] == "Mocked RAG answer for testing."
