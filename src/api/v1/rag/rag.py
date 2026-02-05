from fastapi import APIRouter, Depends, File, UploadFile
from requests import Session
from src.database.core import get_db
from src.models.rag.document_ingestion.document_ingestion_request import DocumentIngestionRequest
from src.services.rag.dependencies import get_file_storage
from src.services.rag.document_ingestion_service import DocumentIngestionService

router = APIRouter()

@router.post("/documents/upload")
async def upload(
    file: UploadFile = File(...),
    storage = Depends(get_file_storage),
    db: Session = Depends(get_db),
):
    file_bytes = await file.read()

    ingestion = DocumentIngestionService(
        file_storage=storage,
        db=db
    )

    result = ingestion.execute(
        DocumentIngestionRequest(
            file_bytes=file_bytes,
            filename=file.filename,
        )
    )

    return result

