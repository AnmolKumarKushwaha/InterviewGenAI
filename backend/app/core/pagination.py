"""
=========================================================
File: pagination.py

Purpose:
    Provides reusable pagination utilities for APIs.

Used in:
    - Interview History
    - Resume History
    - Dashboard
    - Users
    - Practice Questions
=========================================================
"""

from math import ceil

from pydantic import BaseModel, Field


# ==========================================================
# Pagination Request Parameters
# ==========================================================

class PaginationParams(BaseModel):
    """
    Query parameters for pagination.
    """

    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=10, ge=1, le=100)


# ==========================================================
# Pagination Metadata
# ==========================================================

class PaginationMetadata(BaseModel):
    """
    Metadata returned with paginated responses.
    """

    page: int
    page_size: int
    total_records: int
    total_pages: int


# ==========================================================
# Pagination Utility
# ==========================================================

def paginate(
    page: int,
    page_size: int,
    total_records: int,
):
    """
    Returns offset, limit and metadata.
    """

    offset = (page - 1) * page_size

    metadata = PaginationMetadata(
        page=page,
        page_size=page_size,
        total_records=total_records,
        total_pages=ceil(total_records / page_size) if total_records else 0,
    )

    return offset, page_size, metadata