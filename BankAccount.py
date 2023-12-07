class BankAccount:
    
    

    def __init__(self, int_rate = 0.03, balance = 0.0): 
        self.int_rate = int_rate
        self.balance = balance
        
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
        
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: charging a $5 fee")
            self.balance = self.balance - 5
            return self
        else:
            self.balance = self.balance - amount
            return self
        
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            return self
        
    @classmethod
    def all_accounts_info(cls):
        all_accounts = []
        for account in BankAccount:
            all_accounts.append(BankAccount(account))
        return all_accounts

Accoutn1 = BankAccount()
Account2 = BankAccount(0.49,132871.42)

Accoutn1.deposit(2541.32).deposit(681.28).deposit(12).withdraw(3350).yield_interest().display_account_info()
Account2.deposit(23164.18).deposit(7649.33).withdraw(641.23).withdraw(142.99).withdraw(99224.06).withdraw(0.42).yield_interest().display_account_info()

print(BankAccount.all_accounts_info)