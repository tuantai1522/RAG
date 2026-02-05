from src.core.settings.base import BaseAppSettings

class DoclingSettings(BaseAppSettings):
    TOKEN_MODEL_ID: str

    PAGE_BREAK_PLACEHOLDER: str
    IMAGE_DESCRIPTION_START: str
    IMAGE_DESCRIPTION_END: str