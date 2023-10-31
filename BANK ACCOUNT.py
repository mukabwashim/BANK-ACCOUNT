import datetime

class BankAccount:
    def __init__(self, account_number, balance, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = datetime.date.today()
        self.customer_name = customer_name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return amount
        else:
            return 0

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            return "Insufficient balance"

    def check_balance(self):
        return f"Account balance is {self.balance}"

    def customer_details(self):
        return f"Customer Name: {self.customer_name}\nAccount Number: {self.account_number}\nDate of Opening: {self.date_of_opening}\nBalance: {self.balance}"

# Example Usage
account = BankAccount("39568488", 1000, "Mukabwa Brothers")

print(account.deposit(50000))  # Output: 50000
print(account.withdraw(9800))  # Output: 9800
print(account.withdraw(15000))  # Output: "Insufficient balance"
print(account.check_balance())  # Output: "Account balance is 58000"
print(account.customer_details())  # Output: Details of the customer
