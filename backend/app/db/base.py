"""
=========================================================
SQLAlchemy Base Class

Every ORM model inherits this Base.

=========================================================
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from app.models.user import User
from app.models.resume import Resume
from app.models.resume_analysis import ResumeAnalysis