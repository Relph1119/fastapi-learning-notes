from fastapi import FastAPI

from api import admin, login

app = FastAPI()

app.include_router(admin.router, prefix="/ch07")
app.include_router(login.router, prefix="/ch07")


@app.get("/index")
def index():
    return {"content": "welcome"}

# ch07h
