"Regex Version of the strip() Method Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than the string to strip, then the function should remove whitespace characters from the beginning and end of the string. Otherwise, the function should remove the characters specified in the second argument to the function."
#idea, what if i use the caret symbol, and combine it with sub()
import re
def re_strip(text:str, character:str = None) -> str: #returnsmodified string 
    if not isinstance(text, str):
        raise ValueError(f"expected str, got: {type(text).__name__}")
    if character is not None and not isinstance(character,str):
        raise ValueError(f"expected str/None, got: {type(character).__name__}")
    if character is None or character  == "":
        pattern = r"^\s+|\s+$"
    else:
        esc = re.escape(character)
        #initially didnt know this
        pattern = f"^{esc}+|{esc}+$"
     
    return re.sub(pattern, "", text)
        
        
    
   
        
#alert: using google on how to use re.sub()
#alert: searching google on how to make arguments optional
    
    #re.sub continues searching after match, the pipe symbol only picking one pattern or the other is irrelevant
        
        
        


if __name__ == "__main__":
    repl = input("What to strip? (type nothing for whitespace): ")
    space_count = len(re_strip(input("Type anything: "),repl))
    print(f"Number of Characters: {space_count}, Character Stripped: \"{repl}\"")
    
    

    #bug found: if end of string has precisely one whitespace, its part of the modified string #example above should be 8, result is 9
    #update; fixed. problem was regex pattern object without re.VERBOSE interprets whitespace in string as part of pattern example: "a b" is identical to "a\sb"

                                                                              #bug to fix: make second argument optional
#update: didnt find any bugs except the fact that I have no idea how to make a parameter optional
                                                                              
                                                                              
                                                                            
    