import json

# This is a normal Python Dictionary (from MOOC Part 1)
user_data = {
    "name": "Alex",
    "completed_mooc": True,
    "parts_finished": 1
}
print(user_data)

# This one line converts it to a JSON string!
json_output = json.dumps(user_data)

print(json_output)
# Output: {"name": "Alex", "completed_mooc": true, "parts_finished": 1}
