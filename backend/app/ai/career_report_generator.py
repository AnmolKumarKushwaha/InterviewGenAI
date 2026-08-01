import json

from app.ai.prompts.career_report_prompt import CAREER_REPORT_PROMPT
from app.ai.providers.llm import LLM

from app.utils.json_parser import parse_llm_json


class CareerReportGenerator:

    @staticmethod
    def generate(

        resume_skills: list,

        missing_skills: list,

        match_percentage: float,

        learning_priorities: list,

        skill_explanations: list,

        learning_roadmap: dict,

        interview_preparation: dict,

    ):

        prompt = CAREER_REPORT_PROMPT.format(

            resume_skills=json.dumps(
                resume_skills,
                indent=4,
            ),

            missing_skills=json.dumps(
                missing_skills,
                indent=4,
            ),

            match_percentage=match_percentage,

            learning_priorities=json.dumps(
                learning_priorities,
                indent=4,
            ),

            skill_explanations=json.dumps(
                skill_explanations,
                indent=4,
            ),

            learning_roadmap=json.dumps(
                learning_roadmap,
                indent=4,
            ),

            interview_preparation=json.dumps(
                interview_preparation,
                indent=4,
            ),
        )

        response = LLM.generate(
            prompt,
        )

        return parse_llm_json(
            response.strip(),
        )