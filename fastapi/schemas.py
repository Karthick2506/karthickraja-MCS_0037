from pydantic import BaseModel

class Cric(BaseModel):
    jersey_no : int
    pname : str
    runs : int

class Cricket_player(BaseModel):
    jersey_no : int
    pname : str
    runs : int