from app.ai.llms.openai_llm import llm


class OpenAIProvider:

    def generate(
        self,
        prompt: str,
    ) -> str:

        response = llm.invoke(prompt)
        
        print("=" * 60)
        print(response)
        print("=" * 60)

        return response.content