"""
=========================================================
File: resume_analysis.py

Purpose:
    SQLAlchemy model for AI resume analysis.

=========================================================
"""

import uuid
from datetime import datetime
from datetime import timezone

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base


class ResumeAnalysis(Base):

    __tablename__ = "resume_analysis"

    # =====================================================
    # Primary Key
    # =====================================================

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    # =====================================================
    # Foreign Key
    # =====================================================

    resume_version_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "resume_versions.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    # =====================================================
    # Analysis Results
    # =====================================================

    resume_score: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    skills: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
    )

    projects: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
    )

    experience: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
    )

    education: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
    )

    certifications: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
    )

    missing_skills: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
    )

    strengths: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
    )

    suggestions: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
    )

    analysis_json: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
    )

    # =====================================================
    # Timestamp
    # =====================================================

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # =====================================================
    # Relationships
    # =====================================================

    resume_version = relationship(
        "ResumeVersion",
        back_populates="analysis",
    )