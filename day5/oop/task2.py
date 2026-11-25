class Counter:
    count = 0  

    def __init__(self):
        Counter.count += 1  

    @classmethod
    def get_total(cls):
        return cls.count

# 5 object 
c1 = Counter()
c2 = Counter()
c3 = Counter()
c4 = Counter()
c5 = Counter()

print("Total:", Counter.get_total())