"""
This module contains the main functionality of the application.
It sets up a FastAPI application with a single endpoint for retrieving a name.
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/name")
def get_name():
    """
    Retrieve the name for the application.

    Returns:
        str: A string containing the name of the application.
    """
    return "hey chiru how are you i am the mohan i am at your village  and come let enjoy"
