"""
=========================================================
File: database.py

Purpose:
    Creates the SQLAlchemy Engine used to communicate
    with the PostgreSQL database.

=========================================================
"""

from sqlalchemy import create_engine

from app.core.config import settings
from app.core.logger import app_logger

engine = create_engine(
    settings.DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_recycle=1800,
    pool_pre_ping=True,
    echo=False,
)

app_logger.info("PostgreSQL Engine initialized successfully.")