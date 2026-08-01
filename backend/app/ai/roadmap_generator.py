import json

from app.ai.prompts.roadmap_prompt import ROADMAP_PROMPT
from app.ai.providers.llm import LLM
from app.utils.json_parser import parse_llm_json

class RoadmapGenerator:

    @staticmethod
    def generate(
        resume_skills: list[str],
        missing_skills: list[str],
        learning_priorities: list,
        skill_explanations: list,
    ) -> dict:

        prompt = ROADMAP_PROMPT.format(

            resume_skills=json.dumps(
                resume_skills,
                indent=4,
            ),

            missing_skills=json.dumps(
                missing_skills,
                indent=4,
            ),

            learning_priorities=json.dumps(
                learning_priorities,
                indent=4,
            ),

            skill_explanations=json.dumps(
                skill_explanations,
                indent=4,
            ),
        )

        response = LLM.generate(
            prompt,
        )

        return parse_llm_json(response)