from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class InterviewCreate(BaseModel):
    role: str = Field(min_length=2, max_length=100)
    difficulty: str = Field(min_length=3, max_length=20)

class InterviewUpdate(BaseModel):
    role: str | None = Field(default=None, min_length=2, max_length=100)
    difficulty: str | None = Field(default=None, min_length=3, max_length=20)

class InterviewResponse(BaseModel):
    id: int
    role: str
    difficulty: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
