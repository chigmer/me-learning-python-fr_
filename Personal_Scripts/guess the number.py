import random
import time

numbers = list(range(1, 51))
player_score = 0

while player_score < 6:
    com_choice = random.choice(numbers)
    player = int(input("Guess the number (1-50)> "))

    if player == com_choice:
        print("You guessed right, gg")
        player_score += 1
        if player_score == 5:
            print("You won!")
            break
    else:
        print(f"Wrong, the number was {com_choice}. Try again.")