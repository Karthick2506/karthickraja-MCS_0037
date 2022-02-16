from database import Base
from sqlalchemy import Column, Integer, String

class Cricket(Base):
    __tablename__ = 'scoreboard'
    jersey_no = Column(Integer, primary_key = True)
    pname =Column(String(40))
    runs =Column(Integer)
