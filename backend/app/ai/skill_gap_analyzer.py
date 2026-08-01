from app.ai.skill_normalizer import SkillNormalizer

from app.ai.semantic_matcher import SemanticMatcher
from app.ai.skill_weights import SKILL_WEIGHTS
from app.ai.feedback_generator import FeedbackGenerator
from app.ai.priority_generator import PriorityGenerator
from app.ai.skill_explainer import SkillExplainer

class SkillGapAnalyzer:

    @staticmethod
    def analyze(

        resume,

        job,
    ):

        resume_skills = set(

            SkillNormalizer.normalize_list(

            resume.extracted_skills,
        )
    )

        job_skills = set(

            SkillNormalizer.normalize_list(

            job.required_skills,
        )
    ) 

        semantic_result = SemanticMatcher.match(

            list(resume_skills),

            list(job_skills),
        )

        matched = semantic_result["matched"]

        missing = semantic_result["missing"]

        semantic_matches = semantic_result["semantic_matches"]

        total_weight = 0

        matched_weight = 0

        for skill in job_skills:

            weight = SKILL_WEIGHTS.get(skill, 1,)

            total_weight += weight

            if skill in resume_skills:

                matched_weight += weight

        percentage = 0

        if total_weight:

            percentage = round(matched_weight / total_weight * 100, 2,)
            
        
        feedback = FeedbackGenerator.generate(
            matched,
            missing,
            percentage,
        )
        
        priorities = PriorityGenerator.generate(
            missing,
        )
        
        skill_explanations = SkillExplainer.generate(
            missing,
        )

        return {

            "match_percentage": percentage,

            "matched_skills": matched,

            "missing_skills": missing,
            
            "semantic_matches": semantic_matches,
            
            "matched_weight": matched_weight,

            "total_weight": total_weight,

            "learning_recommendations": [

                f"Learn {skill}"

                for skill in missing
            ],
            
            "learning_priorities": priorities,
            
            "ai_feedback": feedback,
            
            "skill_explanations": skill_explanations,
        }