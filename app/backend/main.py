from fastapi import FastAPI, File, UploadFile
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String

from typing import Annotated
from uuid import uuid4

from model.model import ValUser
from db.create_table import Base, Users


app = FastAPI()

"""@app.post("/auth")
async def hello(user: ValUser):
    #User
    return {user.phone: user.email}
"""
@app.post("/check_social_price")
async def get_file(file: Annotated[bytes, File()], user: ValUser):
    return {"file size": len(file)}

@app.post("/check_steal")
async def uploadfile(file: UploadFile):
    return {"filename", file.filename}
