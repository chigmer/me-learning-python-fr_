#a function returns another callable function
import random
def random_greet():
    greet_list = "Hello Hi Howdy Wassup Yo".split(" ")
    
    def greet(name):
        print(f"{random.choice(greet_list)}, {name.title()}.")
    return greet
    
random_greet()("James")
    