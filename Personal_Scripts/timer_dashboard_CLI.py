#a CLI script that allows you to:
#set a timer 
#positional args: 'task', the task thou is doing
# plus something like [int] hrs [int] min [int] sec, default is 0,but positional since you need atleast one value,max vals is 48-120-120, doubled everything
#update: you need ALL values, this solves ambiguity, is easier to understand and easy to implement in code
#content: refreshes every second, displays task and a live counter in format HH:MM:SS,  if M and S then MM:SS
#flags: --warning -w, caps lock mode + funny but serious lines for motivation

import argparse
def parse_args():
    parser = argparse.ArgumentParser(description="Timer script! Better than your clock app.")
# Add arguments here
    parser.add_argument(
    "task", 
    type=str, 
    help="The name of the task you plan to do.",    
    )  
    parser.add_argument(
    "time",
    type=int,
    nargs=3,
    help="usage: <hrs> <min> <sec>, all args required!"
    )
    #adding three flags for each unit of time is too long for a line. imo
    parser.add_argument(
    "-w",
    "--warning",
    action="store_true",
    help="Optional flag for activating warning mode."
    )

    args = parser.parse_args()
    return args

def format_time(time:int): #accepts total secs"
    total = time
    new_time = []
    #total = total seconds
    
    new_time.append(total//3600)
    new_time.append((total%3600)//60)
    new_time.append((total%3600)%60)
    return new_time
        
        
def display_time(time:list):
    if time[0]:
        counter = f"{time[0]}:{time[1]:02}:{time[2]:02}"
    elif time[1]:
        counter = f"{time[1]:02}:{time[2]:02}"
    else:
        counter = f"{time[2]:02}"
        
    return counter
   
    
        
        
if __name__ == "__main__":
    import time
    import random
    #own module
    from soft_words import word_bank
    args = parse_args()
    
    
    
    #test before i write real code so i dont waste an hour debugging
    #
    #args:
    #task-str
    #time- [H,M,S]
    #warning-toggle boolean
    total = args.time[0] * 3600 + args.time[1] * 60 + args.time[2]
    words =word_bank
    chosen_word = ""
    
    while total >= 0:
        if args.warning:
            if random.random() < 0.2:
                chosen_word = random.choice(words)        
        current_time = format_time(total)   
        display_current_time = display_time(current_time)             
    # convert and display here
        
        print(f"\r{args.task} |  {display_current_time} {chosen_word}",end="",flush=True)
        
        time.sleep(1)
        total -= 1
    print("\nbeep boop beep. alarm is done, hopefully your work is done too.")
    
