import time,sys,secrets,datetime
print("Want a password? (Y/n)")
#choice
#choice.lower().strip()
#sys.exit()

while True:
    choice = input(">")
    choice = choice.lower().strip()
    if choice == "n":
        print("affirmative")
        sys.exit()
    elif choice == "y":
        break
    else:
        print("invalid response")
while True:
    length = input("length: ")
    try:
        length = int(length)
    except ValueError:
        print("invalid response.  input must be an integer")
        continue   
    
    
    if length > 60:
        print("too long for a standard password. you are NOT protecting the US government.")
    elif length <= 3:
        print("invalid length")
        
    else:
        break
       
    
    
   
char_bank = r"1234567890qwertyuiopQWERTYUIOP()asdfghjklASDFGHJKLzxcvbnmZXCVBNM!?#&*<>%" #no punctuation characters except for ? and ! because its cool as hell
time.sleep(0.5)
print()
password = ""

for _ in range(length):
    password += secrets.choice(char_bank)
time.sleep(0.5)
print(password)
print()
notes = input("Notes: ")
current_date = datetime.datetime.now()
current_date =  current_date.strftime("%B %d, %Y")

    
    

time.sleep(0.08)
with open("password_list.txt","a" ) as p:
    p.write(f"Password: {password}\n Notes: {notes}\n Date: {current_date}\n")
    p.write("\n")
    p.write("\n")
    
    # TODO:
# 1. Ask user for desired password length (validate integer and reasonable range)
#✓

# 2. Use `secrets.choice()` for cryptographically secure randomness 
#✓

# 3. Append generated passwords to a text file instead of just printing
#✓
#read a python doc
#i have returned from the shadows and improved this feb 17, 2026
#update. todo: os.path to make the script run from anywhere
 #todo: encrypt the txt file. i dont know how or what. but just keep this in mind   
    
    
    
        

