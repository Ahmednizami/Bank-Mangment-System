import pickle
import os
import pathlib
class Account:
    accNo = 0
    name = ''
    deposit=0
    type = ''

    def create_account(self):
        self.accNo = int(input("Enter the Account Number: "))
        self.name = input("Enter the acount holder name: ")
        self.type = input("Enter Amount Type [C/S] : ")
        self.deposit = int(input("Enter Amount to deposit: "))
        print("Congratulations! Account Open Suucesfully!")

    def show_account(self):
        print("Account Number : ",self.accNo)
        print("Account Holder Name : ", self.name)
        print("Type of Account",self.type)
        print("Balance : ",self.deposit)

    def deposit_amount(self, amount):
        self.deposit += amount

    def withdraw_amount(self,amount):
        self.deposit -= amount

    def modify_account(self):
        print("Account Number : ",self.accNo)
        self.name = input("Modify Account Holder Name :")
        self.type = input("Modify type of Account :")
        self.deposit = int(input("Modify Balance :"))

    def getAccountNo(self):
        return self.accNo
    def getAcccountHolderName(self):
        return self.name
    def getAccountType(self):
        return self.type
    def getDeposit(self):
        return self.deposit

def writeAccount():
    account = Account()
    account.create_account()
    writeAccountsFile(account)

def displayAccount():
    with open("accounts.data", "rb") as f:
        mylist = pickle.load(f)
        print("*".center(100, "*"))
        print("|".ljust(4) + "Account Number".center(15, " ") + "|".rjust(4) + "Acoount Holder Name".center(33, " ") + "|".ljust(4) +  "Account Type".center(12, " ") + "|".rjust(4) + "Total Balance".center(20, " ") + "|".rjust(4))
        print("*".center(100, "*"))
        for item in mylist:
            print("|".ljust(4) + str(item.accNo).center(15, " ") + "|".rjust(4) + item.name.center(33, " ")  + "|".ljust(4) + item.type.center(12, " ") + "|".rjust(4) + str(item.deposit).center(20, " ") + "|".rjust(4))
        print("*".center(100, "*"))

# Introduction
def intro():
    print("\t\t\t\t\t" + "*".center(35, "*"))
    print("\t\t\t\t\t" + "BANK MANAGEMENT SYSTEM".center(35, ' '))
    print("\t\t\t\t\t" + "*".center(35, "*"))
    print("\t\t\t\t\t" + "Brought To You By:")
    print("\t\t\t\t\t" + "https://www.github.com/Ahmednizami")
    print("\t\t\t\t\t" + "*".center(35, "*"))

def deposit(accNum):
    file = pathlib.Path("accounts.data")
    if file.exists():
        with open("accounts.data", "rb") as rfile:
            mylist = pickle.load(rfile)
        os.remove('accounts.data')
        for item in mylist:
            if item.accNo == accNum:
                amount = int(input("Enter the amount to deposit : "))
                item.deposit += amount
                print("Your account is updted")
    else :
        print("No records to Search")
    with open("newaccounts.data", "wb") as wfile:
        pickle.dump(mylist, wfile)
    os.rename('newaccounts.data', 'accounts.data')

def withdraw(accNum):
    file = pathlib.Path("accounts.data")
    if file.exists():
        with open("accounts.data", "rb") as rfile:
            mylist = pickle.load(rfile)
        os.remove('accounts.data')
        for item in mylist:
            if item.accNo == accNum:
                amount = int(input("Enter the amount to withdraw : "))
                if amount <= item.deposit :
                    item.deposit -=amount
                else :
                    print("You cannot withdraw larger amount")
    else :
        print("No records to Search")
    with open("newaccounts.data", "wb") as wfile:
        pickle.dump(mylist, wfile)
    os.rename('newaccounts.data', 'accounts.data')

def displaySp(accNum):
    file = pathlib.Path("accounts.data")
    if file.exists():
        with open("accounts.data", "rb") as rfile:
            mylist = pickle.load(rfile)
        found = False
        for item in mylist :
            if item.accNo == accNum:
                print("Your account Balance is = ",item.deposit)
                found = True
    else :
        print("No records to Search")
    if not found :
        print("No existing record with this number")

def deleteAccount(accNum):
    file = pathlib.Path("accounts.data")
    if file.exists():
        with open("accounts.data", "rb") as rfile:
            oldlist = pickle.load(rfile)
        newlist = []
        for item in oldlist :
            if item.accNo != accNum:
                newlist.append(item)
        os.remove('accounts.data')
    with open("newaccounts.data", "wb") as wfile:
        pickle.dump(newlist, wfile)
    os.rename('newaccounts.data', 'accounts.data')

def modifyAccount(accNum):
    file = pathlib.Path("accounts.data")
    if file.exists():
        with open("accounts.data", "rb") as rfile:
            oldlist = pickle.load(rfile)
        for item in oldlist :
            if item.accNo == accNum:
                item.name = input("Enter the account holder name : ")
                item.type = input("Enter the account Type : ")
                item.deposit = int(input("Enter the Amount : "))
        os.remove('accounts.data')
    with open("newaccounts.data", "wb") as wfile:
        pickle.dump(oldlist, wfile)
    os.rename('newaccounts.data', 'accounts.data')

def writeAccountsFile(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        with open("accounts.data", "rb") as rfile:
            oldlist = pickle.load(rfile)
            oldlist.append(account)
        os.remove('accounts.data')
    else :
        oldlist = [account]
    with open("newaccounts.data", "wb") as wfile:
        pickle.dump(oldlist, wfile)
    os.rename('newaccounts.data', 'accounts.data')

ch = 1
while ch != 8:
    os.system("cls" if os.name == 'nt' else 'clear')
    intro()
    print("\tMAIN MENU")
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. ALL ACCOUNT HOLDER LIST")
    print("\t6. CLOSE AN ACCOUNT")
    print("\t7. MODIFY AN ACCOUNT")
    print("\t8. EXIT")
    print("\tSelect Your Option (1-8) ")
    os.system("pause")
    ch = input("Enter your choice : ")
    os.system("cls" if os.name == 'nt' else 'clear')
    if ch == '1':
        writeAccount()
    elif ch =='2':
        accNo = int(input("\tEnter The account No. : "))
        deposit(accNo)
    elif ch == '3':
        accNo = int(input("\tEnter The account No. : "))
        withdraw(accNo)
    elif ch == '4':
        accNo = int(input("\tEnter The account No. : "))
        displaySp(accNo)
    elif ch == '5':
        displayAccount();
    elif ch == '6':
        accNo =int(input("\tEnter The account No. : "))
        deleteAccount(accNo)
    elif ch == '7':
        accNo = int(input("\tEnter The account No. : "))
        modifyAccount(accNo)
    elif ch == '8':
        print("\tThanks for using bank managemnt system")
        break
    else :
        print("Invalid choice")

    os.system("pause")