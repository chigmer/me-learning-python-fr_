#count down from someones birthday 
from datetime import datetime

import time as t
def parse_seconds(total_seconds) -> tuple:
    hrs = total_seconds // 3600
    mins = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    return [int(val) for val in [hrs,mins,secs]]

def format_and_display_birthday(target:datetime) -> str:
    while True:        
        seconds = (target - datetime.now()).total_seconds()
        if seconds <= 0:
            break
        else:
            h,m,s = parse_seconds(seconds)                      
            parsed_days = int(seconds // 86400) #truncation strat
            days = f"{parsed_days} days left | " if parsed_days else ''
                      
            if h:
                print(f"\r{days}"+f"{h}:{m:02}:{s:02}",end='',flush=True)
            else:
                print(f"\r{days}"+f"{m:02}:{s:02}",end='',flush=True)
            
        t.sleep(1)
    
    
    
    
def validate_and_parse_input() -> bool:
    print("see --help for help\n\n")
    while True:
        user = input(">").strip()
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
    
    while True:        
        birthday = validate_and_parse_input()
        now = datetime.now()
        delta = birthday - now
        if delta.total_seconds() <= 0: #ensures value is not a past or present date 
            
            print("Birthday MUST be a future date.")
            continue
        else:
            break
    
    format_and_display_birthday(birthday)
    print("the birthday has arrived, Go get 'em tiger.")
if __name__ == "__main__":
    main()
    
    
