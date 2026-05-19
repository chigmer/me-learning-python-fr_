import time,random

def choose_equation() -> int | float:
    a = random.randint(-100,1000)
    b = random.randint(-100,1000)
    op = random.choice(["*", "+", "-", "/"])
    if op == "+":
        ans = a + b
    elif op == "-":
        ans = a - b
    elif op == "*":
        ans = a * b
    else:
        ans = a / b
        
    print(f"{a} {op} {b} = {ans:,}")

print("I will do some random mathematical operations\npause if you must by pressing Ctrl + C\n\n")
while True:
    try:
        time.sleep(1.5)
        choose_equation()
    except KeyboardInterrupt:
        time.sleep(0.33)
        print("Paused.\n")
        while True:
            try:
                print("Tick")
                time.sleep(1)
                print("Tock")
                time.sleep(1)
            except KeyboardInterrupt:
                print("Unpaused.\n")
                break
                
        
    

  