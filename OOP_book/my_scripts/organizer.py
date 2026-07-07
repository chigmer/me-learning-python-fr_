from pathlib import Path
import sys,shutil,json
#File Organizer
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
        self.file_location = Path(__file__).resolve()
        self.logs = "Logs.json"
        if not self.base_path.exists():
            raise FileNotFoundError
        if self.base_path.is_file():
            raise ValueError
        self.scanned_files = []
        self.exclude = {
    Path(__file__).resolve(),
    (self.base_path / self.logs).resolve()
}
       
      
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
        self.scanned_files.clear()
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
    def _unique_path(self,path):
        if not path.exists():
            return path

        counter = 0
        while True:
            counter += 1
            new_path = path.with_stem(f"{path.stem}_{counter}")
            if not new_path.exists():
                return new_path
        
        
    def _get_category(self,ext):
        for category,ext_list in self.CATEGORIES.items():
            if ext in ext_list:
                if not category == "misc":
                    return category
        return "misc"
    def _log(self,data_to_save:list):
        #[{src:dst},{...}]
        #scrap that.
        with open(self.logs,"w") as file:
            json.dump(data_to_save, file, indent=4)
    def _rm_dirs(self):
        for folder in reversed(list(self.base_path.rglob("*"))):
            if folder.is_dir():
                try:
                    folder.rmdir()
                except OSError:
                    continue
    def _extract(self):
        try:
            with open(self.logs, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("logs doesn't exist yet.")
            sys.exit(0)
       

        
   
    
                                                     
        
        
               
    def organize(self,preview=True,show_process=True):
        preview_dict = {}
        log_data = []
        
        for i in self.CATEGORIES.keys():
           
           
            preview_dict[i] = []
                    
        
       
        for file in self.scanned_files:            
            category = self._get_category(file.suffix.lower())            
                                    
            if not preview:  
                if file in self.exclude:
                    continue                                 
                try:                   
                    src = file                    
                    folder = self.base_path / Path(category)
                    dst = folder / file.name
                    final_dst = self._unique_path(dst)
                    
                    if show_process:
                        print(f"moving {src.name} to {category}")
                        #print(f"src: {src} dst: {dst}")
                       
                       
                    folder.mkdir(exist_ok=True,parents=True)
                    log_data.append(
                        {                            
                            "src":str(src),
                            "dst":str(final_dst)                        
                        }
                        )
                    shutil.move(src,final_dst) 
                        #actual moving line!
                        #I cannot believe it took me a few days of my fucking time to design an organizer
                        #around this gimmick                                                                                  
                                     
                except Exception as e:
                    
                    print(f"Error: {e}")
                    raise 
                    
               
            else:
                preview_dict[category].append(file.name)
        if not preview:
            self._log(log_data)
            
        
                
                
        #this loop doesnt run when preview mode is off because the dict is empty 
        
        for cat,item in preview_dict.items():
            if not preview:
                break
            if item:
                print(f"{cat}/")                        
                   
                for f in item:
                  
                    print(f"   |__{f}")  
                print('\n\n')  
        if show_process:
            print("Removing dirs...")                
        self._rm_dirs()  
    def undo(self):
        for move in reversed(self._extract()):
            src = Path(move["src"])
            dst = Path(move["dst"])

            if dst.exists():
                src.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(dst, src)    
            
            
        
    def __repr__(self):
        return f"Organizer(path={self.base_path!r})"
if __name__ == "__main__":
    org = Organizer()
    org.scan().organize(False,True)
    print(org.file_location)
    
    #help(org)
    org.undo()
    #method chaining for a clean one liner
    