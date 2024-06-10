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