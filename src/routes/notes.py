from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from .repository import ContactRepository

app = FastAPI()

repository = ContactRepository()

@app.get("/contacts/")
async def get_all_contacts():
    return JSONResponse(content=repository.get_all_contacts(), media_type="application/json")

@app.get("/contacts/{contact_id}")
async def get_contact(contact_id: int):
    contact = repository.get_contact(contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return JSONResponse(content=contact, media_type="application/json")

@app.post("/contacts/")
async def create_contact(contact: dict):
    new_contact = Contact(**contact)
    repository.create_contact(new_contact)
    return JSONResponse(content={"message": "Contact created successfully"}, media_type="application/json")

@app.put("/contacts/{contact_id}")
async def update_contact(contact_id: int, contact: dict):
    contact_to_update = repository.get_contact(contact_id)
    if not contact_to_update:
        raise HTTPException(status_code=404, detail="Contact not found")
    for key, value in contact.items():
        setattr(contact_to_update, key, value)
    repository.update_contact(contact_to_update)
    return JSONResponse(content={"message": "Contact updated successfully"}, media_type="application/json")

@app.delete("/contacts/{contact_id}")
async def delete_contact(contact_id: int):
    contact = repository.get_contact(contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    repository.delete_contact(contact_id)
    return JSONResponse(content={"message": "Contact deleted successfully"}, media_type="application/json")