#Strong Password Detection Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password has several rules: it must be at least eight characters long, contain both uppercase and lowercase characters, and have at least one digit. Hint: It’s easier to test the string against multiple regex patterns than to try to come up with a single regex that can validate all the rules.

""" Password security checkar """
import re
def is_min_eightchar(password:str) -> bool:
    if not isinstance(password,str):
        raise ValueError("password must be a string")
#fullmatch(pattern,sometext)
    return bool(re.fullmatch(r"[^\s]{8,}",password)) #is it a bad idea to allow whitespaces?
def is_upper_and_lower(password:str) -> bool:
    if not isinstance(password,str):
        raise ValueError("password must be a string")
    return bool(re.search(r"[a-z]",password) and re.search(r"[A-Z]",password))
def has_digit(password:str) -> bool:
        if not isinstance(password,str):
            raise ValueError("password must be a string")
        return bool(re.search(r"\d",password))
        
#Actual function:
def is_strong_password(password:str) -> tuple[bool,str|None]:
     if not isinstance(password,str):
            raise ValueError("password must be a string")
     if is_min_eightchar(password):
         if is_upper_and_lower(password):
            if has_digit(password):
                return True, None
            else:
                return False, "password doesn't have a number"           
         else:
             return False, "password only has lowercase/uppercase letters"
     else:
         return False, "password is less than eight characters (spaces excluded)"
    
#these funcs technically return tuples, which is the best kind. but I feel like using -> tuple will confuse people more  
if __name__ == "__main__":
    import time as t
    print("Password Test.")
   
    user = input("type your password: ")
    print()
    t.sleep(0.5)
    #by the way, i did this without a single use of google, since im in class
    print(is_strong_password(user))
    
    
        