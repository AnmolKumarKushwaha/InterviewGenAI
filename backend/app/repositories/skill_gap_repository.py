from sqlalchemy.orm import Session

from app.models.skill_gap import SkillGap


class SkillGapRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create(
        self,
        gap: SkillGap,
    ):

        self.db.add(
            gap,
        )

        self.db.commit()

        self.db.refresh(
            gap,
        )

        return gap

    def get(
        self,
        resume_id,
        job_id,
    ):

        return (
            self.db.query(
                SkillGap,
            )
            .filter(
                SkillGap.resume_id == resume_id,
                SkillGap.job_id == job_id,
            )
            .first()
        )