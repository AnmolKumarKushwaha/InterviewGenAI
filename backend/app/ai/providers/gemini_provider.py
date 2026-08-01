from app.ai.llms.gemini_llm import llm


class GeminiProvider:

    def generate(
        self,
        prompt: str,
    ) -> str:

        response = llm.invoke(prompt)

        print("=" * 60)
        print(response)
        print("=" * 60)
        
        return response.content