from fastapi import FastAPI

app = FastAPI(
    title="Day 4 LLMOps CI/CD API",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "day4-cicd-llmops"
    }

@app.get("/")
def root():
    return {
        "message": "LLMOps CI/CD pipeline is running"
    }
