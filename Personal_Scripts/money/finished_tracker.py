"""Balance Tracker"""
#i messed up while writing this code.
#expenses is the money you SPEND. but my actual goal was tracking balance. expect misleading variable names
#I can predict that this code will be horrible. This is NOT a serious project.

#.strftime("%Y,%M,%D")
import datetime, sys

now = datetime.datetime.now()
now = now.strftime("%d/%m/%Y")


def store_expenses(expense) -> None:
    try:
        with open("Expenses.txt", "a") as e:
            e.write(expense)
            e.write("\n")
            e.write("\n")
    except Exception as err:
        print("error logging file.")
        print("Error: " + str(err))
        sys.exit()
    
        


while True:
    user = input("How much money do you have right now? (USD) ").strip()
    try:
        float(user)
    except ValueError:
        print("Make sure your response is a number.")
        continue
    break

    
note = input("Notes: ")

balance = f"{now}  |  ${user}  |  {note}"
store_expenses(balance)
print("logged. \n \n you may check your expenses on 'Expenses.txt'")


 



       
    

    
    
    
    
     

    
    
