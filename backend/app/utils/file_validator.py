from pathlib import Path

from fastapi import HTTPException
from fastapi import UploadFile
from fastapi import status

from app.core.constants import (
    ALLOWED_RESUME_EXTENSIONS,
    MAX_RESUME_SIZE_MB,
)


class FileValidator:

    @staticmethod
    async def validate(file: UploadFile):

        extension = Path(file.filename).suffix.lower()

        if extension not in ALLOWED_RESUME_EXTENSIONS:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Only PDF and DOCX files are allowed.",
            )

        content = await file.read()

        size_mb = len(content) / (1024 * 1024)

        if size_mb > MAX_RESUME_SIZE_MB:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Maximum file size is {MAX_RESUME_SIZE_MB} MB.",
            )

        await file.seek(0)