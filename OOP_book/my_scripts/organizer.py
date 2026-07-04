from pathlib import Path
import sys,shutil,json
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
class Organizer:
    def __init__(self,path=Path.cwd()):
        #path serves as the directory to organize.
        if not isinstance(path,(str,Path)):
            raise TypeError
        self.base_path = Path(path).resolve()
        self.logs = "Logs.json"
        if not self.base_path.exists():
            raise FileNotFoundError
        if self.base_path.is_file():
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
    "misc": []
    # add catch-all for anything unrecognized, 'misc'
}
        
    def scan(self,max_depth:int=None):
        base = self.base_path
        
        
        
        for i in base.rglob("*"):
            if i.is_dir():
                continue
            depth = i.relative_to(base).parts            
            #print(depth,len(depth))
            
            if max_depth is None or len(depth) <= max_depth:
                self.scanned_files.append(i)
                
            #how do I preserve dir strucutre?
            #do I ignore it and just forcibly move everything to predetermined folders?
        
        return self
    def _get_category(self,ext):
        for category,ext_list in self.CATEGORIES.items():
            if ext in ext_list:
                if not category == "misc":
                    return category
        return "misc"
    def _log(self,source:list,dst:list):
        #must have correct indexes.
        data_to_save = {}
        for i,src in enumerate(source):
            data_to_save[src] = dst[i]
        with open(self.logs,"a") as file:
            json.dump(data_to_save, file, indent=4)
    def _extract(self):
        with open(self.logs, "r") as file:
            return json.load(file)
       

        
   
    
                                                     
        
        
               
    def organize(self,preview=True,show_process=True):
        preview_dict = {}
        for i in self.CATEGORIES.keys():
           
           
            preview_dict[i] = []
                    
        src_list = []
        dst_list = []
       
        for file in self.scanned_files:            
            category = self._get_category(file.suffix.lower())                                    
            if not preview:                                   
                try:                   
                    src = file
                    dst = self.base_path / Path(category)
                    dst.mkdir(exist_ok=True)
                    if show_process:
                        print(f"moving {src.name} to {dst.name}")
                    #shutil.move(src,dst) 
                    
                    src_list.append(f"{str(src)}")          
                    dst_list.append(f"str(dst)")      
                    #CONTINUE HERE   
                                     
                except Exception as e:
                    print(f"Error: {e}")
                    sys.exit(1)
            else:
                preview_dict[category].append(file.name)
                
        #this loop doesnt run when preview mode is off because the dict is empty 
        if not preview and src_list and dst_list:
            self._log(src_list,dst_list)       
            print(self._extract())
        for cat,item in preview_dict.items():
            if not preview:
                break
            if item:
                print(f"{cat}/")                        
                   
                for f in item:
                  
                    print(f"   |__{f}")                         
    def __repr__(self):
        return f"Organizer(path={self.base_path!r})"
if __name__ == "__main__":
    org = Organizer()
    org.scan().organize(False)
    #method chaining for a clean one liner
    print("TEST!!!")
    
    
    print(org.base_path)