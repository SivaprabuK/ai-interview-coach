from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.exception_handlers import register_exception_handlers

app = FastAPI(
    title=settings.app_name,
    description="An AI-powered platform for interview preparation",
    version=settings.app_version,
)

register_exception_handlers(app)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Interview Coach!",
        "status": "running",
    }
