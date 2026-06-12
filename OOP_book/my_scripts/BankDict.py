from bank_simulator_1 import BankAccount
import random,hashlib
def gen_fingerprint(entry):
    #feels a little redundant. 
    return hashlib.md5(entry.encode()).hexdigest()[:6]
def main():
    myBank = {}
    #test Data
    names = ["Joe Schmoe", "Mary M.", "Al Sweigart"]
    balance= [random.randint(500,1000) for _ in range(3)]
    for i in range(3):
        current_Acc = BankAccount(names[i],"password",balance[i])
        myBank[gen_fingerprint(f"{names[i]}")] = current_Acc
    print(f"Total Accounts: {len(myBank)}") 
    print()
    print("Pick from any ID's listed below.\n\nevery account password is \"password\"\n('q' to quit)\n\n")
    for i in myBank:
        print(i,"\n")
    
    while True:
        #letting the user check accounts                
        user = input(">").strip()
        if user == "q" or user == "Q":
            break
        elif not user in myBank.keys():
            print(f"No account found with ID: \"{user}\"")
            continue
        BankAcc = myBank[user] 
        print("Actions:\n\nD–deposit\nW–withdraw\nB-Check Balance\nQ-quit\n\n")       
        while True:
            user = input(">").strip()
            if user == "D":
                D_password = input("password>")
                try:
                    D_amount = float(input("amount>"))
                except Exception:
                    print("not a number")
                    continue
                
                BankAcc.deposit(D_password,D_amount)
            elif user == "W":
                W_password = input("password>")
                try:
                    W_amount = float(input("amount>"))
                except Exception:
                    print("not a number")
                    continue
                BankAcc.withdraw(W_password,W_amount)
            elif user == "B":
                B_password = input("password>")
                BankAcc.show()
                BankAcc.check_balance(B_password)
            elif user == "Q":
                break
                
                
                
            
        
     
            
        
        
        
if __name__ == "__main__":
    main()     
    print("\nVery clunky right now, will improve it I promise")        
