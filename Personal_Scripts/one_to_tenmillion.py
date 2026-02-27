import random,time
print("if you were to receive money between one dollar to ten million dollars..")
time.sleep(1)
print("you would have..")
time.sleep(1)

number = random.randint(1,10000000)
print(f"{number:,}$")