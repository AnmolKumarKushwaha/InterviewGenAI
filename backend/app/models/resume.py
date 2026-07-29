"""
=========================================================
File: resume.py

Purpose:
    SQLAlchemy model for uploaded resumes.

=========================================================
"""

import uuid
from datetime import datetime
from datetime import timezone

from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.core.enums import ResumeStatus
from app.db.base import Base


class Resume(Base):
    """
    Resume table.
    """

    __tablename__ = "resumes"

    # =====================================================
    # Primary Key
    # =====================================================

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    # =====================================================
    # Foreign Keys
    # =====================================================

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    # =====================================================
    # Resume Information
    # =====================================================

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    status: Mapped[ResumeStatus] = mapped_column(
        Enum(ResumeStatus),
        default=ResumeStatus.UPLOADED,
        nullable=False,
    )

    # =====================================================
    # Timestamps
    # =====================================================

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # =====================================================
    # Relationships
    # =====================================================

    user = relationship(
        "User",
        back_populates="resumes",
    )

    versions = relationship(
        "ResumeVersion",
        back_populates="resume",
        cascade="all, delete-orphan",
    )