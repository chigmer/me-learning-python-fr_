#commence txt file generator

#Ask the user for the filename. (use re.fullmatch())✓
#Ask for the content.✓
#Write to a .txt file using a with open() block so it’s safe and auto-closed.✓
import re
print("Text File Generator\nmade on Mar. 11, 2026")

import os


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
        
        
        
print("\n\nContent: \n")
content = input(">")        

script_dir = os.path.dirname(os.path.abspath(__file__))

# optionally, a subfolder inside the script folder
subfolder = "text_maker"
target_dir = os.path.join(script_dir, subfolder)
os.makedirs(target_dir, exist_ok=True)  # creates it if it doesn't exist

# write the file
with open(os.path.join(target_dir, f"{filename}.txt"), "w") as f:
    f.write(content)

print(f"\nDone! check {filename}.txt in {subfolder}")

#copy pasted this part, will infact learn what this piece of code does
#other than the part where the directory stuff was needed, everything was written by me
#TODO: code this script to have the ability to place a file on whichever directory i want
    
    