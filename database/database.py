from typing import List, Union

from beanie import PydanticObjectId

from models.namespace import Namespace

namespace_collection = Namespace

async def list_namespace() -> List[Namespace]:
    students = await namespace_collection.all().to_list()
    return students