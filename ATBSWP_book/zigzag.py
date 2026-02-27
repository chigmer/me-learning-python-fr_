import time
import sys

indent = 0  # How many spaces to indent
indent_increasing = True  # Whether the indentation is increasing or not

try:
    while True:  # The main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)  # Pause for 1/10th of a second

        if indent_increasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indent_increasing = False
        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indent_increasing = True

except KeyboardInterrupt:
    # This catches Ctrl+C so the program doesn't throw a messy traceback
    print("\nFine, I'll stop. It's not like you were actually watching it.")
    sys.exit()
        