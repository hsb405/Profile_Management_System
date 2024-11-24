'''
---------------------------------------------------
Project:        Profile Management System
Date:           Aug 23, 2024
Author:         Abdul Haseeb
---------------------------------------------------

Description:
FASTAPI Modular Routing.
---------------------------------------------------
'''

from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.tasks import router as tasks_router
from app.middleware.auth_middleware import AuthMiddleware
from app.routes.templates import router as templates_router

app = FastAPI()

# Add middleware
app.add_middleware(AuthMiddleware)

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(tasks_router, prefix="/tasks", tags=["tasks"])
app.include_router(templates_router, prefix="/templates", tags=["templates"])
