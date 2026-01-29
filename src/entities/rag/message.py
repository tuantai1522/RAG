from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import UUID, TEXT, ForeignKey
import uuid
from datetime import datetime
from sqlalchemy import func

from entities.base import Base
from entities.rag.message_role import MessageRole

class Message(Base):
    __tablename__ = 'messages'

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
        back_populates="messages"
    )

    text: Mapped[str] = mapped_column(TEXT, nullable=False)
    role: Mapped[MessageRole]

    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())
