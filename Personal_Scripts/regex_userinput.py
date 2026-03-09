import time as t
from wordlist import words
import random
print("type these words in order.\n\n")

wordbank = []
playerbank = []
for _ in range(5):
    wordbank.append(random.choice(words))
     
for attempt in range(5):
    print(wordbank[attempt])
    playerbank.append(input(">").strip())
#the user is at fault for wrong capitalization   


   

if playerbank == wordbank:
    print("\nhello user \n")
    t.sleep(.99)
    print("you finally followed instructions.\n")
    t.sleep(1)
    print("good for you.")
else:
    print("\nshame on you")
    

#if youre wondering about the regex thing. a simple if user == "string": could do the job but im literally doing this for a learning experience
#update: fuckkkk, im scrapping the regex thing. i just cant stand letting go of an easier and cleaner alternative.
#misleading filename. its called regexuserinput.py, im not bothering to change it anytime soon
    
