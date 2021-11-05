import pandas as pd
from pathlib import Path
import csv
import os
import sys


class BANK:
    data = []
    totalCash = 0

    def printScreen():
        print("--------------------x--------------------")
        print(''' WELCOME TO GLAZEMOR BANK
choose your option
(1) = Reset Branch
(2) = Add Branch
(3) = Total Cash in Bank
(exit) = Exit
        ''')
        print("--------------------x--------------------")
        choice = input("Enter your choice : ")
        if(choice == "1"):
            BANK.resetBranch()
        elif(choice == "2"):
            BANK.addBranch()
        elif(choice == "3"):
            BANK.totalCashInBank()
        elif(choice == "exit"):
            print("--------------------x--------------------")
            print("THANK YOU FOR USING OUR BANK !!")
            print("--------------------x--------------------")
            sys.exit()
        else:
            print("INVALID CHOICE !!!")
            BANK.printScreen()

    @classmethod
    def get_total_cash(cls):
        with open('./database/totalcash.txt', 'r') as f:
            data = f.readline()
            BANK.totalCash = data

    def update_cash(cash):
        with open('./database/totalcash.txt', 'w') as f:
            f.write(cash)
        with open('./database/totalcash.txt', 'r') as f:
            data = f.readline()
            BANK.totalCash = data

    @classmethod
    def getDataFromServer(cls, name):
        items = pd.read_csv(f"./database/{name}.csv")
        BANK.data = items

    @classmethod
    def resetBranch(cls):
        if(BANK.__Authorize()):
            name = input("Enter the branch you want to reset : ")
            os.remove(f"./database/{name}.csv")
            header = ['name', 'bankId', 'cash', 'email',
                      'pinNumber', 'loanApplied', 'loanAmount', 'branch']
            with open(f"./database/{name}.csv", 'w') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                f.close()
            print("--------------------x--------------------")
            print(f"{name.upper()} RESETED SUCCESSFULLY !!")
            print("--------------------x--------------------")
            BANK.printScreen()
        else:
            print("--------------------x--------------------")
            print("NOT AUTHORIZED !!!")
            print("--------------------x--------------------")
            BANK.printScreen()

    def addBranch():
        if(BANK.__Authorize()):
            branch = input("Enter the branch to create : ").replace(
                " ", "").lower()
            if Path(f"./database/{branch}.csv").exists():
                print("--------------------x--------------------")
                print("Branch Already Exists !!")
                print("--------------------x--------------------")
                BANK.printScreen()
            else:
                header = ['name', 'bankId', 'cash', 'email',
                          'pinNumber', 'loanApplied', 'loanAmount', 'branch']
                with open(f"./database/{branch}.csv", 'w') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    f.close()
                print("--------------------x--------------------")
                print(f"{branch.upper()} CREATED SUCCESSFULLY !!")
                print("--------------------x--------------------")
                BANK.printScreen()
        else:
            print("--------------------x--------------------")
            print("NOT AUTHORIZED !!!")
            print("--------------------x--------------------")
            BANK.printScreen()

    def totalCashInBank():
        if(BANK.__Authorize()):
            print("--------------------x--------------------")
            BANK.get_total_cash()
            print(f"The total cash in Bank is ${BANK.totalCash}")
            print("--------------------x--------------------")
            BANK.printScreen()
        else:
            print("--------------------x--------------------")
            print("NOT AUTHORIZED !!!")
            print("--------------------x--------------------")
            BANK.printScreen()

    def __Authorize():
        key = input("Input the special key : ")
        if key == "GLAZEMOR_456456":
            return True
        else:
            return False
