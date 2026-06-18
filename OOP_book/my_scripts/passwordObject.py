#turn a past script to a class
import secrets

class LengthError(Exception):
    """too long of an input"""
    pass

class Password:

    def __init__(self):
        
        self.char_bank = {
    'uppercase' : "ABCDEFGHIJKLMNOPQRSTUVWXYZ",

'lowercase' : "abcdefghijklmnopqrstuvwxyz",

'numbers' : "0123456789",

'special_characters' : " !?.,:;-_()[]{}'\"/@#&%+*=<>"
} 
       

    def create_password(
        self,
        length=10,
        letters=True,
        uppercase=True,
        lowercase=True,
        numbers=True,
        special_chars=True,
        exclusions=None
    ):
        self._validate_param(
            letters,
            uppercase,
            lowercase,
            numbers,
            special_chars
        )
        if exclusions is None:
            exclusions = []
        char_bank = self.char_bank.copy()
        if not letters:
            del char_bank["uppercase"]
            del char_bank["lowercase"]
        elif letters:
            if not uppercase:
                del char_bank["uppercase"]
            if not lowercase:
                del char_bank["lowercase"]
        if not numbers:
            del char_bank["numbers"]
        if not special_chars:
            del char_bank["special_characters"]
            
        
        if len(char_bank) < 1:
            raise Exception  # i have no idea what error to raise. will fix later?
         
        else:
            chars = ""
            for i in char_bank.values():
                chars += i
        if not isinstance(length, int):
            raise TypeError("length must be an int")

        if length <= 0:
            raise ValueError("invalid length")

        if length >= 100000:
            raise ValueError("dont make a password this long.")
        if exclusions: 
            char_bank = list(char_bank)
        for ex in exclusions:
            
            if ex in char_bank:
                char_bank = [character for character in char_bank if character != ex]
        if len(char_bank) < 1:
            return 
            
        char_bank = ''.join(char_bank)                       
        password = ""                                 

        for _ in range(length):
            password += secrets.choice(char_bank)

    def _validate_param(self,*args):
        for arg in args:
            if not isinstance(arg, bool):
                raise TypeError("invalid type for parameter")


if __name__ == "__main__":
    oPassword = Password()
    pass_1 = oPassword.create_password(length=20)
    pass_2 = oPassword.create_password(length=20,letters=False)
    print(f"PASS 1: {pass_1}\nPASS 2: {pass_2}")
    

"""
OLD SCRIPT:

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

char_bank = r"1234567890qwertyuiopQWERTYUIOP()asdfghjklASDFGHJKLzxcvbnmZXCVBNM,.*"':;!?@#$_&-+()/<>~[]{}\\/' #no punctuation characters except for ? and ! because its cool as hell

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
current_date = current_date.strftime("%B %d, %Y")

time.sleep(0.08)
with open("password_list.txt", "a") as p:
    p.write(f"Password: {password}\n Notes: {notes}\n Date: {current_date}\n")
    p.write("\n")
    p.write("\n")
"""