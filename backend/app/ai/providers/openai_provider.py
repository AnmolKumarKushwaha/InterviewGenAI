from openai import OpenAI

from app.core.config import settings


class OpenAIProvider:

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
        )

    def generate(
        self,
        prompt: str,
    ) -> str:

        response = self.client.chat.completions.create(

            model="gpt-4.1-mini",

            messages=[

                {
                    "role": "user",
                    "content": prompt,
                }

            ],

            temperature=0,
        )

        return response.choices[0].message.content