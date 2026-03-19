"""
 Practice Questions 1. Why are functions advantageous to have in your programs? 2. When does the code in a function execute: when the function is defined or when the function is called? 3. What statement creates a function? 4. What is the difference between a function and a function call? 5. How many global scopes are there in a Python program? How many local scopes are there? 6. What happens to variables in a local scope when the function call returns? 7. What is a return value? Can a return value be part of an expression? 8.  If a function does not have a return statement, what is the return value of the call to that statement? 9. How can you force a variable in a function to refer to the global variable? 10. What is the data type of None? 11. What does the import areallyourpetsnamederic  statement do? 12. If you had a function named bacon()  in a module named spam, how would you call it after importing spam? 13. How can you prevent a program from crashing when it gets an error? 14. What goes in the try  clause? What goes in the except  clause? 15. Write the following program in a file named notrandomdice.py  and run it. Why does each function call return the same number?import randomrandom_number = random.randint(1, 6)def get_random_dice_roll():
 
 # Returns a random integer from 1 to 6 return random_numberprint(get_random_dice_roll())print(get_random_dice_roll())print(get_random_dice_roll())print(get_random_dice_roll())Practice ProgramsFor practice, write programs to do the following tasks.The Collatz SequenceWrite a function named collatz()  that has one parameter named number. If number  is even, then collatz()  should print number // 2  and return this value. If number  is odd, then collatz()  should print and return 3 * number + 1.Then, write a program that lets the user enter an integer and that keeps calling collatz()  on that number until the function returns the value 1. (Amazingly enough, this sequence actually works for any integer; sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)Remember to convert the return value from input()  to an integer with the int()  function; otherwise, it will be a string value. To make the output more compact, the print()  calls that print the numbers should have a sep=' 'named parameter to print all values on one line.The output of this program could look something like this:Enter number:33 10 5 16 8 4 2 1Hint: An integer number  is even if number % 2 == 0, and it’s odd if number % 2 == 1.Input ValidationAdd try  and except  statements to the previous project to detect whether the user entered a non-integer string. Normally, the int()  function will raise a ValueError  error if it is passed a non-integer string, as in int('puppy'). In the except  clause, print a message to the user saying they must enter an integer.
"""
"""
 1. functions can make repetitive tasks easier, they can replace the copy paste method.
 2. the function is executed only when it is called
 3. def variable(parameter): #<- colon
 4. a function is code written into memory, does nothing. a function call is the statement that makes the function run
 5. global scope, one. local scope one per function definition
 6. idk, they get executed, and immediately vanish into the void (to be reused again by another function call)
 7. the output of the function, if theres no return value. youre literally giving python None, second question, yes (I do not know how)
 8.  see no. 7
 9. use global
 10. NoneType
 11. it imports areallyourpetsnamederic, and you can use it on your own py script
 12. spam.bacon() #uhhm?
 13. try/ except
 14. part of the code that, when causes an error, jumps to the except statement.
 except YourErrorHere: has a block of code that runs whenever a specific error appears when try is run
 15. the function is defined at the top, the function calls at the bottom run the defined function, and since random.randint() doesnt give the same result everytime, the printout is random
 
"""
# message to future me
    #"this is me from Feb. 14 2026, im 14, single, tired, and broke")
import sys
def collatz(number):
    if number % 2 == 0:
        print(number // 2, end = "  ")
        return number // 2
    else:
        print(3 * number + 1, end = "  ")
        return 3 * number + 1
        

# 3 * number + 1
try:
    num = int(input("Type your number: "))
except ValueError:
    print("Type a positive integer")
    sys.exit()
if num < 0:
    print("type a positive integer")
while num > 1:
    num = collatz(num)
print()
    
    
    