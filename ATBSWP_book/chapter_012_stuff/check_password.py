import argparse
import re
def parse_args() -> str:
    parser = argparse.ArgumentParser(
        epilog="this script gives your password strength locally"
    ) 
    parser.add_argument("user",type=str,metavar="password",help="your password")
    args = parser.parse_args()
    user = args.user
    return user
def is_min_eightchar(password:str) -> bool:
    if not isinstance(password,str):
        raise ValueError("password must be a string")

    return bool(re.fullmatch(r"[^\s]{8,}",password))
def is_upper_and_lower(password:str) -> bool:
    if not isinstance(password,str):
        raise ValueError("password must be a string")
    return bool(re.search(r"[a-z]",password) and re.search(r"[A-Z]",password))
def has_digit(password:str) -> bool:
        if not isinstance(password,str):
            raise ValueError("password must be a string")
        return bool(re.search(r"\d",password))
        
#Actual function:
def is_strong_password(password:str):
     if not isinstance(password,str):
            raise ValueError("password must be a string")
     if is_min_eightchar(password):
         if is_upper_and_lower(password):
            if has_digit(password):
                return True, "Your password is strong"
            else:
                return False, "password doesn't have a number"           
         else:
             return False, "password only has lowercase/uppercase letters"
     else:
         return False, "password is less than eight characters (spaces excluded)"
def main():
    user = parse_args()
    print(f"\nyou typed: {user}")
    #bool, message
    strong,message = is_strong_password(user)
    if strong:
        print(message)
    else:
        print(f"Your password is not strong: {message}")
        
if __name__ == "__main__":
    main()
        
    
    
    
    
    
    