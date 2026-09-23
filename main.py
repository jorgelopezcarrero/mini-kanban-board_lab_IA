from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    status: str = "Todo"

tasks_db = []

@app.get("/tasks")
def get_tasks():
    return tasks_db

@app.post("/tasks")
def create_task(task: Task):
    tasks_db.append(task)
    return task
