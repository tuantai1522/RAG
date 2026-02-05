from sqlalchemy import create_engine
from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import sessionmaker, Session

from src.core import settings

engine = create_engine(settings.database.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close

DbSession = Annotated[Session, Depends(get_db)]