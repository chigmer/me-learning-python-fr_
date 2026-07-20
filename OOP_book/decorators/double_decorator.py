import random
def decorator(func):    
    def wrapper(N):
        for _ in range(N):
            if func() <= 0.05:
                return False
        return True
        
        
    return wrapper
@decorator
def return_num():
    return random.random()
        
print(return_num(99))
        
        #this is genuinely pointless.
        
             
        
        
        
                