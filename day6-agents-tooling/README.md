# Day 6 - Agents and Tooling for LLMOps

## Project Goal

This project is part of my LLMOps / AI DevOps self-training program.

The goal of Day 6 is to build a light AI DevOps Agent that can route user requests to approved operational tools.

This demonstrates how AI applications can safely interact with existing DevOps systems such as logs, monitoring tools, ticketing systems, and Kubernetes troubleshooting workflows.

## What This Project Does

This FastAPI application exposes an AI DevOps Agent API.

The agent receives a user request, analyzes the request, selects the correct tool, runs the tool, and returns a structured response.

The current project uses simulated tools for training purposes. In production, these tools could be replaced with real integrations such as AWS CloudWatch, Jira, ServiceNow, GitHub Issues, Kubernetes APIs, Datadog, Splunk, or OpenSearch.

## API Endpoints

### GET /health

Confirms that the service is running.

Example response:

```json
{
  "status": "healthy",
  "service": "day6-agents-tooling"
}