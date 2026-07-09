# Day 5 - Production Observability for LLMOps

## Project Goal

This project is part of my LLMOps / AI DevOps self-training program.

The goal of Day 5 is to add production-style observability to an AI application. This helps track whether the application is healthy, reliable, fast, and cost-efficient.

## What This Project Does

This FastAPI application simulates an LLM chat endpoint and records operational metrics for each request.

The API tracks request ID, endpoint name, model name, prompt version, response latency, token usage, estimated cost, request status, errors, structured JSON logs, and aggregated metrics.

## API Endpoints

### GET /health

Confirms that the service is running.

### GET /metrics

Returns operational metrics for the service.

Example response:

```json
{
  "total_requests": 2,
  "successful_requests": 2,
  "failed_requests": 0,
  "total_prompt_tokens": 52,
  "total_completion_tokens": 46,
  "total_estimated_cost": 0.000036,
  "last_latency_ms": 1
}