"""
=========================================================
File: base.py

Purpose:
    Defines the Base class that every database model
    inherits from.

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

        class Resume(Base):
            ...

    """
    pass