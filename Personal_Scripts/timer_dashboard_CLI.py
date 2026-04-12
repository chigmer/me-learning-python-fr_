#!/usr/bin/env/python3
import argparse
import time
import random
import sys



def parse_args():
    parser = argparse.ArgumentParser(description="Timer script! Better than your clock app.")
    parser.add_argument("task", type=str, help="The name of the task.")  
    parser.add_argument("time_vals", type=int, nargs=3, metavar=('HRS', 'MIN', 'SEC'),
                        help="usage: <hrs> <min> <sec>, all args required!")
    parser.add_argument("-w", "--warning", action="store_true", help="Activate warning mode.")
    return parser.parse_args()

def format_time(total_seconds):
    """Converts total seconds into a list of [H, M, S]."""
    hrs = total_seconds // 3600
    mins = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    return [hrs, mins, secs]

def display_time(time_list):
    """Formats the time list into a readable string."""
    h, m, s = time_list
    if h:
        return f"{h}:{m:02}:{s:02}"
    return f"{m:02}:{s:02}"

def main():
    #  soft_words is a local file
    try:
        from soft_words import word_bank
    except ImportError:
        word_bank = ["DO YOUR WORK", "TICK TOCK", "STOP SLACKING"]
        #portability just in case module doesnt exist
        #or isnt in the same directory

    args = parse_args()
    
    # Calculate total seconds from the 'time_vals' list
    h, m, s = args.time_vals
    total = h * 3600 + m * 60 + s
    chosen_word = ""

    try:
        while total >= 0:
            if args.warning and random.random() < 0.2:
                chosen_word = random.choice(word_bank)
            
            current_time = format_time(total)   
            display_str = display_time(current_time)             
            
            # Using sys.stdout.write is sometimes cleaner for \r, 
 
            print(f"\r{args.task} | {display_str} {chosen_word}", end="", flush=True)
            
            time.sleep(1)
            total -= 1
            
        print("\nbeep boop beep. Alarm is done. Go outside.")

    except KeyboardInterrupt:
        # Boilerplate for "User got bored and hit Ctrl+C"
        print("\nTimer aborted. Quitting before you actually finished anything?\nif youre the creator, i'll allow it.")

if __name__ == "__main__":
    main()
