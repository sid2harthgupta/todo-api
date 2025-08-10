from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Todo API", version="1.0.0")

class Todo(BaseModel):
    id: int
    title: str

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    """Get a to-do by ID."""
    return {"id": todo_id, "title": "Sample"}

@app.post("/todos")
def post_todo(todo: Todo):
    """Create a new to-do."""
    return todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    """Delete a to-do by ID."""
    return {"message": f"Todo {todo_id} deleted successfully"}

@app.get("/completed")
def completed_todos():
    """Get all completed to-dos."""
    return {
        "tasks": [
            {"id": 1, "title": "Sample 1"},
            {"id": 2, "title": "Sample 2"},
        ]
    }
