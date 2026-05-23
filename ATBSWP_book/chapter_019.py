"""Practice Questions

1. What is the Unix epoch? 
2. What function returns the number of seconds since the Unix epoch?
3. What time module function returns a human-readable string of the current time, like 'Mon Jun 15 14:00:38 2026'?
4. How can you pause your program for exactly ﬁve seconds? 
5. What does the round() function return? 
6. What is the difference between a datetime object and a timedelta object? 
7. Using the datetime module, what day of the week was January 7, 2019?"""

"""
1. a number measured in seconds, starting from January 1, 1970 exactly
2. time.time()
3. time.ctime(), not the same module but strftime() also does the same thing but with a datetime object
4. time.sleep(5), 5 seconds in function sleep()
5. a rounded-up integer of the argument when no second arg is provided, or a rounded float with n decimals based on the second arg (brain melt)
6. a datetime is a specific point in time, a timedelta is a duration of time
7. i dont remember that method (well, now i do), i used isoweekday(). its a Monday
"""