import os
import sys
from pathlib import Path
from typing import Dict

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)