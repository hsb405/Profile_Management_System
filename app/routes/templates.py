'''
---------------------------------------------------
Project:        Profile Management System
Date:           Aug 23, 2024
Author:         Abdul Haseeb
---------------------------------------------------

Description:
Template Module.
---------------------------------------------------
'''

import os
import json
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_template():
    # Get the absolute path of the project root directory
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    
    template_path = os.path.join(project_root, "template.json")

    try:
        with open(template_path, "r") as file:
            template_data = json.load(file)
        return template_data
    except FileNotFoundError:
        return {"error": f"template.json not found at {template_path}"}
