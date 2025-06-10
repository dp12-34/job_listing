from pydantic import BaseModel
from typing import Optional

class JobListing(BaseModel):
    title: str
    company: Optional[str] = None
    location: Optional[str] = None
    url: Optional[str] = None
    description: Optional[str] = None
