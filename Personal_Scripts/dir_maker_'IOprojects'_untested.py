from pathlib import Path


#help(os.makedirs)
def create_dir(text: Path):
    if text.exists():
        print("Directory exists.")
        return
    try:
        text.mkdir(exist_ok=True)
        print("Done")
    except FileNotFoundError:
        print("Parent Directory(s) does not exist")
    
    except PermissionError:
        print("no permission")
    except Exception as e:
        print(f"error making directory: {e}")

p = Path.cwd() / Path('IOprojects')
if not p.exists():
    create_dir(p) #currently have no idea what parents=True does
#exist_ok=True prevents FileExistsError if file/directory already exists

#calling mkdir() like on text.mkdir() only works if the object(or text) is a Path object.
    



