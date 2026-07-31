from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Text


class SkillGap(Base):

    __tablename__ = "skill_gap"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    resume_id = Column(
        String(36),
        ForeignKey(
            "resumes.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    job_id = Column(
        String(36),
        ForeignKey(
            "job_descriptions.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    match_percentage = Column(
        Float,
        nullable=False,
    )

    matched_skills = Column(
        JSON,
        nullable=False,
        default=list,
    )

    missing_skills = Column(
        JSON,
        nullable=False,
        default=list,
    )
    
    semantic_matches = Column(
        JSON,
        nullable=False,
        default=list,
    )
    
    matched_weight = Column(
        Integer,
        nullable=False,
        default=0,
    )

    total_weight = Column(
        Integer,
        nullable=False,
        default=0,
    )

    learning_recommendations = Column(
        JSON,
        nullable=False,
        default=list,
    )
    
    ai_feedback = Column(
        Text,
        nullable=False,
        default="",
    )
    
    learning_priorities = Column(
        JSON,
        nullable=False,
        default=list,
    )

    resume = relationship(
        "Resume",
    )

    job = relationship(
        "JobDescription",
    )