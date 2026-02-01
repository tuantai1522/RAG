from fastapi import FastAPI

from src.core.logging import configure_logging

configure_logging()

app = FastAPI()

@app.get("/")
async def root():
    return "Hello World !"


@app.get("/123")
async def root():
    return "Hello World123 !"
