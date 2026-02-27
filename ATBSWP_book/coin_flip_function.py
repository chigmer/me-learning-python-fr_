import random

def coin_flip(iter): #short for iterations
    H = 0
    T = 0
    for _ in range(iter):
        
        result = random.randint(0,1) #used random.randint() since the book uses it (i know intuitively, that random.choice is better.)
        if result == 0:
            H += 1
        elif result == 1:
            T += 1
    return f"Heads: {H}", f"Tails {T}"
          
        
 
    
    
    
if __name__ == "__main__":
        
        for i in range(10):
            a = coin_flip(10)
            print(a)
        
   
    

