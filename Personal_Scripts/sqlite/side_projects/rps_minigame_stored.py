import sqlite3
import random
import time
from datetime import datetime
conn = sqlite3.connect("rps_data.db")
cur = conn.cursor()
#Play an RPS game with a bot, best of 5
#store the results in two tables, one storing each session
#and one displaying info from each of those sessions
#(use left joining in case user quits midway)
#also make the logic for rps from scratch.
def get_now():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return now
def player_won(player:str,computer:str):
    """The Logic, biased towards the player in its logic style"""
    #clean the data before calling this
    choices = ["r","p","s"]
    assert player in choices and computer in choices
    
    if player == computer:
        return None
    #I think consecutive elif statements would make 
    #this part easier to understand
    elif player == "r" and computer == 's' or player == "p" and computer == "r" or player == "s" and computer == "p":
        return True
    else:
        return False
        
    
def main():
    cur.execute("""
CREATE TABLE IF NOT EXISTS sessions (
    source_id INTEGER PRIMARY KEY,
    winner TEXT,
    started_at TEXT
) STRICT
""")
    cur.execute("""
CREATE TABLE IF NOT EXISTS game (
    game_number INTEGER PRIMARY KEY,
    source_id INTEGER, 
    player_won INTEGER,
    computer_won INTEGER,
    played_at TEXT
) STRICT
""")
    
    
    
    

    #source_id, session, winner, started_at




    
    player_wins = 0
    computer_wins = 0
    i = 0
    choices = ["rock","paper","scissors"]
    now = get_now()
    cur.execute("INSERT INTO sessions (started_at) VALUES (?)",(now,))
    parent_id = cur.lastrowid
    conn.commit()
    print("Welcome to R-P-S.\nPick either:\n[1] rock\n[2] paper\n[3] scissors\n\nFirst to Five\n")
    time.sleep(0.4)
    while player_wins < 5 and computer_wins < 5:
        i += 1
        player = 0
        com = 0
        user = input(">").strip()
        try:
            user = int(user)
            if not 0 < user < 4:
                print("invalid choice!")
                continue
            if user == 1:
                user = "r"
            elif user == 2:
                user = "p"
            elif user == 3:
                user = "s"
        except ValueError:
            if user.lower() not in choices and not user.lower().startswith(("r","p","s")):
                print("didnt catch that, perhaps you typed wrong?")
                continue
            user = user[0]
        time.sleep(.4)
        com_choice = random.choice(choices)
        print(f"Computer chose: {com_choice}")
        result = player_won(user,com_choice[0])
        if result is None:
            print("its a tie!")
            continue
        elif result:
            print("you won!")
            player_wins += 1
            player += 1
        else:
            print("you lost.")
            computer_wins += 1
            com += 1
        time.sleep(0.3)
        game_data = (parent_id,player,com,now)
        cur.execute("INSERT INTO game (source_id,player_won,computer_won ,played_at) VALUES (?,?,?,?) ",game_data)
        if i >= 69:
            break
    time.sleep(1.5)  
    if player_wins == 5:
        print("Congrats, never doubted you for a second")
        
        cur.execute("""UPDATE sessions
SET winner = 'player'
WHERE source_id = ?
""",(parent_id,))

    elif computer_wins == 5:
        print("rock paper scissors is just a child's game anyway. dont let it get to you.")
        cur.execute("""UPDATE sessions
SET winner = 'computer'
WHERE source_id = ?
""",(parent_id,))
    else:
        print("thats some serious dedication dude.")
        cur.execute("""UPDATE sessions
SET winner = NULL
WHERE source_id = ?
""",(parent_id,))
    conn.commit()


if __name__ == "__main__":
    main()
        
            
        
        
            
    
    
    