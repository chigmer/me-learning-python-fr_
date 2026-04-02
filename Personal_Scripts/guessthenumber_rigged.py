#i wanted guess the number, but this is even better.

import random
def is_num_what_my_number_is(num:int=0) :
    if not isinstance(num,int):
        raise ValueError("INTEGER is the argument")
    elif num < 0:
        raise TypeError("must be a positive integer too")
    my_num = random.randint(1,999)
    if num == my_num:
        print(f"ahh, you guessed correct. good for you\nthe number was {my_num}")
        return True
    else:
        print(f"wrong. you are off by {my_num - num} ")
for i in range(100000):
    print(f"current guess, {i}")
    correct = is_num_what_my_number_is(i)
    if correct:
        break
#i just made a more complicated version of guess the number