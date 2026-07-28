"""
=========================================================
File: base.py

Purpose:
    Defines the SQLAlchemy Declarative Base class.

=========================================================
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy models.
    """
    pass


# =========================================================
# Import ALL models AFTER Base is defined
# =========================================================

from app.models.user import User
from app.models.resume import Resume
from app.models.resume_version import ResumeVersion
from app.models.resume_analysis import ResumeAnalysis