from database import Base
from sqlalchemy import Column,Integer, String


class Marks_details(Base):
    __tablename__ = 'Results'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    english = Column(Integer)
    tamil = Column(Integer)
    physics = Column(Integer)
    chemistry = Column(Integer)
    biology = Column(Integer)
    maths = Column(Integer)
    total = Column(Integer)
    grade = Column(String(20))


