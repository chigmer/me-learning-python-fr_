#even odd shi

#check if a variable is odd or even
import time

print("welcome, i shall count whether your number is even or odd")

while True:

    number = input("Type your number here>")
    

    
    time.sleep(.3)


    number = int(number)
    half = number / 2

    if half == int(half):
        print ("even")
    else:
        print("odd")