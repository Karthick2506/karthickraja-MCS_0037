from fastapi import FastAPI,Depends
import uvicorn
import models
from schemas import Cric, Cricket_player
from sqlalchemy.orm import Session
from utils import get_db
from database import engine
from service import service_insert, service_retrieve
from typing import List

app =FastAPI()

models.Base.metadata.create_all(bind = engine)


@app.post('/insert')
def insert_player(cc:Cric, db: Session = Depends(get_db)):
    new_player = models.Cricket(jersey_no = cc.jersey_no, pname = cc.pname, runs = cc.runs)
    return service_insert(new_player, db)

@app.get('/retrieve', response_model=List[Cricket_player])
def retrieve_data(db: Session = Depends(get_db)):
    return service_retrieve(db)





if __name__ == '__main__':
    uvicorn.run(app)