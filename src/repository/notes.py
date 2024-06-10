from sqlalchemy.orm import sessionmaker
from .models import Contact

class ContactRepository:
    def __init__(self):
        self.session = sessionmaker(bind=engine)()

    def get_all_contacts(self):
        return self.session.query(Contact).all()

    def get_contact(self, contact_id):
        return self.session.query(Contact).filter(Contact.id == contact_id).first()

    def create_contact(self, contact):
        self.session.add(contact)
        self.session.commit()

    def update_contact(self, contact):
        self.session.commit()

    def delete_contact(self, contact_id):
        contact = self.get_contact(contact_id)
        if contact:
            self.session.delete(contact)
            self.session.commit()
            
            
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
