#counts how many python scripts i have.
#lowk neat
from pathlib import Path
file_count = 0


for file in Path.cwd().rglob("*.py"):
    print(f"found: {file.name}")
    file_count += 1
if file_count:
    print(f"\ntotal is {file_count} files")
else:
    print("No .py files found.")


    
    