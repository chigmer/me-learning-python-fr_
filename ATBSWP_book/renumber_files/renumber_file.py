import re
from pathlib import Path

"""
Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and a spam003.txt but no spam002 .txt)
As an added challenge, write another program that can insert gaps into
numbered files (and bump up the numbers in the filenames after the gap) so that a new file can be inserted."""
def find_files(path=Path.cwd())->list:
    #dev errors
    if not isinstance(path,Path):
        raise ValueError("expected Path obj")
    elif not path.is_dir():
        raise ValueError("expected directory.")  
    pattern = re.compile(r"""
    ([a-zA-Z]+)
    (\d+)\.    
    ([a-zA-Z]+)
    
    """,re.VERBOSE) 
    file_info = []
         
    for filepath in path.iterdir():
        match = re.fullmatch(pattern,filepath.name)
        if match:
            file_info.append((match.group(1),int(match.group(2)),match.group(3),Path(filepath.name)))
    return file_info
        
        
 
#newer update
#i got the list of tuples working .   
#breakdown before i go, it returns (prefix,number,extension,Path obj to file)   
   
   
    #older update
    #todo: organize all files with a common prefix and filename extension
    #then be able to identify which stuff is missing using the function below.
    
    
def find_ordering(files:tuple):
    #everything should be in a dictionary.
    #no need to do any dev checks or stuff. this is just for the user, if it breaks, its not my fault.
    file_collection = {}
    for file in files:
        key = (file[0], file[2])
        file_collection.setdefault(key, []).append(file[1])
    return file_collection
    
def find_gaps(collection:dict):
    for entry in collection:
        imperfect_set = set(collection[entry]) #list obj turned to a set               
        perfect_set = set(range(1,max(imperfect_set) + 1))
        #unfinished
        
        return perfect_set - imperfect_set
        
        
            #the values within entry
    
print(find_ordering(find_files()))    
print("yo")

#missing files:
missing = find_gaps(find_ordering(find_files()))
    
      
    
    
    
    