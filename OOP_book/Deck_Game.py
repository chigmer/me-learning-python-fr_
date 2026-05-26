"""This is my own version, recreated from general observation"""
#Read Card higher or lower game. doing it myself to spot the gaps.

#define a card
#store every piece of card in a list, effectively being a deck
#user input: Play? yes or no
#Loop: Loop each game
#Inner loop: a game lasts 8 rounds, or whatever the global variable says
#First Loop: prepare shuffled Deck, with Current Card Info. (suit,rank,value(for non ambiguous card definitions)) (use pop() to ensure no duplicates)
#Inner Loop: take the next Card Dict from the deck, compare to the current one, the current card should be displayed first
#Next Card -> Current Card for Next Game -> Next Card to compare to, popped card dict from the shuffled list.
#GOO
import random


SUIT_LIST = ['Spades','Hearts','Clubs','Diamonds']
RANK_LIST = ['Ace'] + list(range(2,11)) + ['Jack','Queen','King']
Proper_Deck = []
#Define A Card by suit, rank, and value
for suit in SUIT_LIST:
    for value,rank in enumerate(RANK_LIST,start=1):
        ThisCard = {
            'suit': suit,
            'rank': rank,
            'value': value  
            
        }
        Proper_Deck.append(ThisCard)
        
#for card in Proper_Deck:
#    print(f"Card: {card}\n")

#Actual Logic
print("Higher or Lower card game!!\nYour Job is to guess if the Next Card")
print("is Higher, Lower, or is equal to the current card\ninfront of you")
print("you start with 50 points.")
#main Loop to start ONE game.
rounds = 8
score = 50
while True:
    SHUFFLED_DECK = Proper_Deck[:]
    random.shuffle(SHUFFLED_DECK)
    #print(SHUFFLED_DECK)
    #prepare current Card for game
    current_card = SHUFFLED_DECK.pop()
    #unpack card info
    current_card_suit = current_card['suit']
    current_card_rank = current_card['rank']
    current_card_value = current_card['value']
    #print(f"the card is: {current_card_rank} of {current_card_suit} Value: {current_card_value} ")
    #game loop
    for round_ in range(1,rounds+1):
        print(f"\nround {round_}")
        next_card = SHUFFLED_DECK.pop()
        next_card_suit = next_card['suit']
        next_card_rank = next_card['rank']
        next_card_value = next_card['value']        
        print("Is it Higher, Lower, or Equal\nto the next card? (type either 'h','l', or 'eq')\n")
        print("The Current card is..\n")
        print(f"The {current_card_rank} of {current_card_suit}.")
        while True:
            user = input(">").lower().strip()
            if not user in ["h","l","eq"]:
                print("invalid. try again")
            else:
                break
        #logic to see if it was equal or not
        print("The next card was..\n")
        print(f"The {next_card_rank} of {next_card_suit}.")
        if user == "eq":
            if current_card_value == next_card_value:
                print("You were right! It is equal.")
                score += 20
            elif current_card_value < next_card_value:
                print("You were wrong. It was higher")
                score -= 15
            else:
                print("You were wrong. It was lower")
                score -= 15
            
        elif user == "h":
            if current_card_value == next_card_value:
                print("You were wrong. It is equal.")
                score -= 15
            elif current_card_value < next_card_value:
                print("You were right! It was higher.")
                score += 20
            else:
                print("You were wrong. It was lower")
                score -= 15
        else:
            if current_card_value == next_card_value:
                print("You were wrong. It is equal.")
                score -= 15
            elif current_card_value < next_card_value:
                print("You were wrong. It was higher.")
                score -= 15
            else:
                print("You were right! It was lower.")
                score += 20
        #couldve optimized this. (repeated the same thing thrice)
        print(f"Score: {score}")
        #prepare current card for next deck
        current_card_suit = next_card_suit
        current_card_rank = next_card_rank
        current_card_value = next_card_value
    print(f"Final score: {score}")
    while True:
        exit = input("Play again? (y/n)").lower().strip()
        if exit not in ['y','n']:
            print("invalid")
            continue
        else:
            break
    if exit == "y":
        pass
    else:
        break
        
print("bye.")    