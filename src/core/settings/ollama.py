from src.core.settings.base import BaseAppSettings

class OllamaSettings(BaseAppSettings):
    BASE_URL: str
    EMBED_MODEL_ID: str
    CHAT_MODEL_ID: str
    VISION_MODEL_ID: str

    