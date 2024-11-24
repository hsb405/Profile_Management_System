'''
---------------------------------------------------
Project:        Profile Management System
Date:           Aug 23, 2024
Author:         Abdul Haseeb
---------------------------------------------------

Description:
Auth Middleware Module.
---------------------------------------------------
'''

from jose import jwt, JWTError
from fastapi import Request, HTTPException
from app.core.security import SECRET_KEY, ALGORITHM
from starlette.middleware.base import BaseHTTPMiddleware

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        excluded_paths = ["/auth/register", "/auth/login", "/docs", "/redoc", "/openapi.json"]
        
        if any(request.url.path.startswith(path) for path in excluded_paths):
            return await call_next(request)

        # Check for Authorization header
        token = request.headers.get("Authorization")
        if not token or not token.startswith("Bearer "):
            raise HTTPException(status_code=403, detail="Invalid or missing authentication token")

        try:
            jwt.decode(token.split(" ")[1], SECRET_KEY, algorithms=[ALGORITHM])
        except JWTError:
            raise HTTPException(status_code=403, detail="Invalid token")

        return await call_next(request)
