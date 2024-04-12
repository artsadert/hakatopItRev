from dotenv import load_dotenv
from os import getenv

load_dotenv()

def get_env():
    return {
        "name_db": getenv("POSTGRES_DB"),
        "user": getenv("POSTGRES_USER"),
        "password": getenv("POSTGRES_PASSWORD")
    }

def url_for_postgres(for_engine=False):
    """it can be used to connect to db"""
    url_attr = get_env()
    if for_engine:
        return f"postgresql+psycopg://{url_attr['user']}:{url_attr['password']}@localhost:5432/{url_attr['name_db']}"
    else:
        return f"postgresql://{url_attr['user']}:{url_attr['password']}@localhost:5432/{url_attr['name_db']}"

if __name__ == "__main__":
    print(url_for_postgres())
    print(url_for_postgres(for_engine=True))
