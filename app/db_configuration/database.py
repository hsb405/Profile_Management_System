'''
---------------------------------------------------
Project:        Profile Management System
Date:           Aug 23, 2024
Author:         Abdul Haseeb
---------------------------------------------------

Description:
Mongo Database Configuration.
---------------------------------------------------
'''

import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

client = AsyncIOMotorClient(MONGO_URI)
db = client["FASTAPI-Task"]
users_collection = db["users"]
tasks_collection = db["tasks"]
