"""
=========================================================
File: config.py

Purpose:
    Loads all application configurations from the .env file.

Why do we need this?

Instead of writing:

    os.getenv("DATABASE_URL")

inside every file, we load all configurations once
and access them anywhere in the project using:

    from app.core.config import settings

=========================================================
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    This class represents all environment variables used
    throughout the application.

    Every variable here is automatically loaded
    from the .env file.
    """

    # =====================================================
    # Application Settings
    # =====================================================

    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    # =====================================================
    # Database
    # =====================================================

    DATABASE_URL: str

    # =====================================================
    # JWT Authentication
    # =====================================================

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # =====================================================
    # OpenAI
    # =====================================================

    OPENAI_API_KEY: str

    # =====================================================
    # Qdrant
    # =====================================================

    QDRANT_URL: str
    QDRANT_API_KEY: str = ""
    QDRANT_COLLECTION: str

    # =====================================================
    # Redis
    # =====================================================

    REDIS_URL: str

    # =====================================================
    # Pydantic Configuration
    # =====================================================

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True
    )


@lru_cache
def get_settings() -> Settings:
    """
    Creates only one Settings object.

    Why?

    Reading the .env file every time
    is unnecessary.

    lru_cache ensures the Settings object
    is created only once and reused
    throughout the application.
    """

    return Settings()


# =========================================================
# Global Settings Object
# =========================================================

settings = get_settings()