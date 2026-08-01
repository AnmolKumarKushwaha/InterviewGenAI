import json

from app.ai.prompts.explanation_prompt import EXPLANATION_PROMPT
from app.ai.providers.llm import LLM
from app.utils.json_parser import parse_llm_json


class ExplanationGenerator:

    @staticmethod
    def generate(
        missing_skills: list[str],
    ) -> list:

        if not missing_skills:

            return []

        prompt = EXPLANATION_PROMPT.format(

            skills="\n".join(
                missing_skills,
            ),
        )

        response = LLM.generate(prompt,)

        return parse_llm_json(response)