from app.ai.providers.gemini_provider import GeminiProvider
from app.ai.providers.openai_provider import OpenAIProvider


class LLM:

    @staticmethod
    def generate(prompt: str) -> str:

        try:

            print("Using Gemini...")

            return GeminiProvider().generate(prompt)

        except Exception as e:

            print(f"Gemini failed: {e}")

        try:

            print("Using OpenAI...")

            return OpenAIProvider().generate(prompt)

        except Exception as e:

            print(f"OpenAI failed: {e}")

            raise Exception(
                "No LLM provider is available."
            )