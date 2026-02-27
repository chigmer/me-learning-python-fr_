import random
word = """yes
no
certainly
certainly_not
im_leaning_yes
im_leaning_no
im_not_sure
i_dont_know
"""
word_list = word.split()
def get_word():
    return random.choice(word_list)
#good idea to make an input validation function am i right?


    
print("8 ball!")
while True:
    user = input("(y/n): ").lower()
    if user in ("y", "n"):
        break
    else:
        print("invalid")
    
   
       
    
        
print("end")
        
        
  
        
        


    
    