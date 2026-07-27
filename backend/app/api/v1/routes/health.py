"""
Health Check API

Used by monitoring systems and load balancers
to verify that the backend is running.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/")
async def health_check():
    """
    Simple health check endpoint.
    """

    return {
        "status": "healthy",
        "message": "InterviewGenAI Backend is running."
    }