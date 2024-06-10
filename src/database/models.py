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
    
    
from datetime import date, timedelta
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    birthday = Column(DateTime)

    def __repr__(self):
        return f"Contact(id={self.id}, name='{self.name}', surname='{self.surname}', email='{self.email}', birthday={self.birthday})"

# src/repository/notes.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.models import Contact

class ContactRepository:
    def __init__(self):
        self.engine = create_engine('sqlite:///contacts.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_contact_by_name(self, name):
        session = self.Session()
        contact = session.query(Contact).filter(Contact.name == name).first()
        session.close()
        return contact

    def get_contact_by_surname(self, surname):
        session = self.Session()
        contact = session.query(Contact).filter(Contact.surname == surname).first()
        session.close()
        return contact

    def get_contact_by_email(self, email):
        session = self.Session()
        contact = session.query(Contact).filter(Contact.email == email).first()
        session.close()
        return contact

    def get_contacts_by_birthday(self):
        session = self.Session()
        today = date.today()
        birthday_contacts = session.query(Contact).filter(Contact.birthday <= today + timedelta(days=7)).all()
        session.close()
        return birthday_contacts