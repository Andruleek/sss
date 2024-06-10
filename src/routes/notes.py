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

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify([contact.__dict__ for contact in repository.get_contacts_by_birthday()])

@app.route('/contacts/name/<string:name>', methods=['GET'])
def get_contact_by_name(name):
    contact = repository.get_contact_by_name(name)
    if contact:
        return jsonify(contact.__dict__)
    else:
        return jsonify({'error': 'Contact not found'}), 404

@app.route('/contacts/surname/<string:surname>', methods=['GET'])
def get_contact_by_surname(surname):
    contact = repository.get_contact_by_surname(surname)
    if contact:
        return jsonify(contact.__dict__)
    else:
        return jsonify({'error': 'Contact not found'}), 404

@app.route('/contacts/email/<string:email>', methods=['GET'])
def get_contact_by_email(email):
    contact = repository.get_contact_by_email(email)
    if contact:
        return jsonify(contact.__dict__)
    else:
        return jsonify({'error': 'Contact not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

