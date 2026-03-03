import re
def is_it_palindrome(word:str)-> bool:        
    
    if not isinstance(word,str):
        raise TypeError("thou input is not a string")
    clean = re.sub(r'[^a-zA-Z0-9]', '', word).lower()
    return clean == clean[::-1]

    
    
if __name__ == "__main__":
   print(is_it_palindrome("Racecar"))
   print(is_it_palindrome("baggy jeans"))
   print(is_it_palindrome("taco cat"))
   print(is_it_palindrome("A man, a Plan, a canal: Panama"))
    

#regex trick learned online(AI)
        
        