from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, create_engine
from sqlalchemy.dialects.postgresql import UUID
import psycopg2

from uuid import uuid4

from load_url_db import url_for_postgres
class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "Users"

    id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = mapped_column(String(30), nullable=True, unique=True)
    phone = mapped_column(String(30), nullable=True, unique=True)

if __name__ == "__main__":
    engine = create_engine(url_for_postgres(for_engine=True))
    conn = psycopg2.connect(url_for_postgres())
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE Users;")
    cursor.close()
    conn.close()
    Base.metadata.create_all(engine)
