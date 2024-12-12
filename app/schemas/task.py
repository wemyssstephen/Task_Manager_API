from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    # Fields that are common to both creation and responses
    title: str = Field(
        min_length=1,
        max_length=100,
        description="The title of task"
    )
    description: Optional[str] = Field(
        None,
        max_length=1000,
        description="Detailed description of task"
    )
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

