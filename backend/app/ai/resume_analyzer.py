import json

from app.ai.prompts import RESUME_ANALYZER_PROMPT
from app.ai.providers.llm import LLM


class ResumeAnalyzer:

    @staticmethod
    def analyze(
        resume_text: str,
    ):

        prompt = RESUME_ANALYZER_PROMPT.format(
            resume=resume_text,
        )

        response = LLM.generate(
            prompt,
        )

        # Gemini sometimes wraps JSON inside ```json ... ```
        response = response.strip()

        if response.startswith("```json"):
            response = response[7:]

        if response.startswith("```"):
            response = response[3:]

        if response.endswith("```"):
            response = response[:-3]

        response = response.strip()

        return json.loads(
            response,
        )