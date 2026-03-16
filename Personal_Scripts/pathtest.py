import os
from pathlib import Path

print(os.path.abspath(__file__))
print(os.getcwd())
print("\n\n\n")
p = Path("something")
print(str(p) + "\n\n\n")
print(Path.cwd() / Path("bacon", "eggs", "sushi"))