'''
---------------------------------------------------
Project:        Profile Management System
Date:           Aug 23, 2024
Author:         Abdul Haseeb
---------------------------------------------------

Description:
Class User Model.
---------------------------------------------------
'''

from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str
    is_active: bool = True
