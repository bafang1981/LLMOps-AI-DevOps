from app.tools import (
    analyze_incident_logs,
    check_cloudwatch_alarm,
    create_jira_ticket,
    summarize_kubernetes_error,
)


def run_agent(user_request: str) -> dict:
    request = user_request.lower()

    if not request.strip():
        return {
            "status": "failed",
            "message": "User request cannot be empty."
        }

    if "cloudwatch" in request or "alarm" in request:
        result = check_cloudwatch_alarm("HighLatencyAlarm")
        return {
            "status": "success",
            "selected_tool": "check_cloudwatch_alarm",
            "result": result
        }

    if (
        "kubernetes" in request
        or "pod" in request
        or "crashloopbackoff" in request
        or "imagepullbackoff" in request
    ):
        result = summarize_kubernetes_error(user_request)
        return {
            "status": "success",
            "selected_tool": "summarize_kubernetes_error",
            "result": result
        }

    if "ticket" in request or "jira" in request:
        result = create_jira_ticket(
            title="Production incident investigation",
            description=user_request,
            severity="medium"
        )
        return {
            "status": "success",
            "selected_tool": "create_jira_ticket",
            "result": result
        }

    if "slow" in request or "latency" in request or "error" in request or "incident" in request:
        result = analyze_incident_logs("checkout-api")
        return {
            "status": "success",
            "selected_tool": "analyze_incident_logs",
            "result": result
        }

    return {
        "status": "success",
        "selected_tool": "none",
        "result": {
            "message": "No tool was required. Ask about logs, latency, incidents, CloudWatch alarms, Jira tickets, or Kubernetes errors."
        }
    }
