import random 
streaks = 0
print("welcome.")
print()
print("preparing results..")

for _ in range(10000):
    coin_values = []
    for i in range(100):
        za_coin = random.randint(0,1)
        if za_coin == 0:
            coin_values.append("H")
        elif za_coin == 1:
            coin_values.append("T")
            #could make this code shorter, but i wanted clarity for me, when reading this any other day than today
    for i in range(len(coin_values)):
        if coin_values[i:i+6] == ["H"] * 6 or coin_values[i:i+6] == ["T"] * 6:
            streaks += 1
            break
            

   
    
    
    

    
    
print("done")
print()
print()
print(f"total streaks across 10,000 experiments: {streaks}")
print()
print("therefore, the chance for a 6-sided coinflip streak in any 100 attempt coin flip session is approximately..")
print(str((streaks / 10000) * 100) + "%")

    
    

     

# Run 10,000 experiments total. # Code that creates a list of 100 'heads' or 'tails' values
# Code that checks if there is a streak of 6 heads or tails in a row print('Chance of streak: %s%%' % (number_of_streaks / 100))
#me here, above this comment is the "guide" of the course. anyway, ill interpret the first comment to be 100,000 instances of 100 list values.