from pathlib import Path


h = Path.home()
dirs = """spam/bacon
spam/eggs2
spam/bacon2
spam/eggs/sausage""".split("\n")
#easier to make a list this way.
for path in dirs:
    (h/path).mkdir(exist_ok = True, parents = True)
    if (h/path).exists():
        print(f"Created {path}")
    else:
        print(f"failed to make {path}")
print("\n\n")
txt = []
for i,v in enumerate(dirs):
     txt.append(f"{v}/file_{i}")

print(f"for dev (me for real.):\n{txt}\n\n")
     
     

     
     
for f in txt:
    with open(h / f, 'w', encoding='utf-8') as file:
        file.write('Hello')
    if Path(h/f).exists():
        print(f"file \"{Path(f).name}\" created")
    else:
        print(f"Error! file \"{Path(f).name}\" not created")
 
#current output:
"""Created spam/bacon                                         Created spam/eggs2                                         Created spam/bacon2                                        Created spam/eggs/sausage                                  


for dev (me for real.):
['spam/bacon/file_0', 'spam/eggs2/file_1', 'spam/bacon2/file_2', 'spam/eggs/sausage/file_3']


file "file_0" created
file "file_1" created
file "file_2" created
file "file_3" created

[Terminal session finished]
"""
#Ive noticed the unusual amount of f-strings ive used