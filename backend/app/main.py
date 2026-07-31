from fastapi import FastAPI

from app.api.v1.router import api_router
from app.api.v1.job import router as job_router

app = FastAPI(
    title="InterviewGenAI",
)

from app.core.handlers import register_exception_handlers

app.include_router(
    api_router,
    prefix="/api/v1",
)


app.include_router(
    job_router,
    prefix="/api/v1",
)