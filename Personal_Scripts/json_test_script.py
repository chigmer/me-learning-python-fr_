#Project Idea:
#make a script that uses persistent storage using json
import json
def load_json():
    try:
        with open("amount.json", "r") as f:
            data = json.load(f)
            return data
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        return {"amount": 0}        
def update_json(data):        
    amount = {"amount": data["amount"] + 1}
    with open("amount.json", "w") as f:
        json.dump(amount, f)            
def main():
    data = load_json()  #dict
    amount = data["amount"]
    update_json(data)
    print(f"Amount of times that you've executed this script: {amount}")
    
if __name__ == "__main__":
    main()
