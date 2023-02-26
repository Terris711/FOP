#
# BankAccounts.py - Bank Account Calculation
#

class BankAccounts():
    fees = 5
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number 
        self.balance = balance

    def withdraw(self, amount):
        #amount = int(input("Enter amount to withdraw: "))

        if amount <= self.balance:
            self.balance -= amount
            print("Current balance is: ", self.balance)
        else:
            raise ValueError("Your amount dont have enough money!")


    def deposit(self, amount):
        self.balance += amount

    def chargeFees(self):
        self.balance = self.balance - self.fees

def balances(account):
    total = 0 
    print("Name:", account.name,"\tNumber: ", account.number, "\tBalance: ", account.balance)
    total = total + account.balance
    print("\t\t\t\tTotal: ", total)



