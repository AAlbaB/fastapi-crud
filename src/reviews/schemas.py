import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ReviewModel(BaseModel):
    uid: uuid.UUID
    rating: int = Field(le=5, ge=1)
    review_text: str
    user_uid: Optional[uuid.UUID] = Field(exclude=True)
    book_uid: Optional[uuid.UUID]
    created_at: datetime
    update_at: datetime


class ReviewCreateModel(BaseModel):
    rating: int = Field(le=5, ge=1)
    review_text: str
