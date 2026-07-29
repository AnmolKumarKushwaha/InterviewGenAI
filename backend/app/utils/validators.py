"""
=========================================================
File: validators.py

Purpose:
    Common validation utilities used across the project.
=========================================================
"""

from pathlib import Path
import re
from fastapi import HTTPException

from app.core.constants import (
    ALLOWED_RESUME_EXTENSIONS,
    MAX_RESUME_SIZE_MB,
)

# ==========================================================
# Email Validation
# ==========================================================

EMAIL_REGEX = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)


def validate_email(email: str) -> bool:
    """
    Returns True if email format is valid.
    """

    return bool(EMAIL_REGEX.fullmatch(email))


# ==========================================================
# Password Validation
# ==========================================================

def validate_password(password: str) -> bool:
    """
    Password Rules

    - Minimum 8 characters
    - One uppercase letter
    - One lowercase letter
    - One digit
    """

    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"\d", password):
        return False

    return True


# ==========================================================
# Resume File Extension
# ==========================================================

def validate_resume_extension(filename: str) -> bool:
    """
    Checks whether uploaded resume format is supported.
    """

    extension = Path(filename).suffix.lower()

    return extension in ALLOWED_RESUME_EXTENSIONS


# ==========================================================
# Resume File Size
# ==========================================================

def validate_file_size(file_size: int) -> bool:
    """
    file_size should be provided in bytes.
    """

    max_size = MAX_RESUME_SIZE_MB * 1024 * 1024

    return file_size <= max_size


# ==========================================================
# Job Description Validation
# ==========================================================

def validate_job_description_extension(
    filename: str,
) -> bool:
    """
    Job descriptions support the same formats as resumes.
    """

    return validate_resume_extension(filename)


# ==========================================================
# Resume Upload Validation
# ==========================================================

def validate_resume_file(
    filename: str,
    file_size: int,
) -> None:
    """
    Validates uploaded resume.
    """

    if not validate_resume_extension(filename):
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are allowed.",
        )

    if not validate_file_size(file_size):
        raise HTTPException(
            status_code=400,
            detail="File exceeds maximum allowed size.",
        )