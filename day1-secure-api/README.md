# Day 1 - Secure LLM API Integration

## Project Goal

This project is part of my LLMOps / AI DevOps self-training program.

The goal of Day 1 is to build a secure backend API that connects to an LLM provider using production-style DevOps practices.

## What This Project Does

This FastAPI application exposes two endpoints:

- GET /health
- POST /ask

The /health endpoint confirms that the service is running.

The /ask endpoint accepts a user question, sends it to an LLM model, and returns a structured JSON response.

## Skills Practiced

- FastAPI backend development
- Secure LLM API integration
- Environment variable management
- Secret protection using .env
- System prompt design
- Structured JSON responses
- Error handling
- Logging
- Latency tracking
- Swagger UI testing

## How to Run Locally

1. Activate the virtual environment:

source venv/Scripts/activate

2. Install dependencies:

pip install -r requirements.txt

3. Create a .env file:

OPENAI_API_KEY=your_api_key_here
LLM_MODEL=gpt-4.1-mini

4. Run the API:

python -m uvicorn main:app --reload

5. Open Swagger UI:

http://127.0.0.1:8000/docs

## DevOps Notes

This project treats the LLM API key like a production secret. In production, the key should be stored in AWS Secrets Manager, Parameter Store, GitHub Actions Secrets, Jenkins Credentials, or Kubernetes Secrets.

## Interview Summary

I built a secure LLM API integration using Python and FastAPI. The service loads the API key from an environment file, calls an LLM provider, returns structured JSON, tracks latency, logs requests, and includes a health check endpoint.
