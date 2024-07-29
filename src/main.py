from fastapi import FastAPI

app = FastAPI()


@app.get("/name")
def get():
    return "this is my name"
