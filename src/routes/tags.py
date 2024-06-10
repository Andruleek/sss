from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from .repository import ContactRepository

app = FastAPI()

repository = ContactRepository()

@app.get("/tags/")
async def get_all_tags():
    return JSONResponse(content=repository.get_all_contacts(), media_type="application/json")

@app.get("/tags/{tag_id}")
async def get_tag(tag_id: int):
    tag = repository.get_contact(tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return JSONResponse(content=tag, media_type="application/json")

@app.post("/tags/")
async def create_tag(tag: dict):
    new_tag = Contact(**tag)
    repository.create_contact(new_tag)
    return JSONResponse(content={"message": "Tag created successfully"}, media_type="application/json")

@app.put("/tags/{tag_id}")
async def update_tag(tag_id: int, tag: dict):
    tag_to_update = repository.get_contact(tag_id)
    if not tag_to_update:
        raise HTTPException(status_code=404, detail="Tag not found")
    for key, value in tag.items():
        setattr(tag_to_update, key, value)
    repository.update_contact(tag_to_update)
    return JSONResponse(content={"message": "Tag updated successfully"}, media_type="application/json")

@app.delete("/tags/{tag_id}")
async def delete_tag(tag_id: int):
    tag = repository.get_contact(tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    repository.delete_contact(tag_id)
    return JSONResponse(content={"message": "Tag deleted successfully"}, media_type="application/json")