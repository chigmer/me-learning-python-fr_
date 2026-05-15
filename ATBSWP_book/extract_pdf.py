from pdfminer.high_level import extract_text
from pathlib import Path

for i in Path.cwd().iterdir():
    if i.suffix.lower() == ".pdf":
        text = extract_text(str(i))
        print(text)
#this is pretty simple i guess
#loops + smarter file finding + inserting output to a txt file would make this an actual script