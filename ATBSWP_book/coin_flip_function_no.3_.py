import random

def coin_flip(iter): #short for iterations
    H = 0
    T = 0
    for _ in range(iter):
        
        result = random.randint(0,1) #used random.randint() since the book uses it. (i know intuitively, that random.choice is better.)
        if result == 0:
            H += 1
        elif result == 1:
            T += 1
    print("Heads: " + str(H))
    print("Tails: " + str(T))
    
          
        
 
    
    
    
if __name__ == "__main__":
                coin_flip(1202)
                print("yo")
                
            
            
        
   
    

