import time,sys
import threading
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")


"""Instructions given to me:
    Find the current time by calling time.time() and store it as a timestamp at the start of the program, as well as at the start of each lap.
    
• Keep a lap counter and increment it every time the user presses enter. 

• Calculate the elapsed time by subtracting timestamps. 

• Handle the KeyboardInterrupt exception so that the user can press ctrl-C to quit.

V2: add a lap counter"""
wants_lap = False
def now() -> float:
    return time.time()
def sniff_input():
    global wants_lap
    while True:
        input() #typing anything except return doesnt end input()
        wants_lap = True

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
threading.Thread(target=sniff_input,daemon=True).start()
clear()
print("Started..\n\n(press 'Enter' to time a lap)")

laps = 0
while True:
    try:
        reset = False
        current = now()
        #hours = int(current - start // 3600)
        #minutes = int(current - start// 60)
        TOTAL = int((current - start))
        hours = (TOTAL // 3600)
        minutes = (TOTAL % 3600) // 60
        seconds = TOTAL % 60 
        mc = str(round((current - start) - TOTAL,5)).split(".")[1]
                               
        
        

        if wants_lap:
            laps += 1            
            # moves up 1 line, the second deletes it
            print("\033[1A", end="")
            print("\033[2K", end="")
            if hours > 0:
                print(f"\rLap {laps}: {hours}:{minutes:02}:{seconds:02}.{mc}")
            else:
                print(f"\rLap {laps}: {minutes:02}:{seconds:02}.{mc}")
            
            wants_lap = False
            reset = True
            
        escape = '\r' #legacy
        if hours > 0:                          
           
            print(f"{escape}{hours}:{minutes:02}:{seconds:02}", end = '')
        else:
            print(f"{escape}{minutes:02}:{seconds:02}", end = '')
        time.sleep(0.09)
       
    except KeyboardInterrupt:
        print("exiting..")
        sys.exit(0)