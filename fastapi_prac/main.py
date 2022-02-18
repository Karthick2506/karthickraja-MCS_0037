from fastapi import FastAPI, Depends
import uvicorn
from schemas import Student, StudentResponse
from service import service_insert, service_retrive, service_retrieve_one, service_update, service_delete
from database import engine
from typing import List
from utils import get_db
from sqlalchemy.orm import Session


import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post('/insert', status_code=201)
def insert_data(st: Student, db: Session = Depends(get_db)):
    total = st.english + st.tamil + st.physics + st.chemistry + st.biology + st.maths
    avg =(total/600) *100
    if(avg>=90):
        grade = "DISTINCTION"
    elif (70 <= avg < 90):
        grade = "GOLD MEDAL"
    elif (30 <= avg < 70):
        grade = "PASS"
    elif (30 < avg):
        grade = "FAIL"
    else:
        grade = "FAIL"

    new_student = models.Marks_details(id=st.id,
                                       name=st.name,
                                       english=st.english,
                                       tamil=st.tamil,
                                       physics=st.physics,
                                       chemistry=st.chemistry,
                                       biology=st.biology,
                                       maths=st.maths,
                                       total=total,
                                       grade=grade,

                                       )
    return service_insert(new_student, db)

@app.get('/retrieve',status_code=200, response_model = List[StudentResponse])
def retrieve_data(db : Session = Depends(get_db)):
    return service_retrive(db)

@app.get('/retrieve/{id}',status_code=200, response_model = StudentResponse)
def retrieve_data(id:int, db : Session = Depends(get_db)):
    return service_retrieve_one(id,db)


@app.put('/update')
def update_data(st: Student, db: Session = Depends(get_db)):
    id = st.id
    name = st.name
    english = st.english
    tamil = st.tamil
    physics = st.physics
    chemistry = st.chemistry
    biology = st.biology
    maths = st.maths
    total = english + tamil + physics + chemistry + biology + maths
    avg = (total / 600) * 100
    chance_given = 1
    if (avg >= 90):
        grade = "DISTINCTION"
    elif (70 <= avg < 90):
        grade = "GOLD MEDAL"
    elif (30 <= avg < 70):
        grade = "PASS"
    elif (30 < avg):
        grade = "FAIL"
    else:
        grade = "FAIL"

    return service_update(id, name, english, tamil, physics, chemistry, biology, maths, total, grade, db)

@app.delete('/delete/{id}')
def delete_data(id:int,db : Session = Depends(get_db)):
    return service_delete(id,db)

if __name__ == '__main__':
    uvicorn.run(app)