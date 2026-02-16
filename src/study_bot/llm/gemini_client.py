from .base import LLMClient
from google import genai

class GeminiClient(LLMClient):
    def __init__(self, api_key: str, model: str = "gemini-3-flash-preview"):
        self.client = genai.Client()
        self.model = model

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )
        return response.text
