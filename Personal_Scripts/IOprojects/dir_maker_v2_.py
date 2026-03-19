from pathlib import Path
import re
def validate(string:str) -> bool:
    return bool(re.fullmatch(r"\w+(?:/\w+)*/?", string)) 
    #letters, numbers, underscores  and the forward slash for Path()
    
       
def create_dir(text: Path):
    if text.exists():
        print("Directory exists.")
        return
    try:
        text.mkdir(exist_ok=True, parents=True)
        print("Done")
    except FileNotFoundError:
        print("Parent Directory(s) does not exist")
    
    except PermissionError:
        print("no permission")
    except Exception as e:
        print(f"error making directory: {e}")
print("Type the directory you want to make within \"IOprojects\"")




while True:
    user = input(">")
    if not validate(user):
        print(f"Incorrect formatting. \nYou Typed: {user}\n\nvalid text must be composed of letters, numbers, underscores, and a forward slash in between words")
        #Im not bothering to write another exhausting except chain.
        continue
    break
    
    


p = Path("/storage/shared/00py_shi/me-learning-python-fr_") / 'ATBSWP_book' / user
try:
    if not p.exists():
        create_dir(p) #parents = True creates intermediate directories if it doesnt exist.
except Exception as e:
    print(e)
#exist_ok=True prevents FileExistsError if file/directory already exists

#calling mkdir() like on text.mkdir() only works if the object(or text) is a Path object.
#some redundancy present, i only did this in one sitting.
    



