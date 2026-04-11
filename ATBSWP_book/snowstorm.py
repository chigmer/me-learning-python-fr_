import os
import random
import time
import sys

TOP = chr(9600)      # '▀'
BOTTOM = chr(9604)   # '▄'
FULL = chr(9608)     # '█'

# Default snow density (%)
DENSITY = 4

# Override density from command line if provided
if len(sys.argv) > 1:
    DENSITY = int(sys.argv[1])


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    clear()

    # Snow field
    for y in range(20):
        for x in range(40):
            if random.randint(0, 99) < DENSITY:
                print(random.choice([TOP, BOTTOM]), end='')
            else:
                print(' ', end='')
        print()

    # Ground
    print(FULL * 40)
    print(FULL * 40)

    print('(Ctrl-C to stop.)')

    time.sleep(0.35)