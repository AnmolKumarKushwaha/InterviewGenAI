"""
=========================================================
File: resume_repository.py

Purpose:
    Database operations for Resume models.

=========================================================
"""

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.resume import Resume


class ResumeRepository:

    def __init__(
        self,
        db: Session,
    ):

        self.db = db


    # =====================================================
    # Create Resume
    # =====================================================

    def create(
        self,
        resume: Resume,
    ):

        self.db.add(resume)

        self.db.commit()

        self.db.refresh(resume)

        return resume


    # =====================================================
    # Get Resume by ID
    # =====================================================

    def get_by_id(
        self,
        resume_id: str,
    ):

        return self.db.scalar(
            select(Resume).where(
                Resume.id == resume_id
            )
        )


    # =====================================================
    # Get all resumes of a user
    # =====================================================

    def get_by_user(
        self,
        user_id: UUID,
    ):

        return list(
            self.db.scalars(
                select(Resume).where(
                    Resume.user_id == user_id
                )
            )
        )


    # =====================================================
    # Update Resume
    # =====================================================

    def update(
        self,
        resume: Resume,
    ):

        self.db.commit()

        self.db.refresh(resume)

        return resume


    # =====================================================
    # Delete Resume
    # =====================================================

    def delete(
        self,
        resume: Resume,
    ):

        self.db.delete(resume)

        self.db.commit()