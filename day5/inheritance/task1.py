class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def study(self):
        print(f"{self.name} is studying {self.course}")

# Test
s = Student("safa", 20, "Python")
s.study()
print(s.name, s.age, s.course)