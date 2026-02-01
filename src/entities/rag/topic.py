from datetime import datetime
from typing import List
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import UUID, func
import uuid

from src.entities.base import Base

class Topic(Base):
    __tablename__ = "topics"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    messages: Mapped[List["Message"]] = relationship(
        back_populates="topic",
        cascade="all, delete-orphan"
    )

    chunks: Mapped[List["Chunk"]] = relationship(
        back_populates="topic",
        cascade="all, delete-orphan"
    )

    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())
