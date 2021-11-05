import pandas as pd
import sys


class EMPLOYEE():

    employeeObj = None

    def __init__(self, name: str, employeeId: str, branch: str):
        self.name = name
        self.employeeId = employeeId
        self.branch = branch

    def getData():
        items = pd.read_csv('./database/employee.csv')
        EMPLOYEE.get_user_data(items)

    def get_user_data(items):
        employee_id = EMPLOYEE.Auth_BankID(items)
        if(employee_id == "NoUser"):
            print("Your Employee ID is invalid !!")
            EMPLOYEE.get_user_data(items)
        else:
            for x in items.itertuples():
                if(x[2] == employee_id):
                    EMPLOYEE.employeeObj = EMPLOYEE(
                        name=x.name,
                        employeeId=employee_id,
                        branch=x.branch
                    )
                    break
        print("--------------------x--------------------")
        print(f"NAME : {EMPLOYEE.employeeObj.name}")
        print(f"EMPLOYEE_ID : {EMPLOYEE.employeeObj.employeeId}")
        print(f"BRANCH : {EMPLOYEE.employeeObj.branch}")
        print("--------------------x--------------------")
        print("--------------------x--------------------")
        print(
            f"WELCOME TO THE GLAZOMER BANK - {EMPLOYEE.employeeObj.employeeId}")
        print("--------------------x--------------------")
        EMPLOYEE.printScreen()

    def Auth_BankID(items):
        empID = input("Enter your employee ID : ")
        flag = False
        for x in items.itertuples():
            if(x[2] == empID):
                flag = True
                password = input("Enter your universal password number : ")
                if(password == "GLAZEMOR_EMP_123123"):
                    return empID
                else:
                    print("Wrong password !!")
                    EMPLOYEE.Auth_BankID(items)
        if(flag == False):
            return "NoUser"

    def printScreen():
        print('''Enter your choice from the below options :
(1) = Delete Account on request
(2) = Create an Account
(exit) = Exit
        ''')
        user = input("Your Choice : ")
        if user == "1":
            EMPLOYEE.deleteAccount()
        elif user == "2":
            EMPLOYEE.CreateAccount()
        elif user == "exit":
            print("--------------------x--------------------")
            print("THANK YOU FOR USING OUR BANK !!")
            print("--------------------x--------------------")
            sys.exit()

    def deleteAccount():
        branch = input("Enter the branch of user : ").replace(" ", "").lower()
        items = pd.read_csv(f"./database/{branch}.csv")
        bankId = int(input("Enter the bankId of the user : "))
        print(type(bankId))
        if(bankId in items.values):
            for x in items.values:
                print(x)
            items.drop(
                items.index[(items["bankId"] == bankId)], axis=0, inplace=True)
            items.to_csv(f"./database/{branch}.csv", index=False)
            print("updating..........")
            print("--------------------x--------------------")
            print(f"Bank Account {bankId} deleted successfully !!")
            print("--------------------x--------------------")
            EMPLOYEE.printScreen()
        else:
            print("--------------------x--------------------")
            print(f"Bank Account doesn't exists in branch : {branch} !!")
            print("--------------------x--------------------")
            EMPLOYEE.printScreen()

    def CreateAccount():
        branch = input("Enter the branch preference of user : ").replace(
            " ", "").lower()
        EMPLOYEE.__getBankID(branch)
        data_branch = pd.read_csv(f"./database/{branch}.csv")
        name = input("Enter your name : ")
        bankId = int(input("Enter the bank ID : "))
        email = input("Enter your E-mail : ")
        if(EMPLOYEE.__emailInput(email)):
            pinNumber = int(input("What pin number you want to set : "))
            if(pinNumber in data_branch):
                print("--------------------x--------------------")
                print("PIN already taken, Choose another one!!")
                print("--------------------x--------------------")
                EMPLOYEE.CreateAccount()
            else:
                amount = int(
                    input("How much amount you want to deposit in your bank : "))
                data = pd.DataFrame(
                    {
                        'name': [name],
                        'bankId': [bankId],
                        'cash': [amount],
                        'email': [email],
                        'pinNumber': [pinNumber],
                        'loanApplied': [False],
                        'loanAmount': [0],
                        'branch': [branch]
                    }
                )
                print(f"---{branch}---")
                data.to_csv(
                    f"./database/{branch}.csv", mode='a', index=False, header=False)
                print("--------------------x--------------------")
                print("Account Created Successfully :) !!")
                print("--------------------x--------------------")
                EMPLOYEE.printScreen()
        else:
            print("--------------------x--------------------")
            print("Entered Email is incorrect !! Please enter a valid one next time.")
            print("--------------------x--------------------")
            EMPLOYEE.CreateAccount()

    def __getBankID(branch):
        data_branch = pd.read_csv(
            f"./database/{branch}.csv", usecols=['bankId'])
        print(data_branch)

    def __emailInput(email: str):
        if email.__contains__("@"):
            return True
        else:
            return False
