#copying the convenient code from my password maker.
#https://docs.python.org/3.12/library/datetime.html
from datetime import datetime
import sys

today = datetime.now().strftime("%r ")
date = datetime.now().strftime("%B %d, %Y")
print(f"the time is.. {today}")
print("would you like to save this information? (Y/n) \n \n")

while True:
    try:
        answer = input(">")
        if answer.lower().strip() == "y":
            notes = input("Notes? ")
            break
        elif answer.lower().strip() == "n":
            print("kay")
            sys.exit()
        else:
            print("pardon?")
    except KeyboardInterrupt:
        sys.exit()
    
try:
    with open("dates.txt","a" ) as D:
        D.write("\n")
        D.write(f"user typed this on {date}{today}")
        D.write("\n") 
        D.write(f"user said: {notes}")
        D.write("\n")
except Exception as msg:
    print("error occurred: " + msg)
    sys.exit()
print("done!!")