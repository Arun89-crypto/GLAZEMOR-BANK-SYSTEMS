# Glazemor Banking System
This is a banking system made with python and uses csv files to store data and pandas module to perform CRUD in csv files
<p>
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>
</p>

## How to use:
* First navigate to the folder and write the following command in terminal
```ssh
python3 main.py
```
Output:
```ssh
--------------------x--------------------
WELCOME TO THE GLAZOMER BANK
What you want to Log In as:
(1) = User
(2) = Employee
(3) = ADMIN ACCESS
(exit) = Exit the bank
    
--------------------x--------------------
Enter your choice : 
```
* Enter your desired choice you will get output according to the options
* Now to access special features you have to use keys listed below:
```ssh
EMPLOYEE_UNIVERSAL_PASSWORD = GLAZEMOR_EMP_123123
BANK_KEY = GLAZEMOR_456456
```

## Features
### USER
```ssh
--------------------x--------------------
WELCOME TO THE GLAZOMER BANK - USER NAME
--------------------x--------------------
Enter your choice from the below options :
(1) = Check Account Balance
(2) = Deposit Money
(3) = Withdraw Money
(4) = Print info statement
(5) = Apply Loan
(6) = Pay Loan Installment
(exit) = Exit

Enter your choice : 
```

### EMPLOYEE
```ssh
--------------------x--------------------
WELCOME TO THE GLAZOMER BANK - EMPLOYEE_ID
--------------------x--------------------
Enter your choice from the below options :
(1) = Delete Account on request
(2) = Create an Account
(exit) = Exit
        
Your Choice : 
```

### BANK
```ssh
--------------------x--------------------
 WELCOME TO GLAZEMOR BANK
choose your option
(1) = Reset Branch
(2) = Add Branch
(3) = Total Cash in Bank
(exit) = Exit
        
--------------------x--------------------
Enter your choice : 
```

## Data Format
```ssh
for a Branch containing users
|--------------|-------------|---------|-----------------------|-----------|-------------|------------|----------|
| name         | bankId      | cash    | email                 | pinNumber | loanApplied | loanAmount | branch   |
|--------------|-------------|---------|-----------------------|-----------|-------------|------------|----------|
| Arun Jangra  | 45671234001 | 207930  | arunjngra89@gmail.com | 3412      | False       | 0          | New York |
|--------------|-------------|---------|-----------------------|-----------|-------------|------------|----------|
| Vicky Jangra | 45671234003 | 1858705 | vickyvick@gmail.com   | 3456      | False       | 0          | New York |
|--------------|-------------|---------|-----------------------|-----------|-------------|------------|----------|
```
