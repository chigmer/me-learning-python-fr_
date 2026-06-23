#csv wrapper class?
#parent = file/filepath, child = different file types
#update, inheritance isnt applicable here.
from pathlib import Path
import csv
import io
import json
#
#   

class ReadFile:
    def __init__(self,filepath: Path | str):
        try:
            abs_path = Path(filepath).resolve()
        except TypeError as err:
            raise TypeError(err)
        if abs_path.exists() and abs_path.is_file():
            pass
        elif abs_path.exists() and abs_path.is_dir():
            raise NotADirectoryError("File class doesn't support directories")
        else:
            raise FileNotFoundError(f"no file/dir found in Path: {abs_path}")       
        self.file = abs_path        
    
    def read(self):
        if self.file.suffix == ".csv":
         self._extract_csv()
        elif self.file.suffix == ".json":
            self._extract_json()           
        elif self._is_text_file():
            self._extract_plaintext()
        else:
            print("file not supported")
            return
            
        
    def _is_text_file(self) -> bool:
        with open(self.file, "rb") as f:
            sample = f.read(8192)

        if b"\x00" in sample:
            #1st check: NUL byte existence
            return False

        try:
            sample.decode("utf-8")
            #2nd check: utf-8 decoding
            return True
        except UnicodeDecodeError:
            return False       
    def _extract_plaintext(self) -> io.TextIOWrapper:
        with open(self.file,"r",encoding="utf-8") as f:
            for line in f:
                print(line,end="")
            
    def _extract_csv(self) -> csv.reader:
        with open(self.file, "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
            
    def _extract_json(self):
        with open(self.file, "r", newline="") as f:
            data = json.load(f)
            print(data)
            
        
    
   
        
        
    

        
ReadFile("Car.py").read()
#print(obj.file)