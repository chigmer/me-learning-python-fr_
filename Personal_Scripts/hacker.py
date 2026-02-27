#hacker
import time
import random
def print_color(text):
   if not isinstance(text,str):
       print("type a string.")
       return
   return f"\033[32m{text}"   # green text in terminal
    #felt like making a function today

    
hacker = r"`~1234567890-=_!@#$%^&*()_+qwertyuiopQWERTYUIOP[]\{}|asdfghjklASDFGHJKL;:zxcvbnmZXCVBNM,./<>?qwertyuiopQWERTYUIOPasdfghjklASDFGHJKLzxcvbnmZXCVBNM69"
#higher chance for 69 because I can


start = time.time()
duration = 15#seconds
while time.time() - start < duration:
    print(print_color(random.choice(hacker)), end = "", flush=True)
    time.sleep(0.0019999)

    
    
    
    #takeaways, I searched how to run a loop for a specific amount of time, how to turn text green, why return exists, how to stop buffering in py, and the fact that imgonna forgetthis anyway



    

