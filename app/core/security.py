'''
---------------------------------------------------
Project:        Profile Management System
Date:           Nov 23, 2024
Author:         Abdul Haseeb
---------------------------------------------------

Description:
Password Hashing and Verification and access_token.
---------------------------------------------------
'''
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    """
    Hashes a given password using bcrypt algorithm.
    """
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    """
    Verifies that plain text password matches with the hashed version.
    """
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Creates a JSON Web Token (JWT) with expiry time.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
