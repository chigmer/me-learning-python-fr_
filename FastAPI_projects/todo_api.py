from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3


class Todo(BaseModel):
    title: str
    description: str
    status: bool = False
class Update_Todo(BaseModel):
         title: str | None = None
         description: str | None = None
         completed: bool |None = None

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
@app.patch("/todos/{id}")
def update_todo(id: int, todo: Update_Todo):
    with sqlite3.connect("todos.db") as conn:
        cur = conn.cursor()
        #try to update row with id param, return 404 if it doesnt exist?
        #if a value is set to null in the pydantic model, ignore that column
        try:
            dump = todo.model_dump()
            data = {key: value for key, value in dump.items() if value is not None}
            column_q = []
            values = tuple(list(data.values()) + [id])

            for k in data.keys():
                column_q.append(f"{k} = ?")
        # There is nothing to update.
            
            if not data:
                raise HTTPException(status_code=400, detail="No fields to update")

            # i assume its [("title","example_str"),...]
            
            query = f"UPDATE todos SET {", ".join(column_q)} WHERE id = ?"
            cur.execute(query,values)
            

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"server error, sorry! \nerror: {e}")
    return {"message": "updated successfully"}

# 9/21, making progress on delete ig

@app.delete("/todos/{id}")
def delete_todo(id: int):
    with sqlite3.connect("todos.db") as conn:
        cur = conn.cursor()
        try:
            cur.execute("""DELETE from todos WHERE id = ?""",(id,))
            return {"message":"todo deleted successfully."}
        except:
            return HTTPException(status_code=400,detail="Deletion could not be completed, check the ID inputted")
     
            

    
     
                


