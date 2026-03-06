import re
#self made, didnt get this from gogle

rawtxt = """The | character is called a pipe, and it’s used as the alternation operator in regular expressions. You can use it anywhere you want to match one of multiple expressions. For example, the regular expression r'Cat|Dog' will match either 'Cat' or 'Dog'. You can also use the pipe to match one of several patterns as part of your
regex. For example, say you wanted to match any of the strings 'Caterpillar', 'Catastrophe', 'Catch', or 'Category'. Since all of these strings start with Cat, it would be nice if you could specify that prefix only once. You can do this by using the pipe within parentheses to separate the possible suffixes. Enter the following into the interactive shell:"""

pattern = re.compile(r" [a-zA-Z]{7} ")
matches = pattern.findall(rawtxt)

if matches:
    print("matches found: ")
    for i,word in enumerate(matches):
        print(matches[i].strip())
        
    
        
else:
    print("nada, nothing")
    
#todo for future me. explain every line in detail. and have an input option for letter count. turn this to a function.