from typing import Optional, Any
from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr


class Namespace(Document):
    name: str

    class Config:
        json_schema_extra = {
            "example": {
                "name": "ns-huydq-test",
            }
        }

    class Settings:
        name = "namespace"

class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data",
            }
        }