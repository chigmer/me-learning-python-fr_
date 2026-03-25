from zipfile import ZipFile
from zipfile import ZIP_DEFLATED
import shelve
from pathlib import Path
from datetime import datetime


r"""Say you’re working on a project whose files you keep in a folder named C:\ Users\Al\AlsPythonBook. You’re worried about losing your work, so you’d like to create ZIP file “snapshots” of the entire folder. You’d also like to keep different versions of these snapshots, so you want the ZIP file’s filename to increment each time a new version is made; for example, AlsPythonBook_1 .zip, AlsPythonBook_2.zip, AlsPythonBook_3.zip, and so on. You could do this by hand, but that would be rather annoying, and you might accidentally misnumber the ZIP files’ names. It would be much simpler to run a program that does this boring task for you. For this project, open a new file editor window and save it as backup_to
_zip.py."""

#Drawing board
#make a function, moduleable, 
#create a dedicated directory in saving these zipfiles

#increment zip files, easiest way? iterate every time this module is called, saved using shelve,keeps the "moduleable" in check

  


def index() -> int:
    Path("indexdata").mkdir(parents=True, exist_ok=True)
    with shelve.open(Path.cwd()/"indexdata/data") as d:
        i = d.get("i", 0)
        #basically {"i": some number}
        i += 1
        d["i"] = i
        return i

def backup_to_zip(sources: list[Path]):
    EXCLUDED_DIRS = {
    "myZipFiles",
    "indexdata",
    "__pycache__",
    ".venv",    
    ".mypy_cache",
    ".pytest_cache",
}
    now = datetime.now().strftime("%Y_%m_%d-%H%M")
    i = index()
    p = Path("myZipFiles")
    p.mkdir(exist_ok=True)
    
    
    #write the ZipFile
    with ZipFile(f"{p}/zip_backup_{i}_{now}.zip", "w") as zf:
        for source in sources:
            if not source.exists():
                print(f"path {source} is nonexistent.. skipping")
                continue
            if source.is_file():
                zf.write(source,arcname=source.name, compress_type=ZIP_DEFLATED,compresslevel=9)
                print(f"zipped {source.name}")
            else:
                for f in source.rglob("*"):
                    if any(part in EXCLUDED_DIRS for part in f.parts):
                        continue
                    zf.write(f,arcname = f.relative_to(source),compress_type=ZIP_DEFLATED,compresslevel=9)
                    print(f"zipped {f.name}")
if __name__ == "__main__":
    import random
    from pathlib import Path
    import sys
    files = []
    for i in range(1,11):
        with open(f"shitty_file_{i}.txt", "w+") as f:
            for _ in range(10000):
                f.write(str(random.randint(0,9)))
        files.append(Path(f"shitty_file_{i}.txt"))
    try:
        backup_to_zip(files)
    except Exception as e:
        print(f"Thou must debug.\n{e}")
        sys.exit()
    print("Done")
        
       
    
    
        
    
            
                
       
    
    
        
    #zf.getinfo('file1.txt')
    #{info.file_size}
    #{info.compress_size}

        
        
    
           
        
                    
                   
                    
                    
            
            
            
    
    
   
    
    

