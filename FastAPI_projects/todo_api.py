from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3


class todo(BaseModel):
    id: int
    title: str
    description: str
    status: bool = False

app = FastAPI()


with sqlite3.connect("todos.db") as conn:
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS todos(
    
    )""")
@app.get("/")
def read_todos():
    with sqlite3.connect("todos.db") as conn:
        cur = conn.cursor()
    return


