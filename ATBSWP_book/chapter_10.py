"""


Practice Questions

1. What is a relative path relative to? 
2. What does an absolute path start with? 
3. What does Path('C:/Users') / 'Al' evaluate to on Windows? 
4. What does 'C:/Users' / 'Al' evaluate to on Windows? 
5. What do the os.getcwd() and os.chdir() functions do? 
6. What are the . and .. folders? 
7. In C:\bacon\eggs\spam.txt, which part is the directory name, and which part is the base name?
8. What three “mode” arguments can you pass to the open() function for plaintext ﬁles?
9. What happens if an existing ﬁle is opened in write mode?
10. What is the difference between the read() and readlines() methods? 11. What data structure does a shelf value resemble?



"""
answers = """
1. the Current Working Directory of the program
2. the root (e.g. 'C:/' or '/')
3. WindowsPath('C:/Users/Al')
4. an error message
5. os.getcwd()returns the current working directory, os.chdir() changes the directory the program is running inqq
6. ./ is the cwd, ../ is the adjacent parent directory of the cwd (the last directory before cwd)
7. dir name: eggs, base name: spam.txt
8. append, write, and read, not counting the variants like 'w+'
9. the file will be overwritten.
10. read returns the entire contents of the file as one string,  readlines() returns a list of strings separated by newlines (atleast what I saw earlier, could be wrong)
11. dictionaries



"""