#import intelligence, critical thinking skills

print("palindrome checker vers. 1")

word = input("Type your word here: ")
x = -1
rev = ""

while len(rev) < len(word):
    i = word[x]
    rev += i
    x += -1
        
print(f"You typed: {word}")
print(f"It is...")
if rev == word:
    print("A Palindrome!!")
else:
    print("Not a Palindrome!!")
    


