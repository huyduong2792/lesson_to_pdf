import os
from typing import Optional

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
import models as models


async def initiate_database():
    print("====initiate_database====")
    user = os.getenv('MONGODB_USERNAME')
    password = os.getenv('MONGODB_PASSWORD')
    host = os.getenv('MONGODB_HOST')
    port = int(os.getenv('MONGODB_PORT', 27017))
    db_name = os.getenv('MONGODB_NAME', 'ltp')

    DATABASE_URL = f"mongodb://{user}:{password}@{host}:{port}/{db_name}"
    client = AsyncIOMotorClient(DATABASE_URL)
    await init_beanie(
        database=client[db_name], document_models=models.__all__
    )