from http.client import HTTPException

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import engine, get_db
from . import models, schemas

# Create database tables
models.Base.metadata.create_all(bind=engine)
app = FastAPI()
@app.post("/tasks/", summary="Create a New Task",response_model=schemas.TaskResponse)
def create_task(task: schemas.CreateTaskRequest, db: Session = Depends(get_db)):
    # Creates a new line
    db_task = models.TaskModel(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/tasks/", summary="Return All Tasks",response_model=list[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    # Retrieves all lines
    tasks = db.query(models.TaskModel).all()
    return tasks

@app.get("/tasks/uncompleted/", summary="List All Incomplete Tasks", response_model=list[schemas.TaskResponse])
def get_uncompleted_tasks(db: Session = Depends(get_db)):
    # Retrieves all uncompleted tasks
    tasks = db.query(models.TaskModel).filter(models.TaskModel.is_completed == False).all()
    return tasks

@app.get("/tasks/completed/", summary="List Completed Tasks", response_model=list[schemas.TaskResponse])
def get_completed_tasks(db: Session = Depends(get_db)):
    # Retrieves all completed tasks
    tasks = db.query(models.TaskModel).filter(models.TaskModel.is_completed == True).all()
    return tasks

@app.patch("/tasks/", summary="Update Task", response_model=schemas.TaskResponse)
def update_task(task_id: int, task_update: schemas.UpdateTaskRequest, db: Session = Depends(get_db)):

    # Get existing task
    db_task = db.query(models.TaskModel).filter(models.TaskModel.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Update fields that are provided
    update_data = task_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_task, field, value)

    db.commit()
    db.refresh(db_task)
    return db_task

async def root():
    return {"message": "Task Management API"}