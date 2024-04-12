from pydantic import BaseModel, Field
from sqlalchemy import Integer, String, Column
from sqlalchemy.dialects.postgresql import UUID

from uuid import uuid4
import sys

sys.path.append('../')
from db.create_table import Base

class ValUser(BaseModel):
    phone: str = Field(max_length=50)
    email: str = Field(max_length=50)

class User(Base):
    __tablename__ = "Users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    phone = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)

