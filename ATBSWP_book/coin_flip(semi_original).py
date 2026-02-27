import random
H_count = 0
T_count = 0

for i in range(11):
    result = random.randint(0,1)
    if result == 0:
        print("Heads", end = " ")
        H_count += 1
    elif result == 1:
        print("Tails", end = " ")
        T_count += 1


print()    
print()    
print(f"Number of heads from the flips: {H_count}")
print(f"Number of tails from the flips: {T_count}")