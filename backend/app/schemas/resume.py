"""
=========================================================
File: resume.py

Purpose:
    Pydantic schemas for Resume module.

=========================================================
"""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


# =========================================================
# Upload Response
# =========================================================

class ResumeUploadResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str
    title: str
    status: str
    created_at: datetime


# =========================================================
# Resume Details
# =========================================================

class ResumeResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str
    user_id: str
    title: str
    status: str
    created_at: datetime
    updated_at: datetime


# =========================================================
# Resume Analysis
# =========================================================

class ResumeAnalysisResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    resume_score: int

    skills: dict
    projects: dict
    experience: dict
    education: dict
    certifications: dict

    missing_skills: dict
    strengths: dict
    suggestions: dict

    analysis_json: dict

    created_at: datetime