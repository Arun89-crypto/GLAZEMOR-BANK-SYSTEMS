from User import USER
from Employee import EMPLOYEE
from Bank import BANK
import sys


def runprgm():
    print("--------------------x--------------------")
    print('''WELCOME TO THE GLAZOMER BANK
What you want to Log In as:
(1) = User
(2) = Employee
(3) = ADMIN ACCESS
(exit) = Exit the bank
    ''')
    print("--------------------x--------------------")
    option = input("Enter your choice : ")
    if(option == "1"):
        branch = input("Enter the branch : ").replace(" ", "").lower()
        USER.get_data(branch)
    elif(option == "2"):
        EMPLOYEE.getData()
    elif(option == "3"):
        BANK.printScreen()
    elif(option == "exit"):
        print("--------------------x--------------------")
        print("THANK YOU FOR USING OUR BANK !!")
        print("--------------------x--------------------")
        sys.exit()
    else:
        print("--------------------x--------------------")
        print("Invalid Choice !!")
        print("--------------------x--------------------")
        runprgm()


if __name__ == "__main__":
    runprgm()
