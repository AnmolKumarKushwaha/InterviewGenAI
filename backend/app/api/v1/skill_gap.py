from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.skill_gap import SkillGapResponse
from app.schemas.skill_gap_request import SkillGapRequest

from app.services.skill_gap_service import SkillGapService


router = APIRouter(

    prefix="/skill-gap",

    tags=["Skill Gap"],
)


@router.post(

    "/analyze",

    response_model=SkillGapResponse,
)
def analyze(

    request: SkillGapRequest,

    db: Session = Depends(
        get_db,
    ),
):

    service = SkillGapService(
        db,
    )

    return service.analyze(

        str(request.resume_id),

        str(request.job_id),
    )