from uuid import uuid4

from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import Enum

from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from datetime import datetime
from datetime import timezone

from app.db.base import Base
from app.core.enums import ResumeStatus


class Resume(Base):

    __tablename__ = "resumes"


    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4())
    )


    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )


    title: Mapped[str] = mapped_column(
        String(255)
    )


    status: Mapped[ResumeStatus] = mapped_column(
        Enum(ResumeStatus),
        default=ResumeStatus.UPLOADED
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )


    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )


    user = relationship(
        "User",
        back_populates="resumes"
    )


    versions = relationship(
        "ResumeVersion",
        back_populates="resume",
        cascade="all, delete-orphan"
    )