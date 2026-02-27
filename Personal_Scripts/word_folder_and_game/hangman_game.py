#hangman temu version. doing this shit during class wish me luck.#update. this was me one day ago during math class
import random, time
import worded #custom module containing a list of 5,000 english words

print("we shall begin hangman.")
time.sleep(0.5)
correct = 0
#here lies correct = 0, the past variable that survived a 2 day journey of suffering that ultimately wasn't used in the end.
count = random.randint(5,10)
time.sleep(0.699)
word = random.choice(worded.word_list)
if len(word) >= 8:
    time.sleep(0.4)
    print("uh oh.. this ones kinda long")
    count = random.randint(10,15)
print("your number of tries are..")
time.sleep(0.6)
print(str(count) + ' attempts!' )
if count >= 14:
    time.sleep(0.3)
    print("ooooh. lucky guy")
revealed_list = [False] * len(word)
#print(word)
#no ones gonna read this but.. remove the hashtag on the previous line for cheatmode. what can I say.. competent developer am I right?
for attempts in range(1, count + 1):
    
    if revealed_list == [True] * len(word):
        print("uhhm. you..")
        break
    
    while True:
        
        print(f"Attempt: {attempts}")
        player_letter = input(">")
        player_letter = player_letter.strip().lower()
        if len(player_letter) == 1:
            break
        else:
            print("invalid")
            continue
    display = ""
    for i in range(len(word)):   
        if word[i] == player_letter:
            revealed_list[i] = True
    for iteration in range(len(word)):
         if revealed_list[iteration]:
             display += word[iteration]
         else:
             display += "_"
    time.sleep(0.23)
    print("you guessed.. " + player_letter)
    time.sleep(0.555)
    print(display)
    
#update: 1 hour 27 minutes and 38 seconds to be exact
 #everything hurts
 #unfinished as of 16-2-26
 #finished 17-2-26
time.sleep(0.5)   
print()
if revealed_list == [True] * len(word):
    print("you won.")
else:
    print("You Lost.")
    time.sleep(0.2)
    print(f"the word was: {word}")
             
             
               
                    
            

