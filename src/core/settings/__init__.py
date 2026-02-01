# __init__.py
from .database import DatabaseSettings

class Settings:
    database = DatabaseSettings()

settings = Settings()
