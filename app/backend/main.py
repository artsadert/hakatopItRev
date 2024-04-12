from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/")
async def hello():
    return {"hello": "world"}

@app.post("/files/")
async def get_file(file: Annotated[bytes, File()]):
    return {"file size": len(file)}

@app.post("/uploadfile")
async def uploadfile(file: UploadFile):
    return {"filename", file.filename}
