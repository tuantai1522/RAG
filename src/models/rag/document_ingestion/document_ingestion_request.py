from pydantic import BaseModel


class DocumentIngestionRequest(BaseModel):
    file_bytes: bytes
    filename: str
