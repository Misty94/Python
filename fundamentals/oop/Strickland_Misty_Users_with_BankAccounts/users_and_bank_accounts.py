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


class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = BankAccount(int_rate=0.02, balance=0)

    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        print(f"Bank Account Balance: {self.account} ")

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True

    def spend_points(self, amount):
        if self.gold_card_points > amount:
            self.gold_card_points -= amount
        else:
            print("Sorry, you don't have enough points.")
    
    def make_deposit(self, amount):
        self.account.deposit(100)
        print(self.account.balance)

    def make_withdrawal(self, amount):
        self.account.withdraw()

    def display_user_balance(self):
        self.account.display_account_info()

# user_misty = User("Misty", "Strickland", "mms.strickland@gmail.com", 28)

# user_misty.display_info()


# user_misty.enroll()
# user_misty.spend_points(50)
# user_misty.enroll()

# print("**********************")

# user_harry = User("Harry", "Potter", "hp.hogwarts@gmail.com", 14)
# user_harry.enroll()
# user_harry.spend_points(80)
# user_harry.display_info()

# print("**********************")

# user_elena = User("Elena", "Gilbert", "egilbert@gmail.com", 22)
# user_elena.display_info()
# user_elena.spend_points(40)