"""
=========================================================
File: hashing.py

Purpose:
    Handles password hashing and password verification.

Why?

Never store plain-text passwords inside the database.

Instead:

Password
      ↓
bcrypt
      ↓
Hashed Password

=========================================================
"""

from passlib.context import CryptContext

# =========================================================
# Configure bcrypt hashing algorithm
# =========================================================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)

# =========================================================
# Hash Password
# =========================================================

def hash_password(password: str) -> str:
    """
    Converts a plain password into a bcrypt hash.
    """

    return pwd_context.hash(password)


# =========================================================
# Verify Password
# =========================================================

def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    """
    Returns True if passwords match.
    """

    return pwd_context.verify(
        plain_password,
        hashed_password,
    )