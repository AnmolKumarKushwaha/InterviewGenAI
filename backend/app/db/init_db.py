"""
=========================================================
File: init_db.py

Purpose:
    Initializes the database during application startup.

Responsibilities:
    - Verify database connectivity
    - Create database tables (development only)
=========================================================
"""

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.core.logger import app_logger
from app.db.base import Base
from app.db.database import engine


# ==========================================================
# Verify Database Connection
# ==========================================================

def check_database_connection() -> None:
    """
    Checks whether PostgreSQL is reachable.
    """

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        app_logger.info("Database connection established successfully.")

    except SQLAlchemyError as exc:
        app_logger.exception("Unable to connect to PostgreSQL.")
        raise exc


# ==========================================================
# Create Tables
# ==========================================================

def create_tables() -> None:
    """
    Creates all tables registered with SQLAlchemy Base.

    NOTE:
    This is intended only for local development.
    In production we will use Alembic migrations.
    """

    Base.metadata.create_all(bind=engine)

    app_logger.info("Database tables created successfully.")


# ==========================================================
# Initialize Database
# ==========================================================

def initialize_database() -> None:
    """
    Performs complete database initialization.
    """

    check_database_connection()

    create_tables()

    app_logger.info("Database initialization completed.")