from pydantic import BaseModel

class Contact(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str
    birthday: str