import re
import argparse
from pathlib import Path
import sys

#Project 3: Extract Contact Information from Large Documents
#I excluded the pyperclip lines. nice to have though.
#Create email regex.

def parse_args() -> tuple:
    parser = argparse.ArgumentParser(
        description="A tool to extract contact information from documents or a piece of text, supports only email addresses and phone numbers"
    )
    parser.add_argument("source",type=str,help="your text or filepath.")
    parser.add_argument("-f","--is_file",action="store_true",help="turn text to a filepath")
    args = parser.parse_args()
    text = args.source
    is_file = args.is_file
    return text,is_file
    
    
    

    
    

def main():
    phone_re = re.compile(r'''
\b
(?:\+?\d{1,3}[\s.-]?)?              # optional country code
(?:\(?\d{3}\)?[\s.-]?)              # area code
\d{3}                              # first 3 digits
[\s.-]?                            # separator
\d{4}                              # last 4 digits
(?:\s*(?:ext|x|ext\.)\s*\d{2,5})?  # extension
\b
''', re.VERBOSE | re.IGNORECASE)
    email_re = re.compile(r'''
\b
(?:[a-zA-Z0-9._%+-]+)      # local part
@
(?:[a-zA-Z0-9-]+\.)+      # domain (handles subdomains)
[a-zA-Z]{2,}              # TLD (no arbitrary 4 limit)
\b
''', re.VERBOSE)
    content,is_file = parse_args()
    PLAINTEXT_EXTENSIONS = {
    "txt", "csv", "log", "md", "markdown", "rst", "json", "yaml", "yml", 
    "toml", "ini", "conf", "cfg", "xml", "html", "htm", "css", "scss", 
    "js", "ts", "py", "pyi", "c", "cpp", "h", "hpp", "cs", "java", "go", 
    "rs", "rb", "php", "pl", "sh", "bat", "ps1", "sql", "r", "swift", 
    "env", "gitignore", "dockerignore", "editorconfig", "makefile"
}

    if not is_file:
        text = content
        #realized way too late that variable text is already used
    else:
        file = Path(content)           
        if file.exists():  
            if file.is_dir():
                print("filepath is a directory.")
                sys.exit()
            elif file.suffix[1:] not in PLAINTEXT_EXTENSIONS:
                print("file is not readable.")
                sys.exit()
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
        else:
            print("file doesnt exist.")
            sys.exit()
            
            
        
    matches = []

# Extract phone numbers
    for m in phone_re.finditer(text):
        matches.append(m.group())

# Extract emails
    for m in email_re.finditer(text):
        matches.append(m.group())

# Output
    if matches:
        matches = list(set(matches))
        print("Matches found:")
        for i in matches:
            print(i)
    else:
        print("no matches found")
    #notifies the user whenever there are no matches
if __name__ == "__main__":
    main()