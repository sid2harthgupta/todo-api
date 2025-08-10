from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Todo API", version="1.0.0")

class Todo(BaseModel):
    id: int
    title: str

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    """Retrieve a to-do by its ID."""
    return {"id": todo_id, "title": "Test 7"}

@app.post("/todos")
def create_todo(todo: Todo):
    """Create a new to-do."""
    return todo

@app.delete("/todos/{todo_id}")
def create_todo(todo_id: int):
    """Delete a to-do using its ID."""
    return None
