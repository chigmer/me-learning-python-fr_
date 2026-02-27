def is_it_palindrome(word:str)-> bool:
    if not isinstance(word,str):
        raise TypeError("thou input is not a string")
    word = word.lower().strip().replace(" ", "")
    return word == word[::-1]
    
    
if __name__ == "__main__":
   print(is_it_palindrome("Racecar"))
   print(is_it_palindrome("baggy jeans"))
   print(is_it_palindrome("taco cat"))
   
    


        
        