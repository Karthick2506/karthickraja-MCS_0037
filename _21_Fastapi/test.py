from pydantic.parse import load_str_bytes
import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

# import uvicorn
#postgres Database
DATABASE_URL = "postgresql://usertest:usertest222@127.0.0.1:5432/dbtest"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.Metadata()

users = sqlalchemy.Table(
    "py_users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String),
    sqlalchemy.Column("password", sqlalchemy.String),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("gender", sqlalchemy.CHAR),
    sqlalchemy.Column("create_at", sqlalchemy.String),
    sqlalchemy.Column("status", sqlalchemy.CHAR),
    
)

engine = sqlalchemy.create_engine(
    DATABASE_URL
)
metadata.create_all(engine)
##Models
class UserList(BaseModel):
    id : str
    username : str
    password : str
    first_name : str
    last_name : str
    gender : str
    create_at : str
    status : str




aaa = FastAPI()

@aaa.get('/users', response_model=List[UserList])
def find_all_users():
    query = users.select()
    return await database.fetch_all(query)
    

    
    