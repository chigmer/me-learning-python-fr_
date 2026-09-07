# Todo API
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

conn = sqlite3.connect("todos.db")
cursor = conn.cursor()
# create a table, ignore if it already exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        completed BOOLEAN DEFAULT FALSE
    )
""")
# pydantic model for request body
class TodoItem(BaseModel):
    id: int
    title: str
    description: str
    completed: bool



app = FastAPI()



# read everything from the database and return it as a list of dictionaries, root endpoint
@app.get("/")
def read_todos():
    cursor.execute("SELECT * FROM todos")
    todos = cursor.fetchall()
    return {"todos": todos}



# read one specific todo if you provide the id, otherwise return 404
@app.get("/todos/{todo_id}")
def read_todo(todo_id: int):
    cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
    todo = cursor.fetchone()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return {"todo": todo}

# create a todo item on endpoint /todos/ with a post request, the request body should be a json object with the following fields: id, title, description, completed
@app.post("/todos/")
def create_todo(todo: TodoItem):
    cursor.execute("INSERT INTO todos (id, title, description, completed) VALUES (?, ?, ?, ?)",
                   (todo.id, todo.title, todo.description, todo.completed))
    conn.commit()
    return {"message": "Todo item created successfully"}

# update a todo item on endpoint /todos/{todo_id} with a put request, the request body should be a json object with the following fields: title, description, completed
# recommendation: just change the completed field to true or false, and the title and description the same, but you can change them if you want to. 
# The id field should not be changed, because it is the primary key of the table and it is used to identify the todo item.
#  If you want to change the id, you should delete the todo item and create a new one with the new id.
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoItem):
    cursor.execute("UPDATE todos SET title = ?, description = ?, completed = ? WHERE id = ?",
                   (todo.title, todo.description, todo.completed, todo_id))
    conn.commit()
    return {"message": "Todo item updated successfully"}



# delete a todo item on endpoint /todos/{todo_id} with a delete request, the request body should be empty
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    return {"message": "Todo item deleted successfully"}