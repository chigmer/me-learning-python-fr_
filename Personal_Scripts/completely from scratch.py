#make smth that counts down from 100 w/o help
#use time.sleep for dramatic effect
#ill probably use the while command to loop 100 times


import time

count = 101

while count > 0:
     count -= 1
     time.sleep (0.3)
     print(count)
     
if count == 0:
    time.sleep(0.5)
    print ("Yay!")   
