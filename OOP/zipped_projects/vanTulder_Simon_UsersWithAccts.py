
# John.make_deposit(10000).make_transfer(Sir, 1).make_withdrawal(1111)

# print(John.account_balance)
# print(Sir.account_balance)

class BankAccount:
    def __init__(self, int_rate=0.01, balance=0): # don't forget to add some default values for these parameters!
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if self.balance< amount:
            print("insufficient funds: Charging a $5 fee")
            self.balance-=5
        else:
            self.balance -= amount
        return self
    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

    def display_account_info(self):
        print("Balance {} ".format(self.balance))
        return self

# Simon_Acct = BankAccount()
# Simon_Acct.deposit(100).deposit(50).deposit(100).withdrawal(10).yield_interest().display_account_info()

# gallahad_acct = BankAccount()
# gallahad_acct.deposit(100).deposit(500).withdrawal(100).withdrawal(10).withdrawal(10).withdrawal(10).yield_interest().display_account_info()

class User:
    #User creation
    def __init__(self, name):
        self.name = name
        self.accounts = BankAccount(int_rate=0.02, balance=0)
    
    #method creation
    def make_deposit(self, amount):
        self.accounts.deposit(amount)
        return self
    #method creation
    def make_transfer(self, user2, amount):
        self.accounts.withdrawal(amount)
        user2.accounts.deposit(amount)
        return self
    #method creation    
    def make_withdrawal(self, amount):
        self.accounts.withdrawal(amount)
        return self
    def account_balance(self):
        self.accounts.display_account_info()
        return self

John = User("John Cleese")
Graham = User("Graham Chapman")
Sir = User("Sir Lance-A-Lot")

John.make_deposit(10000)
John.account_balance()
