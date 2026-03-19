"""Practice Questions 
write an assert statement that triggers an assertion error if the variables spam is less than 10
Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different. (That is, 'hello' and 'hello' are considered the same, as are 'goodbye' and 'GOODbye'.)
Write an assert statement that always triggers an AssertionError.
What two lines must your program have to be able to call logging.debug()? 

What two lines must your program have to make logging.debug() send a logging message to a file named programLog.txt?()

What are the five logging levels?
i'll answer this anyway, wasted knowledge.

its debug
info
warning
error
critical

What line of code can you add to disable all logging messages in your program?

Why is using logging messages better  than using print() to display the same message?

What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?

After you click Continue, when will the debugger stop? What is a b reakpoint? How do you set a breakpoint on a line of code in Mu? """
"""
spam = 9
assert spam >= 10, "int must be larger than 10"
"""

"""
bacon = "Goodbye"
eggs = "GOODBYE"

bacon = bacon.lower().strip()
eggs = eggs.lower().strip()

assert bacon != eggs, "variable eggs and bacon are equal"
"""

"""
assert None, "cant escape this one!!"
"""

""" safe to say that the following questions are irrelevant. print()is sufficient for now(emphasis on FOR NOW. I have a very productive learning schedule. this is beneath me.. For NOW)"""

