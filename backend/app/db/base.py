"""
=========================================================
File: base.py

Purpose:
    Defines the Base class that every database model
    inherits from.

=========================================================
"""

from sqlalchemy.orm import DeclarativeBase


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