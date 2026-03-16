from pathlib import Path
with open("TEXTTEST.txt", "w") as t:
    t.write("ahh hello there. \n\nThese nested directories were made from a program using os.makedirs()")
    
   
print(Path.cwd())
#it worked
    