from fastapi import UploadFile
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.resume import Resume
from app.models.user import User

from app.repositories.resume_repository import ResumeRepository

from app.ai.resume_analyzer import ResumeAnalyzer
from app.models.resume_analysis import ResumeAnalysis
from app.repositories.resume_analysis_repository import ResumeAnalysisRepository

from app.utils.file_storage import FileStorage
from app.utils.file_validator import FileValidator

from app.extractors.extractor import ResumeExtractor
from app.utils.text_cleaner import TextCleaner

from app.schemas.resume_history import ResumeHistoryResponse
import os
from fastapi.responses import FileResponse


class ResumeService:

    def __init__(
        self,
        db: Session,
    ):

        self.repository = ResumeRepository(db)

        self.analysis_repository = ResumeAnalysisRepository(
          db,
        )

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
        
        analysis = ResumeAnalyzer.analyze(
            text,
         )

        print("=" * 60)
        print("Gemini Response")
        print(analysis)
        print("=" * 60)

        analysis_record = ResumeAnalysis(

            resume_id=resume.id,

            extracted_skills=analysis["skills"],

            extracted_projects=analysis["projects"],

            extracted_experience=analysis["experience"],

            extracted_education=analysis["education"],

            resume_score=analysis["resume_score"],

            missing_skills=analysis["missing_skills"],

            suggestions=analysis["suggestions"],
        )

        self.analysis_repository.create(
            analysis_record,
        )

        print("Analysis saved.")

        return resume
    
    
    def get_analysis(
        self,
        resume_id: str,
    ):
    
        analysis = self.analysis_repository.get_by_resume_id(
            resume_id,
        )

        if analysis is None:

            raise HTTPException(
                status_code=404,
                detail="Analysis not found.",
            )

        return analysis
    
    
    def get_user_resumes(
        self,
        user: User,
    ):

        resumes = self.repository.get_user_resumes(
            user.id,
        )

        resume_ids = [
            resume.id
            for resume in resumes
        ]
        
        scores = (
            self.analysis_repository.get_scores(
                resume_ids,
            )
        )

        response = []

        for resume in resumes:
        
                response.append(
        
                    ResumeHistoryResponse(
        
                        id=resume.id,
        
                        original_filename=resume.original_filename,
        
                        created_at=resume.created_at,
        
                        resume_score=scores.get(
                            resume.id,
                        ),
                    )
                )
        
        return response
    
    
    def delete_resume(
        self,
        resume_id: str,
        current_user: User,
    ):

        resume = self.repository.get_by_id(
            resume_id,
        )

        if resume is None:
        
            raise HTTPException(
                status_code=404,
                detail="Resume not found.",
            )

        if resume.user_id != current_user.id:
        
            raise HTTPException(
                status_code=403,
                detail="Not authorized.",
            )

        if os.path.exists(
            resume.file_path,
        ):

            os.remove(
                resume.file_path,
            )

        self.repository.delete(
            resume,
        )

        return {
            "message": "Resume deleted successfully.",
        }
        
    def download_resume(
        self,
        resume_id: str,
        current_user: User,
    ):
        
        resume = self.repository.get_by_id(
            resume_id,
        )
        
        if resume is None:

            raise HTTPException(
                status_code=404,
                detail="Resume not found.",
            )

        if resume.user_id != current_user.id:

            raise HTTPException(
                status_code=403,
                detail="Not authorized.",
            )

        return FileResponse(

            path=resume.file_path,

            filename=resume.original_filename,

            media_type=resume.mime_type,
        )