from fastapi import FastAPI

from app.api.v1.router import api_router

app = FastAPI(
    title="InterviewGenAI",
)

from app.core.handlers import register_exception_handlers

app.include_router(
    api_router,
    prefix="/api/v1",
)