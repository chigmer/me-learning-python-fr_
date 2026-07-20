#run a function N amount of times
import random, time
def retry(num,delay=None):   
    """Usage: retry(retry attempts, delay[default is None])"""
    def decorator(func):
        #print("decorator running")
        def wrapper():           
            #print("wrapper running")
            nonlocal num
            while num:
                try:
                    func()
                    return
                except Exception as e: 
                    print(e)
                    if delay:
                                        
                        time.sleep(delay)
                    num -= 1
            
                    
                                                          
        return wrapper
    return decorator

#(retry(5))(main)
if __name__ == "__main__":
    @retry(5)
    def main():
        if random.random() <= 0.2345:
            raise Exception
        else:
            print("success.")
    
