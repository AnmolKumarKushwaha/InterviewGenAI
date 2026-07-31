"""
=========================================================
User Model

Stores registered users.

=========================================================
"""

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.base import Base


class User(Base):

    __tablename__ = "users"

    # -----------------------------------------------------
    # Primary Key
    # -----------------------------------------------------

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    # -----------------------------------------------------
    # User Details
    # -----------------------------------------------------

    full_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    # -----------------------------------------------------
    # Status
    # -----------------------------------------------------

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    # -----------------------------------------------------
    # Audit Fields
    # -----------------------------------------------------

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    
    resumes = relationship(
    "Resume",
    back_populates="user",
    cascade="all, delete-orphan",
    )
    
    
    job_descriptions = relationship(
    "JobDescription",
    back_populates="user",
    )