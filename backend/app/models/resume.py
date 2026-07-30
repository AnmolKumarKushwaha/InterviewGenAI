from datetime import datetime
from datetime import timezone
from uuid import uuid4

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base


class Resume(Base):

    __tablename__ = "resumes"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
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

    file_size: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    mime_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )

    user = relationship(
        "User",
        back_populates="resumes",
    )
    
    extracted_text: Mapped[str | None] = mapped_column(
    Text,
    nullable=True,
    )
    


    analysis = relationship(
        "ResumeAnalysis",
        back_populates="resume",
        uselist=False,
        cascade="all, delete-orphan",
    )
    
    analysis = relationship(
        "ResumeAnalysis",

        back_populates="resume",

        uselist=False,

        cascade="all, delete-orphan",
    )