class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f'Desposited amount Rs.{amount}. New balance: Rs.{self.balance}'

    def withdraw(self, amount):
        if amount <= self.balance:
            amount -= self.balance
            return f"Withdraw: Rs.{amount} Balance: Rs.{self.balance}"
        else:
            return "you don't have enough money"

    def get_balance(self):
        return f'Amount: Rs.{self.balance} Account Number: Rs.{self.account_number}'


# Child class representing a Savings Acoount, Inherting from BankAccount
class SavingsAccount(BankAccount):

    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        return f"Interest applied. New balance: rs.{self.balance}"


# Overriding the get_balance method to incude interest information
def get_balance(self):
    return f"Savings Account #{self.account_number} balance: Rs.{self.balance} with interest{self.interest_rate}"
