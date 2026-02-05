
from src.core import settings
from src.services.file.local_storage import LocalFileStorage


def get_file_storage():
    return LocalFileStorage(base_dir=settings.application.UPLOAD_DIR)
