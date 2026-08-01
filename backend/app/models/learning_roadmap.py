from uuid import uuid4

from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import JSON

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.base import Base


class LearningRoadmap(Base):

    __tablename__ = "learning_roadmap"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    resume_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
    )

    job_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
    )

    duration: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    roadmap: Mapped[list] = mapped_column(
        JSON,
        nullable=False,
    )

    ai_summary: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )