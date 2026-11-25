class Stack:
    def __init__(self):
        self.__items = []  # private list

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if self.__items:
            return self.__items.pop()
        return None

    def __str__(self):
        return f"Stack: {self.__items}"

# Test
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s)

print("Popped:", s.pop())
print(s)