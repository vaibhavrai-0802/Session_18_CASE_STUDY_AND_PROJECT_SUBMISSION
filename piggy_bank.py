import os

class piggy_bank():
    def __init__(self):
        "initialise variables"
        self.account_balance = 0
        print ('-'*15,'Start','-'*15)
        self.main_func()
        
    def main_func(self):
        option = input('Start or End :')
        if option == "Start":
            self.usage_func()
        else:
            os._exit(1)
    def usage_func(self):
        usage = input('Add(A), Withdraw(W) or Check(C) : ')
        if usage == 'Add' or usage == 'A':
            self.deposit()
        elif usage == 'Withdraw' or usage == 'W':
            self.withdraw()
        elif usage == 'Check' or usage == 'C':
            self.check_balance()
        elif usage == 'exit':
            os._exit(1)
        else:
            print("Wrong input, please provide appropriate input or type exit")
            self.usage_func()
    def withdraw(self):
        "function to check withdrawals"
        withdrawal=input('withdraw amount : ')
        self.account_balance = self.account_balance - int(withdrawal)
        print ("After withdrawing, balance amount is %.2f rupees" %self.account_balance)
        self.main_func()
        
    def deposit(self):
        "function to calculate deposits"
        deposit=input('Add amount : ')
        self.account_balance = self.account_balance + int(deposit)
        print ("After adding, your updated balance is %.2f rupees" %self.account_balance)
        self.main_func()
        
    def check_balance(self):
        "function to check account balance"
        print("Your current balance is %.2f rupees" %self.account_balance)
        self.main_func()