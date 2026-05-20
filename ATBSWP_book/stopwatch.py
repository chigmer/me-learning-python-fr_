import time,sys
import os


"""Instructions given to me:
    Find the current time by calling time.time() and store it as a timestamp at the start of the program, as well as at the start of each lap.
    
• Keep a lap counter and increment it every time the user presses enter. 

• Calculate the elapsed time by subtracting timestamps. 

• Handle the KeyboardInterrupt exception so that the user can press ctrl-C to quit."""
def now() -> float:
    return time.time()

    
print("Start Stopwatch? (y/n)\n")
while True:
    user = input(">").strip().lower()
    if user == "y":
        break
    elif user == "n":
        sys.exit(0)
    else:
        print("Invalid")
start = now()

print("Started..\n\n")
while True:
    try:
        current = now()
        #hours = int(current - start // 3600)
        #minutes = int(current - start// 60)
        TOTAL = int((current - start))
        hours = (TOTAL // 3600)
        minutes = (TOTAL % 3600) // 60
        seconds = TOTAL % 60 
        
        
        
        if hours > 0:
            
            print(f"\r{hours}{minutes:02}:{seconds:02}", end = '')
        else:
            print(f"\r{minutes:02}:{seconds:02}", end = '')
        time.sleep(1)
       
    except KeyboardInterrupt:
        print("exiting..")
        sys.exit(0)