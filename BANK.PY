from random import randint

class Bank:
    def __init__(self):
        self.account_no = randint(100000, 999999)
        self.name = input("ENTER YOUR NAME:- ")
        self.phone_no = input("ENTER YOUR PHONE NUMBER:- ")
        self.__balance = 0

    def show_info(self):
        print(f"Account Number:- {self.account_no}")
        print(f"Name:- {self.name}")
        print(f"Balance:- {self.__balance}\n")

    def deposit(self):
        amount = int(input("ENTER AN AMOUNT TO DEPOSIT:-"))
        self.__balance += amount

    def withdraw(self):
        amount = int(input("ENTER AN AMOUNT TO WITHDRAW:-"))
        if amount > self.__balance:
            print("BALANCE IS NOT SUFFICIENT")
        else:
            self.__balance -= amount

    def show_balance(self):
        print(f"CURRENT BALANCE:- {self.__balance}")

banks = []

def check_account_exist(acc_no: int):
    global banks
    for obj in banks:
        if obj.account_no == acc_no:
            return obj
    return None

while True:
    print("1. Create account")
    print("2. Show all details of account")
    print("3. Deposit Amount")
    print("4. Withdraw Amount")
    print("5. Transfer Amount")
    print("6. Exit")
    choice = int(input("Enter your choice:- "))

    if choice == 1:
        obj = Bank()
        banks.append(obj)

    if choice == 2:
        if len(banks) == 0:
            print("No account has been created")
        else:
            for account in banks:
                account.show_info()

    if choice == 3:
        if len(banks) == 0:
            print("No account have been created yet")
        else:
            acc_no = int(input("Enter your account no:- "))
            for acc in banks:
                if acc.account_no == acc_no:
                    acc.deposit()
                    break

    if choice == 4:
        if len(banks) == 0:
            print("No account has been created")
        else:
            acc_no = int(input("Enter your account no:- "))
            for acc in banks:
                if acc.account_no == acc_no:
                    acc.withdraw()
                    break

    if choice == 5:
        from_account_no = int(input("Enter an account from which you want to transfer:- "))
        to_account_no = int(input("Enter an account to which you want to transfer:- "))
        from_account = check_account_exist(from_account_no)
        to_account = check_account_exist(to_account_no)
        if from_account is not None and to_account is not None:
            transfer_amount = int(input("Enter transfer amount:- "))
            if from_account._Bank__balance < transfer_amount:
                print("Insufficient Amount")
            else:
                from_account.withdraw(transfer_amount)
                to_account.deposit(transfer_amount)
        else:
            print("One or both accounts do not exist")

    elif choice == 6:
        break

    else:
        print("INVALID CHOICE")
