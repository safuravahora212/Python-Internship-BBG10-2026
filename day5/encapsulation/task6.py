class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot compare different currencies")
        return self.amount < other.amount

    def __gt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot compare different currencies")
        return self.amount > other.amount

m1 = Money(100, "INR")
m2 = Money(200, "INR")
print(m1 < m2)  
print(m1 > m2)  

m3 = Money(150, "USD")
#print(m1 > m3) #valueerror  

