from google import genai

from app.core.config import settings


class GeminiProvider:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY,
        )

    def generate(
        self,
        prompt: str,
    ) -> str:

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        
        print("=" * 60)
        print(response.text)
        print("=" * 60)

        return response.text