from pathlib import Path
import shutil
import re
#rglob() coming in clutch, by walking through a folder I'll use a user supplied Path object relative to the cwd
#the file extension is also user supplied
#create dir "{extension} files"
#use shutil.copy()
def mkdir_and_find_extension(ext:str,path=Path.cwd()) -> tuple[list[Path], Path]:
    if not isinstance(ext,str):
        raise ValueError(f'expected str object in argument 1, got {type(ext).__name__}')        
    elif not isinstance(path,Path):
        raise ValueError(f'expected Path object in argument 2, got {type(path).__name__}')
    if not re.fullmatch(r"\.[a-zA-Z]+",ext):
        raise TypeError("invalid filename extension")
    #safeguards for dev
    file_dir = Path(f"{ext[1:]} files")
    file_dir.mkdir(exist_ok=True)
    files = []
    for file in path.rglob(f"*{ext}"):
        print(f"found {file.name}")
        files.append(file)
    return files,file_dir

def copyfiles(file_list,target_dir) -> None:
    if not file_list:
        print("no files found.")
        return
    for file in file_list:
        shutil.copy(file,target_dir/file.name)
    print(f"copied {len(file_list)} files to {target_dir}")



if __name__ == "__main__":
    print("type a filename extension (e.g. .txt, .docx), and you shall get the corresponding files.")
    while True:
        user_input = input('>')
        if not re.fullmatch(r"\.[a-zA-Z]+",user_input):
            print('invalid filename extension')
            continue
        break
    files, path = mkdir_and_find_extension(user_input)
    copyfiles(files,path)
    print("cool\ndone.")
    #stuck to cwd for simplicity
    
    

        

        
