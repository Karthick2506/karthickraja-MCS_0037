from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


# creating Object
obj = FastAPI()

# /hello -- Endpoint
# localhost -- base URL

# creating Endpoint

@obj.get("/")
def home():
    return {"Data": "Test"}
#@obj.get("/about/{id}") # path parameter
#def about(id):
    #return {"id":id}
#@obj.get("/about/")
#def read(number:int, text:str): # Query parameter
    #return {"number": number, "text": text}

#@obj.post("/package/{priority}")
#def package(priority:int, package:Package):
    #return {"priority": priority, **package.dict()}
@obj.post("/items/")    
class Item(BaseModel):
    name: str
    price: int
    description: Optional[str] = None
def create_item(item: Item):
    return item


 








