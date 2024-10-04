#two Python scripts: bank_account.py, which contains the BankAccount class, and main-0.py, which interfaces with the class through command line arguments to perform banking operations.

class BankAccount:
    def __init__(self, initial_balance):
        self.__account_balance = initial_balance

    def deposit(self, amount):
        #Add amount ot account balance
        if amount > 0:
            self.__account_balance += amount

    
    def withdraw(self, amount):
        #check if available funds are sufficient to withdraw
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        #display current balance
        print(f"Current Balance: ${self.__account_balance:.2f}")
