today_is_opposite_day = input("is it opposite day? (Y/n): ")


# Set say_it_is_opposite_day based on today_is_opposite_day:
if today_is_opposite_day == "Y":
    say_it_is_opposite_day = True
else:
    say_it_is_opposite_day = False

# If it is opposite day, toggle say_it_is_opposite_day:
if today_is_opposite_day == "Y":
    say_it_is_opposite_day = not say_it_is_opposite_day
else:
   say_it_is_opposite_day = True
   

# Say what day it is:
if say_it_is_opposite_day == True:
    print('Today is Opposite Day.')
else:
    print('Today is not Opposite Day.')