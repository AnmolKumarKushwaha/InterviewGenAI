"""
Main API Router

Collects all API routes in one place.
"""

from fastapi import APIRouter

from app.api.v1.routes.health import router as health_router

api_router = APIRouter()

api_router.include_router(health_router)