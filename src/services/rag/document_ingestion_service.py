from src.database.entities.rag.chunk import Chunk
from src.database.entities.rag.chunk_metadata import ChunkMetaData
from src.models.rag.document_ingestion.document_ingestion_request import DocumentIngestionRequest
from src.models.rag.document_ingestion.document_ingestion_response import DocumentIngestionResponse
from src.services.ai.embeddings.embedding_service import EmbeddingService
from src.services.file.file_storage import FileStorage
from src.services.rag.docling import DoclingService
from sqlalchemy.orm import Session
from uuid import UUID

class DocumentIngestionService:
    def __init__(
        self, 
        file_storage: FileStorage,
        db: Session,
    ):
        self.file_storage = file_storage
        self.docling = DoclingService()
        self.embeddings = EmbeddingService()
        self.db = db

    def execute(
        self,
        request: DocumentIngestionRequest
    ) -> DocumentIngestionResponse:
        # 1. Save uploaded file
        file_path = self.file_storage.save(
            request.file_bytes,
            request.filename
        )

        # 2. Get chunks
        chunks = self.docling.get_chunks_by_link_url(file_path, request.filename)

        # 3. Only embeddings if len chunk is larger than 0
        if len(chunks) > 0:
            texts = [chunk["text"] for chunk in chunks]

            vectors = self.embeddings.embed(texts)

            # 4. Add new record in db
            TEST_TOPIC_ID = UUID("791b82c7-233e-47d5-a119-d657e1b3d239")

            for i in range(len(chunks)):
                new_chunk = Chunk(
                    text = chunks[i]["text"],
                    topic_id=TEST_TOPIC_ID,

                    embeddings = vectors[i],
                    attributes = ChunkMetaData(
                        file_name = chunks[i]["metadata"]["file_name"],
                        page_numbers = chunks[i]["metadata"]["page_numbers"],
                        title = chunks[i]["metadata"]["title"],
                    ).model_dump()
                )

                self.db.add(new_chunk)

            # Commit the changes to the database
            self.db.commit()

        return DocumentIngestionResponse(
            file_path=file_path,
            chunk_count=len(chunks),
        )
