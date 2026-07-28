"""
=========================================================
File: base.py

Purpose:
    Defines the SQLAlchemy Declarative Base class.
    Every ORM model inherits from this Base.

=========================================================
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy models.

    Example:

        class User(Base):
            ...

    """
    pass