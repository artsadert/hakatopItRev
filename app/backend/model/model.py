from pydantic import BaseModel, Field


#sys.path.append('../..')

class ValUser(BaseModel):
    phone: str = Field(max_length=50)
    email: str = Field(max_length=50)


