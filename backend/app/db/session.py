"""
=========================================================
File: session.py

Purpose:
    Creates database sessions for every API request.

=========================================================
"""

from sqlalchemy.orm import sessionmaker, Session

from app.db.database import engine

# ==========================================================
# Session Factory
# ==========================================================

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


def get_db():
    """
    FastAPI dependency.

    Creates a new database session for every request
    and closes it automatically after the request
    completes.
    """

    db: Session = SessionLocal()

    try:
        yield db

    finally:
        db.close()