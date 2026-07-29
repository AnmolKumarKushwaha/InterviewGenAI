from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.models.resume import Resume
from app.models.user import User
from app.repositories.resume_repository import ResumeRepository
from app.utils.file_storage import FileStorage
from app.utils.file_validator import FileValidator

from app.extractors.extractor import ResumeExtractor
from app.utils.text_cleaner import TextCleaner

class ResumeService:

    def __init__(
        self,
        db: Session,
    ):

        self.repository = ResumeRepository(db)

    async def upload_resume(
        self,
        file: UploadFile,
        current_user: User,
    ):

        await FileValidator.validate(file)

        stored_file = await FileStorage.save(file)
        
        text = ResumeExtractor.extract(
        stored_file["file_path"],
    )

        
        
        print("=" * 60)
        print("Extracted text length:", len(text))
        print(text[:300])
        print("=" * 60)

        text = TextCleaner.clean(text)
        
        print("Cleaned text length:", len(text))
        
        
        resume = Resume(

            user_id=current_user.id,

            original_filename=file.filename,

            stored_filename=stored_file[
                "stored_filename"
            ],

            file_path=stored_file[
                "file_path"
            ],

            file_size=file.size,

            mime_type=file.content_type,
        )

        # Save metadata
        resume = self.repository.create(
           resume,
        )

        # Save extracted text
        self.repository.update_text(
            resume,
            text,
    )
        
        print("Saved extracted text to database.")

        return resume