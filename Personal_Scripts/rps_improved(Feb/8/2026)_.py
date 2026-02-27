import random
import time

choice_list = ("rock", "paper", "scissors")
    
player_wins = 0
computer_wins = 0

while player_wins < 5 and computer_wins < 5:
 
 
  player = input("Welcome to Rock-Paper-Scissors, type your answer>") 
  time.sleep(2)
  computer_decision = random.choice(choice_list)
  
  print("You chose", player)
  time.sleep(2)
  print("Computer chose", computer_decision)
  
  
  if player == computer_decision:
      print ("It's a tie.")
      
  elif (player == "rock" and computer_decision == "scissors" or
  player == "paper" and computer_decision == "rock" or
  player == "scissors" and computer_decision == "paper"):
      print("You won.")
      player_wins += 1
  
  else:
      print("Computer wins!")
      computer_wins += 1



print ("Good game, it's over")
      