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
    def update_name(self,name:str):
        self.name = name              
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
    def _validate_account(self, BankAcc=None,AccountID=None):
        #dev tool? idk whats the name
        if BankAcc is not None:
            if not isinstance(BankAcc, BankAccount):
                raise TypeError("Expected BankAccount obj")
        if AccountID is not None:
            if not isinstance(AccountID,int):
                raise TypeError("Expected int")
            
    def add(self,account:BankAccount):
        self._validate_account(BankAcc=account)
        self.accountDict[self.currentID] = account
        self.currentID += 1    
    def get(self, account_id: int) -> BankAccount:
        self._validate_account(AccountID=account_id)
        acc = self.accountDict.get(account_id)
        if acc is None:
            raise KeyError("Account doesn't exist")
        else:
            return acc
    def update_name(self,account_id,new_name):
        self._validate_account(AccountID=account_id)
        if not isinstance(new_name,str):
            raise TypeError("expected str")
        try:
            currentAccount = self.accountDict[account_id]
            currentAccount.update_name(new_name)
        except KeyError:
            print(f"no account found with ID: {account_id}")
        
    def remove(self, account_id: int):
        self._validate_account(AccountID=account_id)
        if account_id not in self.accountDict:
            raise KeyError("Account not found")
        del self.accountDict[account_id]  
    def show_accounts(self):
        for account in self.accountDict.values():
            account.show()
def main():
    bank = BankManager()

    # Create test accounts
    acc1 = BankAccount("Joe", "soup", 1500)
    acc2 = BankAccount("Mary", "toast", 750.5)
    acc3 = BankAccount("Al", "beans", 100)

    print("Initial standalone account display:")
    acc1.show()
    acc2.show()
    acc3.show()

    # Add them to the manager
    bank.add(acc1)
    bank.add(acc2)
    bank.add(acc3)

    print("\nAccounts after adding to BankManager:")
    bank.show_accounts()

    # Use BankManager.get()
    first = bank.get(0)
    second = bank.get(1)
    third = bank.get(2)

    print("\nChecking balances:")
    first.check_balance("soup")
    second.check_balance("toast")
    third.check_balance("beans")

    print("\nDoing deposits and withdrawals:")
    first.deposit("soup", 250)
    first.withdraw("soup", 100)

    second.deposit("toast", 50)
    second.withdraw("toast", 25)

    third.deposit("beans", 900)
    third.withdraw("beans", 200)

    print("\nUpdating names directly on BankAccount:")
    first.update_name("Joe Schmoe")
    second.update_name("Mary M.")
    third.update_name("Al Sweigart")

    first.show()
    second.show()
    third.show()

    print("\nUpdating a name through BankManager:")
    bank.update_name(1, "Mary Updated")
    bank.get(1).show()

    print("\nRemoving account ID 2:")
    bank.remove(2)

    print("\nAccounts after removal:")
    bank.show_accounts()

    print("\nTrying to access removed account:")
    try:
        bank.get(2)
    except KeyError as e:
        print(e)

    print("\nDone")      
if __name__ == "__main__":
    main()
   
    
    
    
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
        