from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Todo API", version="1.0.0")

class Todo(BaseModel):
    id: int
    title: str

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    """Get a todo by ID"""
    return {"id": todo_id, "title": "Test 6"}

@app.post("/todos")
def create_todo(todo: Todo):
    """Create a new todo"""
    return todo
