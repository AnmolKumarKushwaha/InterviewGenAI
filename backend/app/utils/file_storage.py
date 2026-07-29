import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

UPLOAD_DIRECTORY = Path("uploads")


class FileStorage:

    @staticmethod
    async def save(file: UploadFile):

        UPLOAD_DIRECTORY.mkdir(
            exist_ok=True,
        )

        extension = Path(file.filename).suffix.lower()

        stored_filename = f"{uuid4()}{extension}"

        destination = UPLOAD_DIRECTORY / stored_filename

        with destination.open("wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer,
            )

        return {
            "stored_filename": stored_filename,
            "file_path": str(destination),
        }