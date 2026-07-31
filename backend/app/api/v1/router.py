from fastapi import APIRouter

from app.api.v1.auth import router as auth_router
from app.api.v1.resume import router as resume_router
from app.api.v1.job import router as job_router
from app.api.v1.skill_gap import router as skill_gap_router

api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(resume_router)
api_router.include_router(job_router)
api_router.include_router(skill_gap_router)