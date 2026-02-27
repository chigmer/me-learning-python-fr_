def checkthe_score(actual_score):
     if actual_score > 100:
         print("are you einstein or something?")
     elif actual_score >=95:
        print("Nice job ")
     elif actual_score >=89:
        print ("welp, atleast you tried your best")
     else:
        print("screw you,"* 5)

scorestocheck = [1000, 99, 2, 400, 900, 70, 9, 100]

for x in scorestocheck:
    checkthe_score(x)
    print ("and", end= " ") #is it normal to fix syntax and indentation errors line by line since python is sooo picky? :/
    #i dont know if other beginners experience this (btw this is the code, rate it)