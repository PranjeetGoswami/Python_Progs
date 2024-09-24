class BankAccount:
    def _init_(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient balance.")
        elif amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance

# Example usage:
account = BankAccount(100)
account.deposit(50)
print("Balance after deposit:", account.get_balance())
account.withdraw(30)
print("Balance after withdrawal:", account.get_balance())
            