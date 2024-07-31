"""
This module contains the main functionality of the application.
It provides the core features and implements the primary logic.
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/name")
def get():
    return "this is my name"

