from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3


class Todo(BaseModel):
    title: str
    description: str
    status: bool = False

app = FastAPI()


with sqlite3.connect("todos.db") as conn:
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS todos(

    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    completed INTEGER CHECK(completed = 0 OR completed = 1)
    
    )""")
@app.get("/")
def read_todos():
    with sqlite3.connect("todos.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM todos")
    data = cur.fetchall()
    if data:
         return data
    else:
         return {"message": "no todos yet, visit /docs to create one"}
@app.post("/todos/")
def add_todo(todo: Todo):
    with sqlite3.connect("todos.db") as conn:
            cur = conn.cursor()
            try:
                 cur.execute("""INSERT INTO todos (title,description,completed) VALUES (?,?,?)""", 
                             (todo.title,todo.description,todo.status)
                             )
                 return {"message": "To-Do written successfully!"}
            except Exception as e:
                 return {"error": e}
                


