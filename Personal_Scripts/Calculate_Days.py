#How many days left until a date?
from datetime import datetime

def calculate_days(target:datetime) -> int:
          
    days = (target.date() - datetime.now().date()).days
                                   
    return days
                      
            
    
    
    
    
def validate_and_parse_input() -> datetime:
    print("see --help for help\n\n")
    while True:
        user = input("TARGET>").strip()
        if user == "--help":
            print("Usage: <YYYY> <MM> <DD> ")    
            print("Valid Separators: \" \", \"/\", and \"-\" ")  
            print("What this is:\n\n<placeholder>")
            continue       
        elif " " in user:
            user = user.split(" ")
        elif "/" in user:
            user = user.split("/")
        elif "-" in user:
            user = user.split("-")    
            
         
        try:
            year = int(user[0])
            month = int(user[1])
            day = int(user[2])
        except ValueError:
            print("invalid value.")
            continue
        except IndexError:
            print("Expected 3 values.")
            continue
        try:
            birthday = datetime(year,month,day)
        except ValueError as err:
            print(f"invalid date format: {err}")
            continue
        return birthday
#FORMAT: YYYY/MM/DD
def main():            
    target = validate_and_parse_input()   
    days = calculate_days(target)
    if days < 0:
        print(f"the target was {days * -1} {'days' if days < -1 else 'day'} ago")
    elif days > 0:
        print(f"the target is {days} {'days' if days > 1 else 'day'} from now.")
    else:
        print("The target is today.")
        
    
        
       
if __name__ == "__main__":
    main()
    
    
