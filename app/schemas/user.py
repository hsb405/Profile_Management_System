'''
---------------------------------------------------
Project:        Profile Management System
Date:           Aug 23, 2024
Author:         Abdul Haseeb
---------------------------------------------------

Description:
Class User Schema.
---------------------------------------------------
'''

from pydantic import BaseModel, EmailStr

class UserIn(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    username: str
    email: EmailStr
