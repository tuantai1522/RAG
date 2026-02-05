# __init__.py
from .application import ApplicationSettings
from .ollama import OllamaSettings
from .docling import DoclingSettings
from .database import DatabaseSettings

class Settings:
    database = DatabaseSettings()
    docling = DoclingSettings()
    ollama = OllamaSettings()
    application = ApplicationSettings()

    
settings = Settings()
