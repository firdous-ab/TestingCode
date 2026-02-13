import requests
from typing import Any, Dict, Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Ajoke's": "World"}
