"""
=========================================================
File: logger.py

Purpose:
    Configure a centralized logger for the entire project.

Why?

Instead of using print() statements throughout the code,
every module will import this logger and write structured
logs.

Example:

    logger.info("Resume uploaded successfully")

=========================================================
"""

from pathlib import Path

from loguru import logger

# =========================================================
# Create logs directory if it doesn't already exist
# =========================================================

LOG_DIRECTORY = Path("logs")
LOG_DIRECTORY.mkdir(exist_ok=True)

LOG_FILE = LOG_DIRECTORY / "application.log"

# =========================================================
# Remove Loguru's default logger
# =========================================================

logger.remove()

# =========================================================
# Console Logger
# =========================================================

logger.add(
    sink=lambda message: print(message, end=""),
    level="INFO",
    colorize=True,
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan> | "
        "<level>{message}</level>"
    ),
)

# =========================================================
# File Logger
# =========================================================

logger.add(
    LOG_FILE,
    rotation="10 MB",
    retention="10 days",
    compression="zip",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name} | {message}",
)

# =========================================================
# Export Logger
# =========================================================

app_logger = logger