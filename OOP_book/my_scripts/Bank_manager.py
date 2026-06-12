#old class, Account obj
class BankAccount:
    def __init__(self,name:str,password:str,amount: int | float):        
        if not isinstance(name,str):
            raise TypeError("name on arg 1 must be type str")
        elif len(name) > 30:
            raise ValueError("name too long.")
        if not isinstance(password,str):
            raise TypeError("password on arg 2 must be type str")
        elif len(password) > 18:
            raise ValueError("password too long.")
        if not isinstance(amount,(int,float)):
            raise ValueError("invalid type on arg 3")
            
        #I wont add any password checking stuff right now        
        #i noticed that my error messages are inconsistent, dont care
        #for a practice script.
        #wont put a limit on balance tho
        
        self.name = name
        self.balance = amount
        self.password = password.strip()
    def show(self) -> None:               
        print(f"name: {self.name}")        
    def check_balance(self,password) -> None:
        if password.strip() != self.password:
            print("Invalid password")
            return None
        print(f"Balance: {self.balance}")
    def deposit(self,password,amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be a number")
        if amount <= 0:
            print("deposit amount must not be zero or less.")
            return
        if password.strip() != self.password:
            print("Invalid password")
            return 
        print(f"depositing {amount} to {self.name}...")
        self.balance += amount
        print(f"Current balance: {self.balance}")
    def withdraw(self,password,amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be a number")
        if amount <= 0:
            print("withdraw amount must not be zero or less.")
            return
        if password.strip() != self.password:
            print("Invalid password")
            return 
        if (self.balance - amount) < 0:
            print("You cannot withdraw more money than you own.")
            return
        print(f"withdrawing {amount} from {self.name}...")
        self.balance -= amount
        print(f"Remaining balance: {self.balance}")
class BankManager():
    def __init__(self):
        self.accountDict = {}
        self.currentID = 0
    def add(self,account:BankAccount):
        if not isinstance(account, BankAccount):
            raise TypeError("method only accepts local 'BankAccount' objects.")
        else:
            self.accountDict[self.currentID] = account
    def show_accounts(self):
        for account in self.accountDict.values():
            account.show()
            
if __name__ == "__main__":
    Bank = BankManager()
    obj_bank_account = BankAccount("Joe","soup",1500)
   
    Bank.add(obj_bank_account)
    Bank.show_accounts()
    print("Done")
    #print(type(obj_bank_account).__name__)
    
    
    
    
    """class BankAccount(builtins.object)                          |  BankAccount(name: str, password: str, amount: int | float)
 |
 |  Methods defined here:
 |
 |  __init__(self, name: str, password: str
, amount: int | float)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  check_balance(self, password)
 -> None
 |
 |  deposit(self, password, amount)
 |
 |  show(self) -> None
 |
 |  withdraw(self, password, amount)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object"""
        