"""Say your boss emails you thousands of files with American-style dates (MM-DD-YYYY) in their names and needs them renamed to Europeanstyle dates (DD-MM-YYYY). This boring task could take all day to do by hand! Instead, write a program that does the following:
Searches all filenames in the current working directory and all subdirectories for American-style dates. Use the os.walk() function to go through the subfolders.
Uses regular expressions to identify filenames with the MM-DD-YYYY pattern in them—for example, spam12-31-1900.txt. Assume the months and days always use two digits, and that files with non-date matches don’t exist. (You won’t find files named something like 99-99-9999.txt.)
When a filename is found, renames the file with the month and day swapped to make it European-style. Use the shutil.move() function to do the renaming."""
from pathlib import Path
from gen_dates import generate_dates
#module i made myzelf
#makes a random valid date with formatting MM-DD-YYYY, from Y 2015-2026

def find_files(path:Path=Path.cwd(),ext: str='txt') -> list:
    if not isinstance(path,Path):
        raise ValueError("expected Path on arg 1")
    elif not isinstance(ext,str):
        raise ValueError("expected str on arg 2")
    elif not path.exists():
        return
        
    files = list(path.rglob(f'*.{ext}'))   
    return files
def make_test_txt() -> list:
    dates = generate_dates(50)
    files = []
    for date in dates:
        filename = f"spam_{date}.txt"
        with open(filename, "w"):
            pass
        files.append(filename)
    return files
    
if __name__ == "__main__":
    import re
    import shutil
    pattern = re.compile(r'''
    ([\w]+)# group 1  
    (\d{2}) # group 2
    -
    (\d{2}) # group 3
    -
    (\d{4})# group 4
    ''',re.VERBOSE)#using verbose for clarity
    
    
    files_created = make_test_txt()  
    #window to type my code in and test stuff, after this, boom files gone, no bloat after each test
    new_names = set()
    for file in files_created:
        file = Path(file)
        if file.exists(): #just in case
            print(f"found {file.name}")
            match = re.search(pattern,file.name)
            if match:
                new_name = f"{match.group(1)}{match.group(3)}-{match.group(2)}-{match.group(4)}.txt"
                new_names.add(new_name)
                #a set uses add()
                shutil.move(file,file.parent/new_name)
                print(f"renamed to: {new_name}\n")
                
     
    
    i = 1
    for f in Path.cwd().rglob("*.txt"):
        if f.name in new_names:
            print(f"{i}. file {f.name} is a test file. \ndeleting...")
            f.unlink()
            i += 1
        
        
        
        
    
    
    
    