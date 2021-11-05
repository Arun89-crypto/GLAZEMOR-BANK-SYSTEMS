import pandas as pd
import sys
from Bank import BANK


class USER:

    userdefined = None
    temp_bank_id = ""
    temp_branch = ""
    temp_cash = 0
    univ_id = 0
    name_user = ""

    def __init__(self, name: str, bankId: int, cash: int, email: str, pinNumber: int, loanApplied: str, loanAmount: int, branch: str):
        self.name = name
        self.bankId = bankId
        self.cash = cash
        self.email = email
        self.pinNumber = pinNumber
        self.loanApplied = loanApplied
        self.loanAmount = loanAmount
        self.branch = branch

    def printScreen():
        print("--------------------x--------------------")
        print(f"WELCOME TO THE GLAZOMER BANK - {USER.name_user}")
        print("--------------------x--------------------")
        print('''Enter your choice from the below options :
(1) = Check Account Balance
(2) = Deposit Money
(3) = Withdraw Money
(4) = Print info statement
(5) = Apply Loan
(6) = Pay Loan Installment
(exit) = Exit
        ''')
        option = input("Enter your choice : ")
        if(option == '1'):
            USER.userdefined.check_amount()
        elif(option == '2'):
            USER.userdefined.deposit_amount()
        elif(option == '3'):
            USER.userdefined.withdraw_amount()
        elif(option == '4'):
            USER.userdefined.print_statement()
        elif(option == '5'):
            USER.userdefined.applyLoan()
        elif(option == '6'):
            USER.userdefined.payLoan()
        elif(option == 'exit'):
            print("--------------------x--------------------")
            print("THANK YOU FOR USING OUR BANK !!")
            print("--------------------x--------------------")
            sys.exit()
        else:
            print("Invalid choice")

    def get_data(branch):
        try:
            items = pd.read_csv(f"./database/{branch}.csv")
            # print(items)
            USER.temp_branch = branch
            USER.get_user_data(items)
        except Exception as e:
            print("Branch doesn't exists contact the bank!!")
            branch_new = input("Enter some other branch : ")
            USER.get_data(branch_new)
            print(e)

    def get_user_data(items):
        if USER.temp_bank_id != "":
            bank_id = USER.temp_bank_id
        else:
            bank_id = USER.Authorize(items)
            if(bank_id == "NoUser"):
                print("Your bank ID is invalid !!")
                USER.get_user_data(items)
            else:
                USER.temp_bank_id = bank_id
                for x in items.itertuples():
                    if(str(x[2]) == bank_id):
                        USER.userdefined = USER(
                            name=x.name,
                            bankId=bank_id,
                            cash=x.cash,
                            email=x.email,
                            pinNumber=x.pinNumber,
                            loanApplied=x.loanApplied,
                            loanAmount=x.loanAmount,
                            branch=x.branch
                        )
                        USER.name_user = x.name
                USER.printScreen()

    def deposit_amount(self):
        amount = int(input("Enter the amount to deposit : "))
        self.cash += amount
        USER.temp_cash = self.cash
        BANK.get_total_cash()
        amount_str = str(int(BANK.totalCash) + amount)
        BANK.update_cash(amount_str)
        USER.__amount_update()
        print("--------------------x--------------------")
        print("Amount deposited successfully!!, THANK YOU")
        print("--------------------x--------------------")
        USER.printScreen()

    def withdraw_amount(self):
        amount = int(input("Enter the amount to withdraw : "))
        if(amount > self.cash):
            print("--------------------x--------------------")
            print("You don't have sufficient amount in your bank !!")
            print("--------------------x--------------------")
        else:
            self.cash -= amount
            USER.temp_cash = self.cash
            USER.__amount_update()
            BANK.get_total_cash()
            amount_str = str(int(BANK.totalCash) - amount)
            BANK.update_cash(amount_str)
            print("--------------------x--------------------")
            print("Amount withdrawn successfully!!, THANK YOU")
            print("--------------------x--------------------")
            USER.printScreen()

    def check_amount(self):
        if(self.cash > 100):
            print("--------------------x--------------------")
            print(f"you have ${self.cash} in your bank account")
            print("--------------------x--------------------")
        else:
            print("--------------------x--------------------")
            print(
                f"you have ${self.cash} in your bank account, please deposit ASAP otherwise your account will be blocked !!")
            print("--------------------x--------------------")
        USER.printScreen()

    def Authorize(items):
        bank_id = input("Enter your bank ID : ")
        flag = False
        for x in items.itertuples():
            if(str(x[2]) == bank_id):
                flag = True
                password = int(input("Enter your bank pin number : "))
                if(password in items.values):
                    return bank_id
                else:
                    print("Wrong pin number !!")
                    USER.Authorize(items)
        if(flag == False):
            return "NoUser"

    def print_statement(self):
        print("--------------------x--------------------")
        print(f"NAME : {self.name}")
        print(f"BANK_ID : {self.bankId}")
        print(f"CASH : ${self.cash}")
        print(f"EMAIL : {self.email}")
        print(f"Loan Applied : {self.loanApplied}")
        if(self.loanApplied == True):
            print(f"LOAN AMOUNT : {self.loanAmount}")
        print(f"BRANCH : {self.branch}")
        print("--------------------x--------------------")
        USER.printScreen()

    def __amount_update():
        items = pd.read_csv(f"./database/{USER.temp_branch}.csv")
        id_item = items.index[items['bankId']
                              == int(USER.temp_bank_id)].tolist()
        USER.univ_id = id_item[0]
        items.loc[id_item[0], 'cash'] = USER.temp_cash
        items.to_csv(f"./database/{USER.temp_branch}.csv", index=False)
        print("UPDATING..........")
        USER.temp_cash = 0

    def applyLoan(self):
        amount_to_apply = int(input("Enter your Loan Amount : "))
        items = pd.read_csv(f"./database/{USER.temp_branch}.csv")
        id_item = items.index[items['bankId']
                              == int(USER.temp_bank_id)].tolist()
        USER.univ_id = id_item[0]
        if(items.loc[id_item[0], 'loanApplied'] == True):
            print("--------------------x--------------------")
            print(
                "LOAN ALREADY APPLIED, first pay the first one please in order to apply for a new one!!")
            print("--------------------x--------------------")
            USER.printScreen()
        else:
            items.loc[id_item[0], 'loanApplied'] = True
            USER.userdefined.loanApplied = True
            items.loc[id_item[0], 'loanAmount'] = amount_to_apply
            USER.userdefined.loanAmount = amount_to_apply
            items.to_csv(f"./database/{USER.temp_branch}.csv", index=False)
            print("UPDATING..........")
            print("--------------------x--------------------")
            print("LOAN APPLIED SUCCESSFULLY !!")
            print("--------------------x--------------------")
            USER.printScreen()

    def payLoan(self):
        items = pd.read_csv(f"./database/{USER.temp_branch}.csv")
        id_item = items.index[items['bankId']
                              == int(USER.temp_bank_id)].tolist()
        USER.univ_id = id_item[0]
        if(items.loc[id_item[0], 'loanApplied'] == False):
            print("--------------------x--------------------")
            print("LOAN NOT APPLIED !!!")
            print("--------------------x--------------------")
        else:
            loan_installment = int(
                input("enter the installment you want to pay : "))
            USER.userdefined.loanAmount -= loan_installment
            if(USER.userdefined.loanAmount == 0):
                items.loc[id_item[0], 'loanApplied'] = False
                items.loc[id_item[0], 'loanAmount'] = 0
                items.to_csv(f"./database/{USER.temp_branch}.csv", index=False)
                print("--------------------x--------------------")
                print("LOAN PAYMENT SUCCESSFULLY !!!")
                print("--------------------x--------------------")
                USER.printScreen()
            else:
                items.loc[id_item[0],
                          'loanAmount'] = USER.userdefined.loanAmount
                items.to_csv(f"./database/{USER.temp_branch}.csv", index=False)
                print("--------------------x--------------------")
                print("LOAN PAYMENT SUCCESSFUL!!!")
                print("--------------------x--------------------")
                USER.printScreen()
