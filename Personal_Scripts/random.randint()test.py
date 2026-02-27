#random.randint(test)
import random

def dice(num):
    if not isinstance(num,int) or num <= 0:
        print("i need a positive integer")
        return
    num = int(num)
    result = random.randint(1,num)
    return result
    
    
if __name__ == "__main__":
    print(dice(10))
    print(dice(1))
    print(dice("yes"))
    print(f"the result is {dice(123)}")