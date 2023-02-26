#
# TestAccounts.py - Test Bank Account
#

from BankAccounts import *

bank = BankAccounts('Thi Van Anh Duong','90023112',1000,)

choice = input("Enter your transaction selection: (W/D/C/B) or X to eXit: ").upper()

while choice != "X":

    if choice == "W":
        amount = int(input("Enter amount to withdraw: "))
        try:
            bank.withdraw(amount)
            balances(bank)
        except ValueError as err:
            print(err)
    elif choice == "D":
        amount = int(input("Enter amount to deposit: "))
        bank.deposit(amount)
        balances(bank)
        
    elif choice == "C":
        bank.chargeFees()
        balances(bank)
    elif choice == "B":
        print("Your balance: ", bank.balance)
        balances(bank)
    choice = input("Enter your transaction selection: (W/D/C/B) or X to eXit: ").upper()
balances(bank)
