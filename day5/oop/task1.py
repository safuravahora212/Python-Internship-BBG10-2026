class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

# 3 alag alag car banavya
car1 = Car("Toyota", "Fortuner", 2022)
car2 = Car("Maruti", "Swift", 2020)
car3 = Car("BMW", "X5", 2024)

car1.display_info()
car2.display_info()
car3.display_info()