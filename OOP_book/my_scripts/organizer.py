from pathlib import Path
#File Organizer
"""Downloads

├── Images
├── PDFs
├── Videos
├── Code
├── Archives
└── Audio

Scan a directory for files
Categorize by extension (images, documents, code, archives, etc.)
Move files into category subfolders
Dry-run mode that previews changes without actually moving anything"""
#preview mode
#undo
#duplicate detection
#empty-folder cleanup
"""from pathlib import Path
import re

def find_files(path: Path = Path.cwd(), ext: str = 'txt') -> list[Path]:
    if not isinstance(path, Path):
        raise ValueError("expected Path on arg 1")
    elif not isinstance(ext, str):
        raise ValueError("expected str on arg 2")
    elif not path.exists():
        return []

    if ext == "*":
        files = [f for f in path.rglob("*") if f.is_file()]
    else:
        files = list(path.rglob(f"*.{ext}"))
    return files"""
    
    
class Organizer:
    def __init__(self,path=Path.cwd()):
        #path serves as the directory to organize.
        if not isinstance(path,(str,Path)):
            raise TypeError
        self.base_path = Path(path).resolve()
        if not path.exists():
            raise FileNotFoundError
        if path.is_file():
            raise ValueError
        self.scanned_files = []
      
        self.CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp", ".ico", ".tiff"],
    "videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv", ".webm"],
    "audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "documents": [".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".txt", ".md", ".rtf"],
    "archives": [".zip", ".tar", ".gz", ".rar", ".7z", ".bz2"],
    "code": [".py", ".js", ".ts", ".html", ".css", ".java", ".c", ".cpp", ".go", ".rs", ".php", ".rb", ".sh"],
    "data": [".json", ".csv", ".xml", ".yaml", ".yml", ".toml", ".sql", ".db"],
    "executables": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".apk"],
    "fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "misc": []  # catch-all for anything unrecognized
}
        
    def scan(self,max_depth:int=None):
        base = self.base_path
        
        
        
        for i in base.rglob("*"):
            if i.is_dir():
                continue
            depth = i.relative_to(base).parts            
            #print(depth,len(depth))
            
            if max_depth is None or len(depth) <= max_depth:
                self.scanned_files.append((i,len(depth)))
        
            return self
   def _organize(self):
       pass
       #unfinished
      
    def preview(self):
        pass                      
    def __repr__(self):
        return f"Organizer(path={self.base_path!r})"
if __name__ == "__main__":
    Organizer = Organizer()
    Organizer.scan()
    print(Organizer.scanned_files)