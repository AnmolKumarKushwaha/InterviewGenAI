import json

from app.ai.prompts.job_analyzer_prompt import JOB_ANALYZER_PROMPT
from app.ai.providers.llm import LLM


class JobAnalyzer:

    @staticmethod
    def analyze(
        job_text: str,
    ):

        prompt = JOB_ANALYZER_PROMPT.format(
            job=job_text,
        )

        response = LLM.generate(
            prompt,
        )

        response = (
            response.replace(
                "```json",
                "",
            )
            .replace(
                "```",
                "",
            )
            .strip()
        )

        return json.loads(
            response,
        )