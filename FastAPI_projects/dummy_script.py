     
dump =  {
        "title": "Learn FastAPI",
        "description": "Learn how POST requests work",
        "status": False
    }

data = [x for x in dump.items() if x[1] is not None]
columns = []
values = []
for i in data:
     columns.append(i[0])
     values.append(i[1])
         # i assume its [("title","example_str"),...]
            
query = f"UPDATE todos SET {" = ?,".join(columns)} WHERE id = ?"
print(query)
        
             