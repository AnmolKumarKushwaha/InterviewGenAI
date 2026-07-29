"""
=========================================================
File: resume_version.py

Purpose:
    SQLAlchemy model for resume versions.

=========================================================
"""

import uuid
from datetime import datetime
from datetime import timezone

from sqlalchemy import BigInteger
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base


class ResumeVersion(Base):

    __tablename__ = "resume_versions"

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

    resume_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "resumes.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    # =====================================================
    # Version Information
    # =====================================================

    version_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    original_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    stored_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    file_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    mime_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    file_size: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # =====================================================
    # Relationships
    # =====================================================

    resume = relationship(
        "Resume",
        back_populates="versions",
    )

    analysis = relationship(
        "ResumeAnalysis",
        back_populates="resume_version",
        uselist=False,
        cascade="all, delete-orphan",
    )