import os
import ssl
import requests
from typing import Optional

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
import models as models

async def initiate_database():
    print("====initiate_database====")
    requests.get('https://webhook.site/36856e9f-c26d-46f5-b684-6cd0a6e0e30f')
    user = os.getenv('MONGODB_USERNAME', 'ltp')
    password = os.getenv('MONGODB_PASSWORD', 'password')
    host = os.getenv('MONGODB_HOST', 'localhost')
    db_name = os.getenv('MONGODB_NAME', 'ltp')

    DATABASE_URL = f"mongodb+srv://{user}:{password}@{host}/"
    client = AsyncIOMotorClient(DATABASE_URL)
    print(client)
    await init_beanie(
        database=client[db_name], document_models=models.__all__
    )