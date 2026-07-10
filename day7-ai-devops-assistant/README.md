# Day 7 - AI DevOps Assistant Capstone

## Project Goal

This project is the final capstone for my 1-week LLMOps / AI DevOps self-training program.

The goal is to combine the main concepts from the previous days into one production-style AI DevOps Assistant.

## What This Application Does

The Day 7 AI DevOps Assistant exposes a FastAPI backend with a /chat endpoint.

The assistant receives a DevOps-related request and decides whether to:

1. Answer from a local knowledge base
2. Route the request to an incident analysis tool
3. Route the request to a Kubernetes troubleshooting tool
4. Route the request to an incident ticket creation tool

Each response includes observability metadata such as request ID, timestamp, endpoint, model name, prompt version, latency, and status.

## API Endpoints

### GET /health

Checks whether the service is running.

Example response:

{
  "status": "healthy",
  "service": "day7-ai-devops-assistant"
}

### POST /chat

Receives a DevOps request and returns either a knowledge-based answer or a tool-based response.

Example request:

{
  "request": "The checkout API is slow with high latency."
}

Expected selected tool:

analyze_incident

## Main Features

### Knowledge Mode

The assistant can search a local DevOps knowledge file and return relevant context.

Example:

{
  "request": "What is LLMOps?"
}

Expected mode:

knowledge

### Incident Analysis Tool

The assistant detects latency, errors, or production incident language and routes the request to an incident analysis tool.

Expected tool:

analyze_incident

### Kubernetes Troubleshooting Tool

The assistant detects Kubernetes issues such as CrashLoopBackOff or ImagePullBackOff.

Expected tool:

summarize_kubernetes_issue

### Incident Ticket Tool

The assistant can simulate creating an incident ticket.

Expected tool:

create_incident_ticket

## Project Structure

day7-ai-devops-assistant/
├── app/
│   ├── __init__.py
│   ├── agent.py
│   ├── config.py
│   ├── main.py
│   ├── observability.py
│   ├── rag.py
│   └── tools.py
├── data/
│   └── devops_knowledge.txt
├── logs/
├── prompts/
│   └── system_prompt_v1.txt
├── tests/
│   └── test_app.py
├── requirements.txt
├── pytest.ini
├── README.md
└── .gitignore

## How to Run Locally

Create and activate the virtual environment:

python -m venv venv
source venv/Scripts/activate

Install dependencies:

pip install -r requirements.txt

Run tests:

python -m pytest

Expected result:

5 passed

Run the API:

python -m uvicorn app.main:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs

## Skills Practiced

- LLMOps architecture
- AI DevOps assistant design
- FastAPI backend development
- Agent and tool routing
- RAG-style knowledge lookup
- Incident response automation
- Kubernetes troubleshooting automation
- Observability metadata
- Prompt version tracking
- Request tracing
- Automated testing
- GitHub portfolio project development

## Interview Summary

In this capstone project, I built an AI DevOps Assistant using Python and FastAPI. The assistant exposes a /chat endpoint that can either answer from a local DevOps knowledge base or route the request to approved DevOps tools. I implemented simulated tools for incident analysis, Kubernetes troubleshooting, and incident ticket creation. I also added production-style observability metadata, including request ID, timestamp, latency, model name, prompt version, and status. Finally, I validated the application using Pytest.

## Resume Bullet

Built a production-style AI DevOps Assistant using Python and FastAPI with RAG-style knowledge lookup, agent/tool routing, incident analysis, Kubernetes troubleshooting, incident ticket simulation, observability metadata, and automated Pytest validation.

## 1-Week Program Completed

- Day 1: Secure LLM API integration
- Day 2: RAG pipeline
- Day 3: Production RAG API
- Day 4: CI/CD and evaluation gates
- Day 5: Observability and metrics
- Day 6: Agents and tooling
- Day 7: AI DevOps Assistant capstone
