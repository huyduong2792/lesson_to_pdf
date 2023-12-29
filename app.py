from fastapi import FastAPI
from contextlib import asynccontextmanager
from config.config import initiate_database


@asynccontextmanager
async def start_database(app: FastAPI):
    # https://fastapi.tiangolo.com/advanced/events/
    await initiate_database()
    yield
    print("Shuting down...")

app = FastAPI(lifespan=start_database)

@app.get("/")
async def root():
    return {"message": "Hello World"}