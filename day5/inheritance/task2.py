class Employee:
    def calculate_salary(self):
        return 30000

class Developer(Employee):
    def calculate_salary(self):
        return super().calculate_salary() + 10000

class Designer(Employee):
    def calculate_salary(self):
        return super().calculate_salary() + 5000

# Test
print("Developer:", Developer().calculate_salary())
print("Designer:", Designer().calculate_salary())