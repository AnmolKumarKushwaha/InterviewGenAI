from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import JSON
from sqlalchemy import String

from sqlalchemy.orm import relationship

from app.db.base import Base


class JobAnalysis(Base):

    __tablename__ = "job_analysis"

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    job_id = Column(
        String(36),
        ForeignKey(
            "job_descriptions.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        unique=True,
    )

    required_skills = Column(
        JSON,
        nullable=False,
        default=list,
    )

    preferred_skills = Column(
        JSON,
        nullable=False,
        default=list,
    )

    responsibilities = Column(
        JSON,
        nullable=False,
        default=list,
    )

    experience = Column(
        String(100),
        nullable=True,
    )

    education = Column(
        String(255),
        nullable=True,
    )

    location = Column(
        String(255),
        nullable=True,
    )

    job = relationship(
        "JobDescription",
        back_populates="analysis",
    )