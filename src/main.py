from fastapi import FastAPI
from pydantic import BaseModel

from src.entities.user import User
from src.entities.history import History



app = FastAPI()

class UserModel(BaseModel):
    id: int
    nickname: str
    password: str
    password_salt: str

class UserCreate(BaseModel):
    nickname: str
    password: str

@app.post("/users", response_model=UserModel, summary="Cria um usuário", tags=['User'])
async def create_user(body: UserCreate):
    return User.create(body.nickname, body.password)

@app.get("/users", response_model=list[UserModel], summary="Lista usuários", tags=['User'])
async def list_users():
    return User.list_users()

@app.get("/users/{id}", response_model=UserModel, summary="Obtem um usuário por ID", tags=['User'])
async def get_user(id: int):
    return User.get_by_id(id)


class UserUpdate(UserCreate):
    pass

@app.put("/users/{id}", response_model=UserModel, summary="Atualiza um usuário por ID", tags=['User'])
async def update_user(id: int, body: UserUpdate):
    user =  User.get_by_id(id)
    
    user.nickname = body.nickname
    user.update_password(body.password)
    
    user.save()

    return user

@app.delete("/users/{id}", summary="Deleta um usuário por ID", tags=['User'])
async def delete_user(id: int):
    user = User.get_by_id(id)
    return user.delete()


class HistoryModel(BaseModel):
    id: int
    title: str
    summary: str
    category: str
    content: str
    user_id: int
    moment: str
class HistoryCreate(BaseModel):
    title: str
    summary: str
    category: str
    content: str
    user_id: int

@app.post("/histories", response_model=HistoryModel, summary="Cria uma história", tags=['History'])
async def create_history(body: HistoryCreate):
    return History.create(body.title, body.summary, body.category, body.content, body.user_id)

@app.get("/histories", response_model=list[HistoryModel], summary="Lista histórias", tags=['History'])
async def list_histories():
    return History.list_histories()

@app.get("/histories/{id}", response_model=HistoryModel, summary="Obtem uma história por ID", tags=['History'])
async def get_history(id: int):
    return History.get_by_id(id)


class HistoryUpdate(BaseModel):
    title: str
    summary: str
    category: str
    content: str

@app.put("/histories/{id}", response_model=HistoryModel, summary="Edita uma história por ID", tags=['History'])
async def update_history(id: int, body: HistoryUpdate):
    history = History.get_by_id(id)
    
    history.title = body.title
    history.summary = body.summary
    history.category = body.category
    history.content = body.content

    history.save()

    return history

@app.delete("/histories/{id}", summary="Deleta uma história por ID", tags=['History'])
async def delete_history(id: int):
    history = History.get_by_id(id)
    return history.delete()

class AddHistoryPart(BaseModel):
    part: str

@app.post("/histories/{id}/add-part", response_model=HistoryModel, summary="Adiciona trechos à história com o GPT", tags=['History'])
async def add_contet_history(id: int, body: AddHistoryPart):
    history = History.get_by_id(id)
    history.add_part_and_merge_with_gpt(body.part)
    return history