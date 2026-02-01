from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import TEXT, UUID, ForeignKey
from pgvector.sqlalchemy import Vector
import uuid

from src.database.entities.rag.chunk_metadata import ChunkMetaData
from src.database.entities.mixins.jsonb_metadata import JsonbMetadataMixin
from src.database.entities.base import Base

class Chunk(Base, JsonbMetadataMixin[ChunkMetaData]):
    __tablename__ = 'chunks'
    __metadata_field__ = "attributes"
    __metadata_model__ = ChunkMetaData

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    topic_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("topics.id"),
        nullable=False
    )

    topic: Mapped["Topic"] = relationship(
        back_populates="chunks"
    )

    attributes: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False,
        default=lambda: {}
    )

    text: Mapped[str] = mapped_column(TEXT, nullable=False)

    embeddings: Mapped[list[float]] = mapped_column(
        Vector(1536),
        nullable=False
    )