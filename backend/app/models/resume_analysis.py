from uuid import uuid4

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base


class ResumeAnalysis(Base):

    __tablename__ = "resume_analysis"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    resume_id: Mapped[str] = mapped_column(
        ForeignKey(
            "resumes.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        unique=True,
    )

    extracted_skills: Mapped[list] = mapped_column(
        JSON,
        default=list,
    )

    extracted_projects: Mapped[list] = mapped_column(
        JSON,
        default=list,
    )

    extracted_experience: Mapped[list] = mapped_column(
        JSON,
        default=list,
    )

    extracted_education: Mapped[list] = mapped_column(
        JSON,
        default=list,
    )

    resume_score: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    missing_skills: Mapped[list] = mapped_column(
        JSON,
        default=list,
    )

    suggestions: Mapped[list] = mapped_column(
        JSON,
        default=list,
    )

    resume = relationship(
        "Resume",
        back_populates="analysis",
    )