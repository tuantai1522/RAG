from typing import List, Optional
from pydantic import BaseModel

class ChunkMetaData(BaseModel):
    file_name: Optional[str]
    page_numbers: Optional[List[int]]
    title: Optional[str]


