class Employee:
    def __init__(self, salary):
        self.__salary = salary  # double __ etle private

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Salary 0 !")

# Test karo
e = Employee(50000)
print(e.get_salary())

e.set_salary(60000)
print(e.get_salary())

e.set_salary(-100)  # aama error aavse