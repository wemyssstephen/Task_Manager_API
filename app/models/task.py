from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from datetime import datetime
from ..database import Base

class TaskModel(Base):
    """This task class defined how data is stored in the database. It maps directly to the database table structure."""
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())