"""
Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this:
    
    
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.
"""

import re


def find_lib(text: str, subs: list) -> str:
    pattern = re.findall(r"ADJECTIVE|NOUN|VERB", text)
    for i,ps in enumerate(pattern):
        text = re.sub(ps, subs[i], text, count=1)
    
    
            
    return text 
    
def iterate(text:str) -> list:
    return re.findall(r"ADJECTIVE|NOUN|VERB",text)
  
    
        
        
            
            
if __name__ == "__main__":
    
    #me before doing this:
    #introduction, collect txt files (visible progress)
    #give an indicator for the amount of "lib"(part of speech) found in example.txt
    #boom, the user is now answering shit.
    #print results ✓
    #ask for filename (ehh scrap that)
    #save it to cwd.
    #done
    #ez plan
    from pathlib import Path
    import sys
    
    output_dir = Path("madlibs_outputs")
    output_dir.mkdir(exist_ok=True)
    
    print("Welcome\nCollecting txt files..\n")
    
    txt_files = list(Path.cwd().rglob("*.txt"))
    if not txt_files:
        print("No txt files found!\nmaybe check the directory this script is running in.")
        sys.exit()
    else:
        for f in txt_files:
            print(f"Found: {f.name}\n")
    
            
    
    
    for f in txt_files:
        string = f.read_text()
        print(f"number of \"libs\" found: {len(iterate(string))} ")
        user = []
        print(f"File: {f.name}\nType these in order->\n")   
        for psp in iterate(string):
            user.append(input(f"{psp}: "))                              
        madlib_result = find_lib(string,user)
        print(madlib_result)
        
        with open(output_dir / f"madlibs_{f.name}", "w") as m:
            #the line "madlibs_{f.name}" should always end in .txt, so being lazy saves me from duplication
            m.write(f"Total 'libs': {len(iterate(string))}\n")
            m.write(madlib_result)
        

    