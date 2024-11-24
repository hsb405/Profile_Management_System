'''
---------------------------------------------------
Project:        Profile Management System
Date:           Aug 23, 2024
Author:         Abdul Haseeb
---------------------------------------------------

Description:
User Task Creation.
---------------------------------------------------
'''

from datetime import datetime
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from app.db_configuration.database import tasks_collection

# Task creation schema to validate the request body
class CreateTaskRequest(BaseModel):
    """
    Schema for creating a new task.
    """
    task_name: str
    user_id: str

router = APIRouter()

@router.post("/")
async def create_task(task: CreateTaskRequest):
    """
    Creates a new task and stores it in mongo database.
    """
    task_data = {
        "task_name": task.task_name,
        "user_id": task.user_id,
        "created_at": datetime.utcnow()
    }
    result = await tasks_collection.insert_one(task_data)
    return {"id": str(result.inserted_id), "task_name": task.task_name}
