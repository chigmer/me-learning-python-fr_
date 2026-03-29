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
    files = []
    for filepath in path.rglob("*.*"):
        files.append(filepath.name)
        
    pattern = re.compile(r"""
    ([\w-]+)
    (\d+)
    \.
    ([a-zA-Z]+)
    
    """,re.VERBOSE)
    #todo: organize all files with a common prefix and filename extension
    #then be able to identify which stuff is missing using the function below.
    #bye
def find_ordering(files):
    pass
    