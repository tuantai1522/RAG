from pydantic import BaseModel


class DocumentIngestionResponse(BaseModel):
    file_path: str
    chunk_count: int
