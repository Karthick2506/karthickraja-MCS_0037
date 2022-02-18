from database import SessionLocal
import models
from models import Marks_details

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def database_retrive(db):
    user_data = db.query(models.Marks_details).all()
    out_res = []
    for each in user_data:
        response = {}
        response['id'] = each.id
        response['name'] = each.name
        response['english'] = each.english
        response['tamil'] = each.tamil
        response['physics'] = each.physics
        response['chemistry'] = each.chemistry
        response['biology'] = each.biology
        response['maths'] = each.maths
        response['total'] = each.total
        response['grade'] = each.grade
        out_res.append(response)
    return out_res

def database_retrive_one(id,db):
    user_data = db.query(Marks_details).filter(Marks_details.id == id).first()
    response = {}
    response['id'] = user_data.id
    response['name'] = user_data.name
    response['english'] = user_data.english
    response['tamil'] = user_data.tamil
    response['physics'] = user_data.physics
    response['chemistry'] = user_data.chemistry
    response['biology'] = user_data.biology
    response['maths'] = user_data.maths
    response['total'] = user_data.total
    response['grade'] = user_data.grade
    return response

def database_update(id, name, english, tamil, physics, chemistry, biology,maths,total, grade,db):
    update_obj = db.query(Marks_details).filter(Marks_details.id == id).first()
    update_obj.id = id
    update_obj.name = name
    update_obj.english = english
    update_obj.tamil = tamil
    update_obj.physics = physics
    update_obj.chemistry = chemistry
    update_obj.biology = biology
    update_obj.maths = maths
    update_obj.total = total
    update_obj.grade = grade
    db.add(update_obj)
    db.commit()
    db.refresh(update_obj)
    return "data updated successfully"


def database_delete(id,db):
    if db.query(Marks_details).filter(Marks_details.id == id).delete():
        db.commit()
        return "Deleted successfully"
    else:
        return 'user not found'