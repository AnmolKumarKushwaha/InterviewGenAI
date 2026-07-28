from uuid import uuid4

from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import BigInteger
from sqlalchemy import DateTime

from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped

from datetime import datetime
from datetime import timezone

from app.db.base import Base


class ResumeVersion(Base):

    __tablename__ = "resume_versions"


    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4())
    )


    resume_id: Mapped[str] = mapped_column(
        ForeignKey(
            "resumes.id",
            ondelete="CASCADE"
        )
    )


    version_number: Mapped[int] = mapped_column(
        Integer
    )


    original_filename: Mapped[str] = mapped_column(
        String(255)
    )


    stored_filename: Mapped[str] = mapped_column(
        String(255)
    )


    file_path: Mapped[str] = mapped_column(
        String(500)
    )


    mime_type: Mapped[str] = mapped_column(
        String(100)
    )


    file_size: Mapped[int] = mapped_column(
        BigInteger
    )


    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )


    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )


    resume = relationship(
        "Resume",
        back_populates="versions"
    )


    analysis = relationship(
        "ResumeAnalysis",
        back_populates="resume_version",
        uselist=False,
        cascade="all, delete-orphan"
    )