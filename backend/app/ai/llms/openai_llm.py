from langchain_openai import ChatOpenAI

from app.core.config import settings


llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.2,
    api_key=settings.OPENAI_API_KEY,
)