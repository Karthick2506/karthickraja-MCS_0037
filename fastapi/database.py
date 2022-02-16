from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# import  models

#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@127.0.0.1:5432/testing"

SQLALCHEMY_DATABASE_URL = "mysql://root:admin@localhost/player_stats"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def insert_player(new_player,db):
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return 'Data inserted successfully'




