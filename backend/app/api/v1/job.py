from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.models.user import User

from app.schemas.job import JobCreate
from app.schemas.job_analysis import JobAnalysisResponse

from app.security.dependencies import get_current_user

from app.services.job_service import JobService
from app.schemas.job_response import JobResponse


router = APIRouter(

    prefix="/jobs",

    tags=["Jobs"],
)


@router.post("/upload", response_model=JobResponse,)
def upload_job(

    job: JobCreate,

    db: Session = Depends(get_db),

    current_user: User = Depends(
        get_current_user,
    ),
):

    service = JobService(
        db,
    )

    return service.create_job(
        job,
        current_user,
    )


@router.get(

    "/analysis/{job_id}",

    response_model=JobAnalysisResponse,
)
def get_job_analysis(

    job_id: str,

    db: Session = Depends(get_db),
):

    service = JobService(
        db,
    )

    return service.get_analysis(
        job_id,
    )