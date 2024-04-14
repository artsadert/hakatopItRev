from pydantic import BaseModel
from typing import Annotated

#from fas

#sys.path.append('../..')

class File(BaseModel):
    #name: str
    #content_type: str
    photo: bytes

class field(BaseModel):
    address: str = None
    phone: str = None
    email: str = None

