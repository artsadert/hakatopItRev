from fastapi import FastAPI, File, UploadFile

from typing import Annotated

from model.model import User, ValUser



app = FastAPI()

@app.post("/auth")
async def hello(user: ValUser):
    User.
    return {user.phone: user.email}

@app.post("/img")
async def get_file(file: Annotated[bytes, File()]):
    return {"file size": len(file)}

@app.post("/")
async def uploadfile(file: UploadFile):
    return {"filename", file.filename}
