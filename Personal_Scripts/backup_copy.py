#copy both project folders as a backup.
from pathlib import Path
import shutil

p = Path.home()
shutil.copytree(Path.cwd(), p/ "script_backups",dirs_exist_ok=True)
backup_count = 0
for file in (p/"script_backups").rglob("*"):
    print(f"Found: {file.name}" )
    backup_count += 1
    
source_count = len(list(Path.cwd().rglob("*")))


if source_count == backup_count:
    print("Backups created successfully")
else:
    print(f"Warning: source has {source_count} files, backup has {backup_count}")