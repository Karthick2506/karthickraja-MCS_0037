from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    english: int
    tamil: int
    physics: int
    chemistry: int
    biology: int
    maths: int

class StudentResponse(BaseModel):
    id : int
    name : str
    english:int
    tamil:int
    physics:int
    chemistry:int
    biology:int
    maths:int
    total : int
    grade : str

    class Config:
        orm_mode = True
