from pydantic import BaseModel
from typing import Optional

class NewsItem(BaseModel):
    title: str
    link: str
    summary: Optional[str] = None
    published: Optional[str] = None
    source: Optional[str] = None
