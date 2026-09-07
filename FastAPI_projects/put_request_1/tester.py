import requests
url = "http://127.0.0.1:8000"
res = requests.post(f"{url}/todos/", json={"id": 1, "title": "make a todo", "description": "This is a test todo", "completed": False})
print(res)

