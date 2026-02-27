import random

def random_text(_):
    random_ = ("Yes", "No")
    text = random.choice(random_)
    return text
    
print("state your question, i shall judge you")
x = input(">")
print()
decision = random_text(x)
print(decision)

