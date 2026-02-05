from fastapi import FastAPI

from src.api.v1.rag import rag
from src.core.logging import configure_logging

configure_logging()

app = FastAPI()

app.include_router(
    rag.router,
    prefix="/api",         
    tags=["documents"],     
)

