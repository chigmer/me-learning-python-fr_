import ATBSWP_book.ZIP_backup.backup_to_zip as bz
from pathlib import Path
#this script makes zip snapshots of my entire repo, just incase i accidentally nuke .git


bz.backup_to_zip([Path.cwd()])
print("\nthe zipping process is complete.")