import os
from pathlib import Path
"""Write a program that walks through a folder tree and searches for exceptionally large files or 
folders—say, ones that have a file size of more than 100MB. 
(Remember that, to get a file’s size, you can use os.path.getsize() from the os module.) 
Print these files with their absolute path to the screen."""

def get_size(path: Path) -> int|None:
    #defensive programming, made sure that the function does not crash if Path is a directory
    #single files only, i think that searching entire directories and calculating its filesize will take
    #longer and ruin my sleep
    #os.path.getsize()
    if not isinstance(path, Path):
        raise ValueError(f"expected Path, got {type(path).__name__}")
    if path.exists() and path.is_file():
        return os.path.getsize(path)
    else:
        return None #for clarity 
if __name__ == '__main__':
    print("searching home directory...")
bigfiles = [] 
for i in Path.home().rglob("*"):
    if i.is_file():
        filesize = get_size(i) / 1048576  # type: ignore #1,048,576
        if filesize >= 100:
            bigfiles.append((filesize,i))

print(f"big files found: {len(bigfiles)}\n\n")
for items in bigfiles:
    print(f"file {items[1].name}:\nSize:{items[0]:.5f} mb\nPath: {items[1]}\n\n")



    

