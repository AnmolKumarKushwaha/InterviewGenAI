"""
=========================================================
File: file_utils.py

Purpose:
    Utility functions for handling file operations.

Used By:
    - Resume Upload
    - Job Description Upload
    - RAG Knowledge Base
=========================================================
"""

from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

from app.core.config import settings


# ==========================================================
# Upload Directory
# ==========================================================

UPLOAD_DIRECTORY = Path(settings.UPLOAD_DIRECTORY)
UPLOAD_DIRECTORY.mkdir(parents=True, exist_ok=True)


# ==========================================================
# Generate Unique Filename
# ==========================================================

def generate_unique_filename(filename: str) -> str:
    """
    Generates a unique filename while preserving the extension.

    Example:
        resume.pdf

    becomes

        e3ab5f7c4d924d0b9d3a9ef6f6c4fd18.pdf
    """

    extension = Path(filename).suffix.lower()

    return f"{uuid4().hex}{extension}"


# ==========================================================
# Save Uploaded File
# ==========================================================

def save_uploaded_file(file: UploadFile) -> Path:
    """
    Saves an uploaded file and returns its path.
    """

    unique_filename = generate_unique_filename(file.filename)

    file_path = UPLOAD_DIRECTORY / unique_filename

    with open(file_path, "wb") as output_file:
        output_file.write(file.file.read())

    return file_path


# ==========================================================
# Delete File
# ==========================================================

def delete_file(file_path: Path) -> bool:
    """
    Deletes a file if it exists.
    """

    if file_path.exists():
        file_path.unlink()
        return True

    return False


# ==========================================================
# Get File Size
# ==========================================================

def get_file_size(file_path: Path) -> int:
    """
    Returns file size in bytes.
    """

    return file_path.stat().st_size