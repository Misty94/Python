class BankAccount:

    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

# account_1 = BankAccount(0.01, 987.63)

# account_1.deposit(205).deposit(57.29).deposit(413).withdraw(546.82).yield_interest().display_account_info()

# account_2 = BankAccount(0.05, 654.17)

# account_2.deposit(497.52).deposit(180).withdraw(27.99).withdraw(152.32).withdraw(90.25).withdraw(279.64).yield_interest().display_account_info()

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.account = BankAccount(int_rate=0.02, balance=0)

    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.balance)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(self.account.balance)

    def display_user_balance(self):
        self.account.display_account_info()

user_misty = User("Misty", "Strickland", "mms.strickland@gmail.com", 28)
user_misty.make_deposit(100)
user_misty.make_withdrawal(27.99)
user_misty.display_user_balance()

