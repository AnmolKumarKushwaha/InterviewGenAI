"""
=========================================================
File: constants.py

Purpose:
    Stores all application-wide constant values.

Why?

Instead of writing string literals everywhere
("admin", "completed", "technical"),

we define them once and reuse them.

=========================================================
"""

from enum import Enum


# ==========================================================
# User Roles
# ==========================================================

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"


# ==========================================================
# Resume Status
# ==========================================================

class ResumeStatus(str, Enum):
    UPLOADED = "uploaded"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


# ==========================================================
# Job Description Status
# ==========================================================

class JDStatus(str, Enum):
    UPLOADED = "uploaded"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


# ==========================================================
# Interview Types
# ==========================================================

class InterviewType(str, Enum):
    TECHNICAL = "technical"
    HR = "hr"
    CODING = "coding"
    VOICE = "voice"


# ==========================================================
# Interview Status
# ==========================================================

class InterviewStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


# ==========================================================
# Difficulty Levels
# ==========================================================

class Difficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


# ==========================================================
# Supported File Types
# ==========================================================

ALLOWED_RESUME_EXTENSIONS = {
    ".pdf",
    ".docx",
}

MAX_RESUME_SIZE_MB = 10