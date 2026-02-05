from abc import ABC, abstractmethod

class FileStorage(ABC):
    @abstractmethod
    def save(self, file_bytes: bytes, filename: str) -> str:
        """Return local file path"""
        pass
