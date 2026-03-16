from pathlib import Path
import os
p = Path.cwd() / Path("STUFFmain/stuff2/stuff3/stuff4/text.txt")
print(p)
print(p.parts) #tuple
def create_dir(text: object):
    
    t = Path(text)
    try:
        os.makedirs(t)
    except OSError as e:
        print(f"error: {e}")
create_dir("Stuff/morestuff/stuff2/stuff3")
create_dir("Stuff/morestuff2")
    