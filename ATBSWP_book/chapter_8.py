questions = r"""
Practice Questions

1. What are escape characters? 2. What do the \n and \t escape characters represent? 3. How can you put a \ backslash character in a string?

4. The string value Howl's Moving Castle is a valid string. Why isn’t it a prob-lem that the single quote character in the word Howls isn’t escaped?
#i removed the double quotew since it keeps messing with the multiline string.

5. If you don’t want to put \n in your string, how can you write a string with newlines in it?

6. What do the following expressions evaluate to?

• 'Hello, world!'[1] • 'Hello, world!'[0:5] • 'Hello, world!'[:5] • 'Hello, world!'[3:]

180 Chapter 8

7.
What do the following expressions evaluate to?

• 'Hello'.upper() • 'Hello'.upper().isupper() • 'Hello'.upper().lower()

8. What do the following expressions evaluate to?

• 'Remember, remember, the fifth of November.'.split() • '-'.join('There can be only one.'.split())

9. What string methods can you use to right-justify, left-justify, and center a string?

10. How can you trim whitespace characters from the beginning or end of a string?"""

answers = """

1. escape characters solve the problem of coding strings, without it, some characters would be impossible to type inside a string.(e.g. double quotes in a string literal defined with double quotes)

2.\n is newline, \t is tab
3. type '\' and a following character for the sequence you desire to make.

4. the quotes that define it uses double quotes, therefore the single quote inside the string doesnt break 
5. use a multiline string
6. 'Hello, world!'[1] • 'Hello, world!'[0:5] • 'Hello, world!'[:5] • 'Hello, world!'[3:]
-'e'
-'Hello' (up to, but not including)
-same thing as no. 2
-'lo, world!' 

7. 'Hello'.upper() = 'HELLO' 'Hello'.upper().isupper() = True 'Hello'.upper().lower() = 'hello'

8. 'Remember, remember, the fifth of November.'.split() -> outputs a list that splits the sentence into multiple strings, separated by either spaces or newlines (or something else that ion know about)
9. '-'.join('There can be only one.'.split())

first, the join function must have a list as its argument. it will return a string where anything in it will be repeared in each iteration. sooo 'There-can-only-be-one.'

10. .lstrip() removes beginning whitespace, .rstrip() removes whitespace at the end of the string, strip() removes both.

quick mention, you can add arguments to these functions to remove any sequence of characters in a string


EXERCISE TIMEEEE.





"""

"""Practice Program: Table Printer
For practice, write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column rightjustified. Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:
tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]
Your printTable() function would print the following:
apples Alice dogs oranges Bob cats cherries Carol moose
banana David goose Hint: Your code will first have to find the longest string in each of the
inner lists so that the whole column can be wide enough to fit all the strings. You can store the maximum width of each column as a list of integers. The printTable() function can begin with colWidths = [0] * len(tableData), which will create a list containing the same number of 0 values as the number of inner lists in tableData. That way, colWidths[0] can store the width of the longest string in tableData[0], colWidths[1] can store the width of the longest string in tableData[1], and so on. You can then find the largest value in the colWidths list to find out what integer width to pass to the rjust() string method."""

def printTable(table:list) -> None:
    some_list = []
    for i in table:
        for item in i:
            some_list.append(item)
    print(some_list)
            
            
        
        
        
            

if __name__ == "__main__":
    tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]
    printTable(tableData)
