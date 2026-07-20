from pathlib import Path
import json
#log a function's return value to a json file, specify
#a path to create the file in
def log(path=None,filename="logs.json",write_mode="a"):
    def decorator(func):
        def wrapper():
            nonlocal path
            if write_mode.lower() not in ["a","w"]:
                    raise TypeError("invalid write mode")
            try:
                path = Path(path) if path is not None else Path.cwd()
              
                path.mkdir(parents=True,exist_ok=True)
                filepath = path / filename
                content = func()
                if content is None:
                    return
                if filepath.exists() and write_mode == "a":
                    if not isinstance(content,dict):
                        content = list(content)
                        #continue here
                    with open(filepath, "r") as file:
                        try:
                            existing = json.load(file)
                        except json.JSONDecodeError:
                            existing = []  # incase of corruption
                    if isinstance(existing,list):
                        content = existing + content
                    
                        
                    elif isinstance(existing,dict):
                        raise TypeError(f"invalid format {type(content).__name__}")
                      
                    
                            
               
                
                    
                with open(path/filename,"w") as file:
                    json.dump(content,file)
            except Exception as e:
                print(e)
                return
            
            
        return wrapper
    return decorator