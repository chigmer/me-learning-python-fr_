"""Regex Search Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression, then prints the results to the screen."""
from pathlib import Path
import sys
import re

txt_files = list(Path.cwd().rglob("*.txt"))

if not txt_files:
    print("No txt files found!\nmaybe check the directory this script is running in.")
    sys.exit()
else:
    for f in txt_files:
        print(f"Found: {f.name}\n")
print("Supply a regex string, and i shall look for matches")

user = input(">")  
try:
    user_pattern = re.compile(rf"{user}")
except re.error as e:
    print(f"invalid regex expression!\n{e}")
    sys.exit()
for f in txt_files:
    text = f.read_text()      
    match = re.findall(user_pattern,text)
    if match:
        print(f"Matches found: {len(match)}")
        for i in match:
            print(i)
    else:
        print("No matches found")
        
    
    
        
    
        
        

    
            