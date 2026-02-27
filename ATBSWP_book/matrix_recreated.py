import random
import sys
import time

width = 75

try:
    column = [0] * width
    while True:
        for i in range(width):
            if random.randint(20,69) == 69:
                column[i] = random.randint(4,17)
            
            if column[i] == 0:
                print(" ", end="")
            else:
                print(random.choice([0,1]), end="")
                
                column[i] -= 1 
        time.sleep(0.1)
        print()
                
            
        
                
                
            
        
                
    
    
except KeyboardInterrupt:
    sys.exit()
    