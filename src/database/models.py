from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from .db import engine, Base

Base.metadata.create_all(engine)

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    phone_number = Column(String)
    birthday = Column(Date)