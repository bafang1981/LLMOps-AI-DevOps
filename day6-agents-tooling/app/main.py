from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.agent import run_agent


app = FastAPI(
    title="Day 6 AI DevOps Agent",
    version="1.0.0"
)


class AgentRequest(BaseModel):
    request: str


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "day6-agents-tooling"
    }


@app.post("/agent")
def agent_endpoint(payload: AgentRequest):
    if not payload.request.strip():
        raise HTTPException(status_code=400, detail="Request cannot be empty.")

    return run_agent(payload.request)
