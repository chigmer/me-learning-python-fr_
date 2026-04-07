import sys
import re
from pathlib import Path
args = sys.argv
if len(args) != 2:
    print("hey. you did it wrong")
    print(f"Usage: python {args[0]} <filename> (add quotes if file has whitespace)")
    sys.exit()
file = Path(args[1])

if not file.suffix and not file.name.startswith("."):
    print("file must have an extension or be a dotfile")
    sys.exit()
if file.exists() and file.is_file():
    print(f"file {file} exists")
else:
    print(f"file {file} does not exist or is not a file.")
    sys.exit()
TEXT_EXTENSIONS = {
    ".txt", ".py", ".md", ".csv", ".json", ".xml", ".html", ".css",
    ".js", ".ts", ".java", ".c", ".cpp", ".h", ".hpp", ".cs", ".go",
    ".rs", ".php", ".rb", ".swift", ".kt", ".sh", ".bat", ".ps1",
    ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf", ".log", ".sql",
    ".env", ".gitignore", ".dockerignore", ".editorconfig",
    ".gitattributes", ".tex", ".rtf"
}
if file.suffix.lower() in TEXT_EXTENSIONS:
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()
        print("successfully read file\n\n")
        print(text)
        print(f"amount of words:\n{len(text.split())}")
        print(f"amount of characters: {len(text)}")
        print(f"amount of lines: {len(text.splitlines())}")       
else:
    print("given file is not a readable plain text file.")

    