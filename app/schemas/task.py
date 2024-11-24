'''
---------------------------------------------------
Project:        Profile Management System
Date:           Aug 23, 2024
Author:         Abdul Haseeb
---------------------------------------------------

Description:
Class Task Schema.
---------------------------------------------------
'''

from datetime import datetime
from pydantic import BaseModel

class Task(BaseModel):
    task_name: str
    user_id: str
    created_at: datetime
