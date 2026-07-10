def analyze_incident(service_name: str) -> dict:
    return {
        "tool": "analyze_incident",
        "service_name": service_name,
        "summary": f"{service_name} is showing high latency and elevated error rates.",
        "possible_causes": [
            "Recent deployment issue",
            "Database connection exhaustion",
            "Upstream dependency timeout",
            "Insufficient scaling"
        ],
        "recommended_actions": [
            "Check recent deployments",
            "Review application logs",
            "Check database metrics",
            "Validate autoscaling configuration",
            "Prepare rollback if errors continue"
        ],
        "severity": "high"
    }


def summarize_kubernetes_issue(error_message: str) -> dict:
    lower_error = error_message.lower()

    if "crashloopbackoff" in lower_error:
        cause = "The container is repeatedly crashing after startup."
        action = "Check container logs, environment variables, image version, and startup command."
    elif "imagepullbackoff" in lower_error:
        cause = "Kubernetes cannot pull the container image."
        action = "Verify image name, tag, registry credentials, and network access."
    else:
        cause = "More Kubernetes context is needed."
        action = "Check pod events, deployment status, logs, and cluster resource usage."

    return {
        "tool": "summarize_kubernetes_issue",
        "error_message": error_message,
        "likely_cause": cause,
        "recommended_action": action
    }


def create_incident_ticket(description: str) -> dict:
    return {
        "tool": "create_incident_ticket",
        "ticket_id": "INC-7001",
        "title": "AI DevOps Assistant Incident Ticket",
        "description": description,
        "status": "created",
        "severity": "medium"
    }
