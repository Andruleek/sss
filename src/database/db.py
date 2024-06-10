from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

engine = create_engine('sqlite:///contacts.db')
Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    phone_number = Column(String)
    birthday = Column(Date)