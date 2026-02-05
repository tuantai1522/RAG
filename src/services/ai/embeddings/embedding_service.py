from openai import OpenAI

from src.core import settings

class EmbeddingService:
    def __init__(self):
        self.client = OpenAI(
            base_url=f"{settings.ollama.BASE_URL}/v1",
            api_key=settings.ollama.BASE_URL
        )
        self.model = settings.ollama.EMBED_MODEL_ID

    def embed(self, texts: list[str]):
        res = self.client.embeddings.create(
            model = self.model,
            input = texts,
        )
        return [d.embedding for d in res.data]
