from app.ai.providers.gemini_provider import GeminiProvider


response = GeminiProvider().generate(
    "Say hello in exactly five words."
)

print(response)