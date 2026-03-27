"""Practice Questions

1. What is the difference between shutil.copy() and shutil.copytree()? 2. What function is used to rename ﬁles?
3. What is the difference between the delete functions in the send2trash and shutil modules?

4. ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?"""

"""
1. shutil.copy() copies a single file, shutil.copytree() can copy a directory and its contents
2.shutil.move(),if you move a file to a path that includes a filename, the file will get renamed by said filename
3. send2trash delete functions move the file to the recycle bin, shutil delete functions delete the file permanently
4. zipfile.ZipFile()

"""