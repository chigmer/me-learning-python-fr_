import requests


url = "http://127.0.0.1:8000/todos/"

todos = [
    {
        "title": "Learn FastAPI",
        "description": "Learn how POST requests work",
        "status": False
    },
    {
        "title": "Study Pydantic",
        "description": "Understand how models validate data",
        "status": True
    },
    {
        "title": "Build an API",
        "description": "Make a small Todo API with SQLite",
        "status": False
    }
]


for todo in todos:
    response = requests.post(url, json=todo)

    print("Status:", response.status_code)
    print("Response:", response.json())
    print()