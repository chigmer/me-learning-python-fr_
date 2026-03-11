#commence txt file generator

#Ask the user for the filename. (use re.fullmatch())✓
#Ask for the content.✓
#Write to a .txt file using a with open() block so it’s safe and auto-closed.✓
import re
print("Text File Generator\nmade on Mar. 11, 2026")

def validate_word(text:str) -> bool:
    if not isinstance(text, str):
        raise ValueError("invalid type")
    match = re.fullmatch(r"^\w+$", text)
    #everything must be composed of letters, numbers, or underscores 
    if match:
        return True
    else:
        return False
        
print("Filename: \n")
#validation section below        
while True:
    filename = input(">")
    if validate_word(filename):
        break
    else:
        print("input must consist of letters, numbers and/or underscores")
        
        
        
print("Content: \n")
content = input(">")        

try:
    with open(f"{filename}.txt", "w") as f:
        #overwrites the text, exactly what I want.
        #TODO: make the script realize if file already exists.
        f.write(content)
except Exception as err:
    print(f"an error occurred: \"{err}\" ")
    #this is for me when any bugs slip.
    #i do NOT know what error message will trigger.
    
    