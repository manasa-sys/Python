bankAccount = []
accountNumber = 9999
delNumbers = []


def menu():
    print("1.	Add a bank account.")
    print("2.	Remove a bank account.")
    print("3.	Display the information by account number")
    print("4.	Apply a deposit by account number")
    print("5.	Apply a withdrawal by account number")
    print("6.	Sort and display the list of clients")
    print("7.	Display the average balance value of the accounts.")
    print("8.	Display the total balance value of the accounts.")
    print("9.	Exit the application.")


def addAccount():

    Account = []
    global accountNumber

    if delNumbers:
        accountNumber = delNumbers[0] - 1
        del delNumbers[0]
    if len(bankAccount) == 100:
        print("Full")

    if len(bankAccount) != 100 and accountNumber < 10099:
        accountNumber = accountNumber + 1
        firstname = input("Please enter your first name\n")
        lastname = input("Please enter your last name\n")
        balance = 0
        Account.append(accountNumber)
        Account.append(firstname)
        Account.append(lastname)
        Account.append(balance)
        bankAccount.append(Account)
        print("Successfully added, your account number is ", accountNumber, "\n")

def removeAccount():

    global delNumbers
    _accountNumber = input("Please enter the account number you want to remove.\n")
    while True:
        if _accountNumber.isdigit() == True :
            _accountNumber = int(_accountNumber)
            break
        _accountNumber = input("You entered a wrong number, please enter the account number you want to remove. \n")
    flag = True
    for i in range(len(bankAccount)):
        if (_accountNumber == bankAccount[i][0]):
            del bankAccount[i]
            print("Account " , _accountNumber , " is deleted\n")
            delNumbers.append(_accountNumber)
            flag = True
            break
        else:
            flag = False
    if (flag == False):
        print("The account number you entered does not exist\n")

def display_by_account_number():
    _accountNumber = input("Please enter the account number you want to display.\n")
    while True:
        if _accountNumber.isdigit() == True :
            _accountNumber = int(_accountNumber);
            break
        _accountNumber = input("You entered a wrong number, please enter the account number you want to display. \n")
    flag = True
    for i in range(len(bankAccount)):
        if (_accountNumber == bankAccount[i][0]):
            print(bankAccount[i])
            flag = True
            break
        else:
            flag = False
    if (flag == False):
        print("The account number you entered does not exist\n")

def deposit_by_account_number():
    _accountNumber = input("Please enter the account number you want to deposit.\n")
    while True:
        if _accountNumber.isdigit() == True :
            _accountNumber = int(_accountNumber);
            break
        _accountNumber = input("You entered a wrong number, please enter the account number you want to deposit. \n")
    flag = True
    for i in range(len(bankAccount)):
        if (_accountNumber == bankAccount[i][0]):
            deposit = input("How much you want to deposit.\n")
            bankAccount[i][3] = bankAccount[i][3] + int(deposit)
            print("Deposit $" , deposit , " into account " , _accountNumber , "\n")
            flag = True
            break
        else:
            flag = False
    if (flag == False):
        print("The account number you entered does not exist\n")

def withdraw_by_account_number():
    _accountNumber = input("Please enter the account number you want to withdraw.\n")
    while True:
        if _accountNumber.isdigit() == True :
            _accountNumber = int(_accountNumber);
            break
        _accountNumber = input("You entered a wrong number, please enter the account number you want to withdraw. \n")
    flag = True
    for i in range(len(bankAccount)):
        if (_accountNumber == bankAccount[i][0]):
            withdraw = input("How much you want to withdraw.\n")
            if (int(withdraw) <= bankAccount[i][3]):
                bankAccount[i][3] = bankAccount[i][3] - int(withdraw)
                print("Your balance is  $" , withdraw , "\n")
                flag = True
                break
            else:
                print("Your balance is insufficient.\n")
                flag = True
                break
        else:
            flag = False
    if (flag == False):
        print("The account number you entered does not exist\n")

def sort():

    print("\naccounr number - ascending")
    print(sorted(bankAccount, key = (lambda x:x[0])))
    print("\naccounr number - descending")
    print(sorted(bankAccount, key = (lambda x:x[0]), reverse = True))

    print("\nfirstname - ascending")
    print(sorted(bankAccount, key = (lambda x:x[1])))
    print("\nfirstname - descending")
    print(sorted(bankAccount, key = (lambda x:x[1]), reverse = True))

    print("\nlastname - ascending")
    print(sorted(bankAccount, key = (lambda x:x[2])))
    print("\nlastname - descending")
    print(sorted(bankAccount, key = (lambda x:x[2]), reverse = True))

    print("\nbalance - ascending")
    print(sorted(bankAccount, key = (lambda x:x[3])))
    print("\nbalance - descending")
    print(sorted(bankAccount, key = (lambda x:x[3]), reverse = True))

    # sorted(bankAccount, key = itemgetter(0))  from operator import itemgetter


def average():
    sum = 0
    for i in range(len(bankAccount)):
        sum = sum + bankAccount[i][3]
    avg = sum / len(bankAccount)
    print(avg)

def total():
    sum = 0
    for i in range(len(bankAccount)):
        sum = sum + bankAccount[i][3]
    print(sum)

option = 0
while(option != "9"):
    menu()
    option = input("Please enter your option:\n")
    if (option == "1"):
        addAccount()
    if (option == "2"):
        removeAccount()
    if (option == "3"):
        display_by_account_number()
    if (option == "4"):
        deposit_by_account_number()
    if (option == "5"):
        withdraw_by_account_number()
    if (option == "6"):
        sort()
    if (option == "7"):
        average()
    if (option == "8"):
        total()
    if (option == "9"):
        print("bye")



