from fastapi import FastAPI
from pydantic import BaseModel

from src.entities.user import User
from src.entities.history import History



app = FastAPI()

class UserCreate(BaseModel):
    nickname: str
    password: str

@app.post("/users")
async def create_user(body: UserCreate):
    return User.create(body.nickname, body.password)

@app.get("/users")
async def list_users():
    return User.list_users()

@app.get("/users/{id}")
async def get_user(id: int):
    return User.get_by_id(id)


class UserUpdate(UserCreate):
    pass

@app.put("/users/{id}")
async def update_user(id: int, body: UserUpdate):
    user =  User.get_by_id(id)
    
    user.nickname = body.nickname
    user.update_password(body.password)
    
    user.save()

    return user

@app.delete("/users/{id}")
async def delete_user(id: int):
    user = User.get_by_id(id)
    return user.delete()


class HistoryCreate(BaseModel):
    title: str
    summary: str
    category: str
    content: str
    user_id: int

@app.post("/histories")
async def create_history(body: HistoryCreate):
    return History.create(body.title, body.summary, body.category, body.content, body.user_id)

@app.get("/histories")
async def list_histories():
    return History.list_histories()

@app.get("/histories/{id}")
async def get_history(id: int):
    return History.get_by_id(id)


class HistoryUpdate(BaseModel):
    title: str
    summary: str
    category: str
    content: str

@app.put("/histories/{id}")
async def update_history(id: int, body: HistoryUpdate):
    history = History.get_by_id(id)
    
    history.title = body.title
    history.summary = body.summary
    history.category = body.category
    history.content = body.content

    history.save()

    return history

@app.delete("/histories/{id}")
async def delete_history(id: int):
    history = History.get_by_id(id)
    return history.delete()

class AddHistoryPart(BaseModel):
    part: str

@app.post("/histories/{id}/add-part")
async def add_contet_history(id: int, body: AddHistoryPart):
    history = History.get_by_id(id)
    history.add_part_and_merge_with_gpt(body.part)
    return history