"""
=========================================================
File: base.py

Purpose:
    Defines the SQLAlchemy Declarative Base class.
    Every ORM model inherits from this Base.

=========================================================
"""

from sqlalchemy.orm import DeclarativeBase
# from app.db.database import Base

# Import all models here
# from app.models.user import User
# from app.models.resume import Resume
# from app.models.interview import Interview

class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy models.

    Example:

        class User(Base):
            ...

    """
    pass