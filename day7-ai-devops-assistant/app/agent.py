from app.rag import search_knowledge_base
from app.tools import (
    analyze_incident,
    summarize_kubernetes_issue,
    create_incident_ticket,
)


def run_ai_devops_assistant(user_request: str) -> dict:
    request = user_request.lower()

    if not request.strip():
        return {
            "status": "failed",
            "mode": "none",
            "message": "Request cannot be empty."
        }

    if "kubernetes" in request or "crashloopbackoff" in request or "imagepullbackoff" in request:
        return {
            "status": "success",
            "mode": "tool",
            "selected_tool": "summarize_kubernetes_issue",
            "result": summarize_kubernetes_issue(user_request)
        }

    if "ticket" in request or "jira" in request or "incident ticket" in request:
        return {
            "status": "success",
            "mode": "tool",
            "selected_tool": "create_incident_ticket",
            "result": create_incident_ticket(user_request)
        }

    if "slow" in request or "latency" in request or "500" in request or "error" in request:
        return {
            "status": "success",
            "mode": "tool",
            "selected_tool": "analyze_incident",
            "result": analyze_incident("checkout-api")
        }

    knowledge_result = search_knowledge_base(user_request)

    return {
        "status": "success",
        "mode": "knowledge",
        "selected_tool": "local_knowledge_search",
        "result": knowledge_result
    }
