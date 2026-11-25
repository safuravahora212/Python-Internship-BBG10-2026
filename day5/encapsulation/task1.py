class Wallet:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid amount")

    @property
    def balance(self):
        return self.__balance

# Test
w = Wallet()
w.deposit(1000)
w.withdraw(400)
print(w.balance)
# w.balance = 5000  error