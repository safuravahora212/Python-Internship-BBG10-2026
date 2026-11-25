class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.area() == other.area()

# Test - different shape, same area
r1 = Rectangle(4, 5)  # area = 20
r2 = Rectangle(2, 10) # area = 20

print(r1 == r2)  # True