from fastapi import FastAPI
from app.api import router
from app.core.config import settings

app = FastAPI(
    title="Self LLM Backend",
    description="Backend API for local LLM integration and example prompts.",
    version="0.1.0",
)

app.include_router(router, prefix="/api")

@app.get("/health", summary="Health check")
async def health_check() -> dict:
    return {"status": "ok", "app": "self-llm-backend", "environment": settings.environment}
