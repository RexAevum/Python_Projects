class Account:
    """ This class creates a banking account and allows user to perform transactions on it"""
    def __init__(self, balancePath):
        self.path = balancePath
        with open(self.path, 'r') as file:
            self.balance = int(file.read())
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
            
    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.path, 'w') as file:
            # when writing to a text file, the type has to be str or has to be cast as str
            file.write(str(self.balance))
    


""" Inheritance """
# When creating a class need to pass the class which you are inhereting from as a parameter
class Checking(Account):
    """ This class creates a checking account """
    # And to init the Checking class we init the super class in the __init__ function fof the inhereting class
    # by calling the __init__ method of the super class
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fees = fee
    
    # Once inherited from super class, can add variables and functions to the inheriting class
    def transfer (self, amount):
        self.balance = self.balance - amount - self.fees


""" Output validation """
check = Checking("simple_balance.txt", 3)
check.deposit(100)
check.commit()
check.transfer(500)
check.commit()
print(check.balance)
print(check.__doc__) # This will return whatever is written right after the class naming and it returns whateve is in the tripple quotes

##### For Account class #####

#account = Account("simple_balance.txt")
#account.withdraw(150)
#account.commit()
#account.deposit(100)
#account.commit()
#print(account.balance)
