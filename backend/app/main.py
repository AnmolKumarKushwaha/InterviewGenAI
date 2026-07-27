"""
Main entry point of InterviewGenAI.

Starts the FastAPI application,
registers routes,
and initializes shared resources.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.api import api_router
from app.core.config import settings
from app.core.logger import app_logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Runs once when the application starts
    and once when it shuts down.
    """

    app_logger.info("Starting InterviewGenAI Backend...")

    # Future startup tasks:
    # - Check PostgreSQL connection
    # - Check Redis connection
    # - Check Qdrant connection
    # - Load AI models if needed

    yield

    app_logger.info("Stopping InterviewGenAI Backend...")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan,
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    """
    Root endpoint.
    """

    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }