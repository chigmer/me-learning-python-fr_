#.upper() .lower() .isupper() .islower()


def hasonelowercase(word:str) -> bool: #checks argument, which is a string, if it has atleast one lowercase character
    if not isinstance(word,str):
        raise ValueError("argument must be a string literal")
    for letter in word:
        if letter.islower():
            return True
    return False
#ive realized how useless this function is.
#and ive also realized that .upper() isnt really useful in most python projects.
if __name__ == "__main__":
    print(hasonelowercase("HIIII"))
    print(hasonelowercase(""))
    print(hasonelowercase("Al Sweigart"))
    print(hasonelowercase("bologna"))
    
    