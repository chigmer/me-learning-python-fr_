import requests

url = "http://127.0.0.1:8000"
id = 1
content = {"completed": True}

res = requests.patch(f"{url}/todos/{id}",json=content)
print(res.json())