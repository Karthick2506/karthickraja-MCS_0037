from database import SessionLocal
import models
from models import Cricket

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def database_retrieve(db):
    user_data = db.query(models.Cricket).filter(Cricket.jersey_no >= 0)
    response = {}
    out_res =[]
    for each in user_data:
        response['jersey_no'] = each.jersey_no
        response['pname'] = each.pname
        response['runs'] = each.runs
        out_res.append(response)
    return out_res






