from sqlalchemy import (Column,String,Integer,Boolean,Float,Date)
from .db import Base

class Cricketer(Base):
    __tablename__ = "cricketers_csv"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    country = Column(String)
    role = Column(String)
    batting_style = Column(String)
    bowling_style = Column(String)

    matches = Column(Integer)
    runs = Column(Integer)

    average = Column(Float)
    wickets = Column(Integer)
    strike_rate = Column(Float)
    economy = Column(Float)

    best_score = Column(String)
    is_active = Column(Boolean)
    join_date = Column(Date)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True , index=True)
    username = Column(String)
    password =  Column(String)
    role = Column(String)
    
    
