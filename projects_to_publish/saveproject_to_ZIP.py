from zipfile import ZipFile
from zipfile import ZIP_DEFLATED
import shelve
from pathlib import Path
from datetime import datetime
import argparse
import sys
#saveproject_to_ZIP_CLI
#Drawing board
#make a function, moduleable, 
#create a dedicated directory in saving these zipfiles

#increment zip files, easiest way? iterate every time this module is called, saved using shelve,keeps the "moduleable" in check

  


def index() -> int:
    db = Path("myZipFiles/.indexdata")
    db.mkdir(parents=True, exist_ok=True)
    with shelve.open(str(db / "data")) as d:
        i = d.get("i", 0)
        #basically {"i": some number}
        i += 1
        d["i"] = i
        return i

def backup_to_zip(sources: list[Path],verbose:bool) -> int:
    #returns current zip file number from index()
    EXCLUDED_DIRS = {
    "myZipFiles",
    ".indexdata",
    "__pycache__",
    ".venv",    
    ".mypy_cache",
    ".pytest_cache",
    ".git"
}
    now = datetime.now().strftime("%Y_%m_%d-%H%M")
    p = Path("myZipFiles")
    p.mkdir(exist_ok=True)
    i = index()
    
    
    #write the ZipFile
    with ZipFile(f"{p}/zip_backup_{i}_{now}.zip", "w") as zf:
        for source in sources:
            if not source.exists():
                if verbose:
                    print(f"path {source} is nonexistent.. skipping")
                continue
            if source.is_file():
                zf.write(source,arcname=source.name, compress_type=ZIP_DEFLATED,compresslevel=9)
                if verbose:
                    print(f"zipped {source.name}")
            else:
                for f in source.rglob("*"):
                    if any(part in EXCLUDED_DIRS for part in f.parts):
                        continue
                    zf.write(f,arcname = f.relative_to(source),compress_type=ZIP_DEFLATED,compresslevel=9)
                    if verbose:
                        print(f"zipped {f.name}")
    return i
          
def parse_args() -> tuple:
    parser = argparse.ArgumentParser(
        description="Creates versioned ZIP backups of files and folders."
    )  
    parser.add_argument("source",type=Path,nargs='+',help="file or directory to zip, use quotes if file contains whitespace") #if argument is .
    #argument is everything in the current working
    #directory
    parser.add_argument("-v","--verbose",action="store_true",help="show script processes")
    args = parser.parse_args()
    source = args.source
    verbose = args.verbose
    return source,verbose
    
          
    
    
             
def main() -> None:   
    source,verbose = parse_args()
    try:
        i = backup_to_zip(source,verbose)
    except Exception as e:
        print(f"bug found, debug immediately.\n{e}")
        sys.exit()
    print(f"Backup version {i} completed.")
 
            
if __name__ == "__main__":
    main()
    
    
        
       
    
    
        
    
            
                
       
    
    
        
    
        
        
    
           
        
                    
                   
                    
                    
            
            
            
    
    
   
    
    

