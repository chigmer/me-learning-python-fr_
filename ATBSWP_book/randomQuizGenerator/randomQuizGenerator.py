# randomQuizGenerator.py - Creates quizzes with questions and answers in # random order, along with the answer key
import random 
from pathlib import Path

# The quiz data. Keys are states and values are their capitals.

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
for quiz_num in range(1,36):
    
    with open(f"Quiz_no._{quiz_num}.txt","w") as qz:
        
        #how do i fix lexicographic ordering betraying me?
        qz.write("Name:\nDate:\n\nScore:\n\n\n")
        qz.write("State Capitals quiz\n\n\n")
        states = list(capitals.keys())
        random.shuffle(states)
        #states are randomized
        for num in range(50):
# Get right and wrong answers.
            correct_answer = capitals[states[num]]
            wrong_answers = list(capitals.values())
            del wrong_answers[wrong_answers.index(correct_answer)]
            wrong_answers = random.sample(wrong_answers, 3)
            answer_options = wrong_answers + [correct_answer]
            random.shuffle(answer_options)
            qz.write(f"{num + 1}. What is the capital of {states[num]}?\n")
            qz.write(f"A. {answer_options[0]}\nB. {answer_options[1]}\nC. {answer_options[2]}\nD. {answer_options[3]}\n\n")
            with open(f'capitalsquiz_answers{quiz_num}.txt', 'a') as answer_file:
                #copy pasting this line, also, i have no idea what .index() does->>
                answer_file.write(f"{num + 1}. {'ABCD'[answer_options.index(correct_answer)]}\n")
                
            
            
            

   
        
        
      
        
        
        
        
        
        
count = 0
ans_count = 0 #both should exactly be 35     
for num in range (1,36):
    if Path(f"Quiz_no._{num}.txt").exists():
        count += 1
    if Path(f"capitalsquiz_answers{num}.txt"):
        ans_count += 1
if count == 35 and ans_count == 35:
    print("Quizzes made successfully.")
else:
    print("Error creating file!")
    #not bothering to explain why.
        
        
