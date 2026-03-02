#import pyperclip
#install pyperclip first, and you may finally actually do the intended activity by Al Sweigart
import sys


print("want bulleted text?, i gotchu\njust paste them here\n")

content = []

print("press Enter to confirm")
while True:
    line = input()
    if line == "":
        break
    if len(line) >= 999999:
        print("woah. too long.")
        sys.exit()
    
    content.append(line)
    
    
if not content:
    print("no input detected. nice try.\nexiting")
    sys.exit()
print()
    
try:
    for sentence in content:
        if sentence:
            print(f"* {sentence}")
        
except Exception as e:
    print(f"something fuckin happened \n{e}")
    sys.exit()
    
    
    



#goal. add a star symbol on every sentence. (e.g. *Lists of something *List of a list of something)

