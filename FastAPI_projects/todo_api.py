from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3


class Todo(BaseModel):
    title: str
    description: str
    status: bool = False
class Update_Todo(BaseModel):
         title: str | None
         description: str | None
         status: bool |None

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
         return {"todos": data}
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


# put is next
@app.put("/todos/{id}")
def update_todo(id: int, todo: Update_Todo):
    with sqlite3.connect("todos.db") as conn:
        cur = conn.cursor()
        #try to update row with id param, return 404 if it doesnt exist?
        #if a value is set to null in the pydantic model, ignore that column
        try:
            dump = todo.model_dump()
            data = [x for x in dump.items() if x[1] is not None]
            columns = []
            values = []
            for i in data:
                 columns.append(i[0])
                 values.append(i[1])
            # i assume its [("title","example_str"),...]
            
            query = f"UPDATE todos SET ({" = ?,".join(columns)}) WHERE id = ?"
            print(query)
        except:
             pass

    
     
                


