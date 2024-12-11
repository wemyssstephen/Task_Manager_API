from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    # Fields that are common to both creation and responses
    title: str
    description: Optional[str] = None
    is_completed: bool = False

class CreateTaskRequest(TaskBase):
    # Inherits all fields from TaskBase, but does not need id or created_at
    pass

class UpdateTaskRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = False

class TaskResponse(TaskBase):
    """This task class defines how the data looks in my API and handles data validation."""
    # Has all fields from TaskBase plus the below:
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

