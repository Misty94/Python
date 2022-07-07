class BankAccount:
#     all_accounts = []

#     @classmethod
#     def print_all_accounts(cls):
#         for account in cls.all_accounts:
#             print()

    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
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



account_1 = BankAccount(0.01, 987.63)

account_1.deposit(205).deposit(57.29).deposit(413).withdraw(546.82).yield_interest().display_account_info()


account_2 = BankAccount(0.05, 654.17)

account_2.deposit(497.52).deposit(180).withdraw(27.99).withdraw(152.32).withdraw(90.25).withdraw(279.64).yield_interest().display_account_info()


