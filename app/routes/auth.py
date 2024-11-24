'''
---------------------------------------------------
Project:        Profile Management System
Date:           Aug 23, 2024
Author:         Abdul Haseeb
---------------------------------------------------

Description:
Auth Login Module.
---------------------------------------------------
'''

from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from app.db_configuration.database import users_collection
from app.core.security import verify_password, create_access_token

router = APIRouter()

class LoginInput(BaseModel):
    """
    Pydantic model representing the input data for the login endpoint.
    """
    email: str
    password: str

@router.post("/login")
async def login(input_data: LoginInput):
    """
    Authenticates a user by validating their email and password
    and then generates a JWT access token.
    """

    email = input_data.email
    password = input_data.password

    # Find the user by email
    user = await users_collection.find_one({"email": email})
    if not user or not verify_password(password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Create a JWT token
    access_token = create_access_token(data={"sub": str(user["_id"])})
    return {"access_token": access_token, "token_type": "bearer"}
