"""
=========================================================
File: helpers.py

Purpose:
    Contains generic helper functions that can be reused
    across the application.
=========================================================
"""

from datetime import datetime, timezone
from uuid import uuid4


# ==========================================================
# Generate UUID
# ==========================================================

def generate_uuid() -> str:
    """
    Returns a random UUID string.
    """

    return uuid4().hex


# ==========================================================
# Current UTC Time
# ==========================================================

def get_current_utc_time() -> datetime:
    """
    Returns the current UTC datetime.
    """

    return datetime.now(timezone.utc)


# ==========================================================
# Datetime to ISO Format
# ==========================================================

def datetime_to_iso(dt: datetime) -> str:
    """
    Converts datetime into ISO-8601 format.
    """

    return dt.isoformat()


# ==========================================================
# Human Readable File Size
# ==========================================================

def format_file_size(size_in_bytes: int) -> str:
    """
    Converts bytes into a human-readable string.
    """

    units = ["B", "KB", "MB", "GB", "TB"]

    size = float(size_in_bytes)

    for unit in units:
        if size < 1024 or unit == units[-1]:
            return f"{size:.2f} {unit}"

        size /= 1024