from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hello World !"


@app.get("/123")
async def root():
    return "Hello World123 !"
