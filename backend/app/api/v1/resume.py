from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import UploadFile

from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import User
from app.schemas.resume import ResumeResponse
from app.security.dependencies import get_current_user
from app.services.resume_service import ResumeService

from app.extractors.extractor import ResumeExtractor

from fastapi import HTTPException

from app.repositories.resume_repository import ResumeRepository
from app.schemas.resume_analysis import ResumeAnalysisResponse
from app.schemas.resume_history import ResumeHistoryResponse

router = APIRouter(
    prefix="/resumes",
    tags=["Resume"],
)


@router.post(
    "/upload",
    response_model=ResumeResponse,
)
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    service = ResumeService(db)

    return await service.upload_resume(
        file=file,
        current_user=current_user,
    )
    
    
@router.get("/extract/{resume_id}")
def extract_resume(
    resume_id: str,
    db: Session = Depends(get_db),
):

    repository = ResumeRepository(db)

    resume = repository.get_by_id(resume_id)

    if resume is None:

        raise HTTPException(
            status_code=404,
            detail="Resume not found.",
        )

    text = ResumeExtractor.extract(
        resume.file_path,
    )

    return {
        "characters": len(text),
        "preview": text[:1000],
    }
    
    
@router.get(
    "/analysis/{resume_id}",
    response_model=ResumeAnalysisResponse,
)
def get_resume_analysis(
    resume_id: str,
    db: Session = Depends(get_db),
):

    service = ResumeService(
        db,
    )

    return service.get_analysis(
        resume_id,
    )
    
    
    
@router.get(
    "",
    response_model=list[ResumeHistoryResponse],
)
def get_user_resumes(

    db: Session = Depends(get_db),

    current_user: User = Depends(
        get_current_user,
    ),

):

    service = ResumeService(
        db,
    )

    return service.get_user_resumes(
        current_user,
    )