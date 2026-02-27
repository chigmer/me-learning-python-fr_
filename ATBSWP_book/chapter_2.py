print("1 What are the two Boolean values? How are they written?", end = "")
print(" True and False with the first letter strictly capitalized")
print()

print("2 What are the three Boolean operators?", end = "")
print(" and, or, not")
print()

print("3 Write the truth tables for each Boolean operator.",end="")
print()
print("and –>  True and True = True, True and False = False, False and True = False, False and False = False.  or –> True or True = True, True and False = True, False and True = True, False and False = False not –> not always flips a boolean value, not not cool, right?")
print()



print("4 Evaluate: (5>4) and (3==5); not(5>4); (5>4) or (3==5); not((5>4) or (3==5)); (True and True) and (True==False); (not False) or (not True)")
print(" 1. False 2. False 3. True 4. False 5. False 6. True")
print()
print("5 What are the six comparison operators?")
print("  ==, <, >, <=, >=, !=")
print()
print("6 Difference between == and = ?")
print(" == is comparison, = is assignment")
print()
print("7 What is a condition and where is it used?")
print("a condition is code that evaluates to a boolean value, its used in if-elif-else statements 80% of the time")
print()
print("8 Identify the three blocks in the spam example.")

spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
       print('bacon')
    else:
        print('ham')
    print('spam')
print('Done')

print("im not typing the whole block again, but ig ill use the keywords used for the blocks")
print()
print("1. if 2. if 3. else")
print()

print("9 Write code that prints Hello if spam==1, Howdy if spam==2, else Greetings!")
print()

spam_ = 1 #try to change this if u want
if spam_ == 1:
    print("Hello")
elif spam_ == 2:
    print("Howdy")
else:
    print("Greetings!")