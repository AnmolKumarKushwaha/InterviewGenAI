"""
=========================================================
File: api.py

Purpose:
    Central API router.
    Registers all version 1 endpoints.

=========================================================
"""

from fastapi import APIRouter

from app.api.v1.endpoints.auth import router as auth_router


api_router = APIRouter()


# ==========================================================
# Authentication Routes
# ==========================================================

api_router.include_router(
    auth_router,
)