from fastapi import FastAPI

app = FastAPI(
    title="CodeArchitect API",
    description="Backend API and AI orchestration service for the CodeArchitect platform.",
    version="0.1.0",
)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Welcome to the CodeArchitect API!"}


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        "service": "codearchitect-api",
        "version": "0.1.0",
    }
