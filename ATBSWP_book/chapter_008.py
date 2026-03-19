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

#when i look back at this. ill be embarassingly confused. ill fix that by adding some comments here and there
def printTable(table: list) -> None:
    # table is expected to be a list of lists.
    # IMPORTANT: This structure is COLUMN-oriented.
    # Meaning:
    # table[0] = first column
    # table[1] = second column
    # table[col][row] = element at (column, row)
    #
    # This is not the usual row-major structure people imagine.
    # So mentally rotate it 90 degrees.

    # Create a list to store the maximum width for each column.
    # len(table) = number of columns.
    # So colWidths[i] will store the width of column i.
    colWidths = [0] * len(table)

    # Iterate through each column index.
    for col in range(len(table)):
        # table[col] is the entire column (a list of strings).
        # We now scan that column to find the longest string in it.

        for string in table[col]:
            # Compare the length of the current string
            # against the largest length seen so far in this column.
            if len(string) > colWidths[col]:
                # If this string is longer, update the stored max width.
                colWidths[col] = len(string)

    # At this point:
    # colWidths looks something like [8, 5, 5]
    # Meaning:
    # Column 0 needs width 8
    # Column 1 needs width 5
    # Column 2 needs width 5
    #
    # We now know how wide each column must be
    # so that right-justification aligns properly.

    # Now we print row by row.
    # IMPORTANT: Since the structure is column-oriented,
    # the number of rows equals the length of any one column.
    # We assume all columns have equal length.
    for row in range(len(table[0])):
        # Print a newline before starting the row.
        # (This creates a blank line before the first row too.)
        print()

        # Now iterate across columns for this specific row.
        for column in range(len(table)):
            # table[column][row] accesses:
            # - specific column
            # - specific row inside that column
            #
            # rjust(colWidths[column]) pads the string
            # on the left so its total width equals the column's max width.
            #
            # end=" " prevents newline and adds space after each cell.
            print(table[column][row].rjust(colWidths[column]), end=" ")


            
            
            
            
        
    
    
                
        
    
  
    
    
        
    
     
        
        
       
        
    
        
            
            
        
        
        
            

if __name__ == "__main__":
    tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]
    printTable(tableData)
    #no comments needed. a 10 year old knows what this is.
