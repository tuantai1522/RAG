import os
import uuid

from src.services.file.file_storage import FileStorage

class LocalFileStorage(FileStorage):
    def __init__(self, base_dir: str = "uploads"):
        self.base_dir = base_dir
        os.makedirs(base_dir, exist_ok=True)

    def save(self, file_bytes: bytes, filename: str) -> str:
        ext = os.path.splitext(filename)[1]
        file_id = f"{uuid.uuid4()}{ext}"
        file_path = os.path.join(self.base_dir, file_id)

        with open(file_path, "wb") as f:
            f.write(file_bytes)

        return file_path
