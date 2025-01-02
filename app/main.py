

from fastapi import FastAPI
from app.routers import task, user
from app.backend.db import engine, Base
from app.models.user import User
from app.models.task import Task

app = FastAPI()

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine) # Создаем таблицы в базе данных

@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}

# Подключение маршрутов
app.include_router(task.router, prefix="/task", tags=["task"])
app.include_router(user.router, prefix="/user", tags=["user"])