
from types import NoneType
from fastapi import Depends, FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
#from fastapi.templating import Jinja2Templates

from typing import Annotated
from os.path import abspath
from os import listdir
from datetime import date

import os
import json

from requests import Session



from model.model import field

from priceChecker.priceCheck import price_check
from priceChecker.checkSocPrice import checkSocPrice


app = FastAPI()

"""@app.post("/auth")
async def hello(user: ValUser):
    #User
    return {user.phone: user.email}
"""
"""@app.post("/check_health")
async def check_health(user: ValUser):
    return {user.phone, user.email}"""

"""
#async def checkPrice(data: ValUser):
async def checkPrice(data: field):
    place = data.place
    email = data.email
    phone = data.phone
"""
@app.post("/check_social_price/file")
async def load_img(photo: UploadFile = File(...)):
    with open(abspath("./temp.jpg"), 'wb') as file:
        file.write(photo.file.read())
    return {"status", photo.filename}

@app.post("/check_social_price")
async def checkPrice(data: field):
    address = data.address
    email = data.email
    phone = data.phone
    #, user: ValUser
    #return {"file size": len(file)}
    #with open(abspath(f"../files/{datetime.today()}|{user.email}|{user.phone}|{user.place}.jpg"), 'w') as file:
    #    file.write(img)
    path = abspath(f"files/{address}|{phone}|{email}|{date.today()}.jpg")
    with open(path, 'wb') as file:
        with open(abspath("./temp.jpg"), 'rb') as temp:
            file.write(temp.read())
        os.remove(abspath("./temp.jpg"))

    res = price_check(path, abspath("./priceChecker/rostov_prices.json"))
    print(res)
    if res is None:
        return {"status": "Не удалось распознать ценник"}
    if res[3] == 1:
        if res[4] is None:
            return {"status": "Не удалось распознать ценник"}
        if int(checkSocPrice(res[1])[0]) < res[4]:
            return {"status": "цена, как для социального ценника, завышена"}
        os.remove(path)
        return {"status": "цена, как для социального ценника, не завышена"}
    os.remove(path)
    return {"status": "это не социальный ценник"}


"""@app.post("/check_steal")
async def uploadfile(index.htmlfile: UploadFile):
    return {"filename", file.filename}
"""
@app.get("/admin")
def admin():
    res = []
    for x in listdir(abspath("./files/")):
        #res.append(x.replace(".jpg", "").split("|"))
        res.append(x.replace(".jpg", "").split("|"))
    
    json_res = json.dumps(res)
    print(json_res)
    return json_res