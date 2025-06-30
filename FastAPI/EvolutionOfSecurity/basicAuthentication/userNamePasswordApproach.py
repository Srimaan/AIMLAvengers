from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app: FastAPI = FastAPI();
user_db: dict = {} #In-memory database for users to store username and password pairs


class User(BaseModel):
    username: str
    password: str

@app.post("/register")
def register(user: User):
    if user.username in user_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    else:user_db[user.username] = user.password
    return {"message": "User registered successfully"}

@app.post("/login")
def login(user: User):
    if not user.username or not user.username.strip():
        raise HTTPException(status_code=400, detail="Username is required")
    if not user.password or not user.password.strip():
        raise HTTPException(status_code=400, detail="Password is required")

    stored_password: str = user_db.get(user.username)
    if not stored_password:
        raise HTTPException(status_code=400, detail="Username is not registered")
    if stored_password != user.password:
        raise HTTPException(status_code=400, detail="Invalid password")
    return {"message": "Login successful"}
