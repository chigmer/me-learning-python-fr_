import random

class Dice():
    def __init__(self):
        self.faces = list(range(1,7))
    def roll(self):
        #methods shouldnt 'print' stuff, just return a value, right?
        value = random.choice(self.faces)
        print(f"You rolled:\n\n{value}")
if __name__ == "__main__":
    dice = Dice()
    for _ in range(5):
        dice.roll()
    