#
# banking.py
#

from accounts import *

accounts = []

bank = BankAccount('Everyday', '007', 2000)
accounts.append(bank)
bank = BankAccount('Cheque A/C', '008', 3000)
accounts.append(bank)
bank = BankAccount('Term Doposit', '009', 20000)
accounts.append(bank)

choice = input("Enter your transaction selection: (W/D/I/B) or X to eXit: ")

while choice.upper() != "X":
   
    if choice.upper() == "W":
        achoice = int(input("Choose an account from 0 to " + str(len(accounts)-1) + ": "))
        amount = int(input("Enter amount to withdraw: "))
        accounts[achoice].withdraw(amount)
        balances(accounts)
    elif choice.upper() == "D":
        achoice = int(input("Choose an account from 0 to " + str(len(accounts)-1) + ": "))
        amount = int(input("Enter amount to deposit: "))
        accounts[achoice].deposit(amount)
        balances(accounts)
    elif choice.upper() == "I":
        achoice = int(input("Choose an account from 0 to " + str(len(accounts)-1) + ": "))
        accounts[achoice].add_interest()
        balances(accounts)
    elif choice.upper() == "B":
        achoice = int(input("Choose an account from 0 to " + str(len(accounts)-1) + ": "))
        print("Your Balance: ", account[achoice].balance)
        balances(accounts)
    else:
        print("Please choose a valid transaction !")
    
    choice = input("Enter your transaction selection: (W/D/I/B) or X to eXit: ")

balances(accounts)
