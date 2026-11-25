class Inventory:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

# Test
inv = Inventory(["apple", "banana", "mango"])
print(len(inv))
print(inv[0])
print(inv[2])