from zipfile import ZipFile
from zipfile import ZIP_DEFLATED
import shelve
from pathlib import Path
from datetime import datetime

#this time. its a "plug and play" script where you just run it, type in the directories or files you want to save to a zip file


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
            
            
#
print("made by Chigmer\n\n\nType the directories/files you want to archive to your zip file\ntype nothing to finish.")
user_paths = []
while True:
    user_input = input(">")
    if not user_input:
        break
    user_path = Path(user_input)
    if not user_path.exists():
        match = list(Path.cwd().rglob(user_path.name))
        if match:
            print(f"dir/file {user_input} is missing parent dir/s\n did you mean:")   
            for m in match:
                print(f"{m.relative_to(Path.cwd())}")         
        else:
            print(f"dir/file {user_input} doesnt seem to exist. did you type it correctly?")
        continue
        
    user_paths.append(user_path)
print("\n\n")
if user_paths:
    backup_to_zip(user_paths)
else:
    print("no Paths provided, exiting")
#sample output
"""
made by Chigmer                                            Type the directories/files you want to archive to your zip file
type nothing to finish.
>IOprojects/dir_maker_v2.py
dir/file IOprojects/dir_maker_v2.py doesnt seem to exist. did you type it correctly?
>IOprojects
>



zipped temp_textmaker.py
zipped TEXTTEST.txt
zipped dir_maker_v2_.py
zipped IOprojects
zipped test_dir
zipped dir_v2
zipped hi
zipped hi2

"""
#a directory named "myZipFiles" containing a .zip file was born
    
    
    
    
    
    
    
    
    

  