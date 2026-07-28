from uuid import uuid4

from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import DateTime

from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped

from datetime import datetime
from datetime import timezone

from app.db.base import Base


class ResumeAnalysis(Base):

    __tablename__ = "resume_analysis"


    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4())
    )


    resume_version_id: Mapped[str] = mapped_column(
        ForeignKey(
            "resume_versions.id",
            ondelete="CASCADE"
        )
    )


    resume_score: Mapped[int] = mapped_column(
        Integer
    )


    skills: Mapped[dict] = mapped_column(
        JSON
    )


    projects: Mapped[dict] = mapped_column(
        JSON
    )


    experience: Mapped[dict] = mapped_column(
        JSON
    )


    education: Mapped[dict] = mapped_column(
        JSON
    )


    certifications: Mapped[dict] = mapped_column(
        JSON
    )


    missing_skills: Mapped[dict] = mapped_column(
        JSON
    )


    strengths: Mapped[dict] = mapped_column(
        JSON
    )


    suggestions: Mapped[dict] = mapped_column(
        JSON
    )


    analysis_json: Mapped[dict] = mapped_column(
        JSON
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )


    resume_version = relationship(
        "ResumeVersion",
        back_populates="analysis"
    )