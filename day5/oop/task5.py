class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below -273.15")
        self._celsius = value

    @property
    def kelvin(self):
        return self._celsius + 273.15

# Test
t = Temperature(25)
print(t.celsius)  # 25
print(t.kelvin)   # 298.15

# t.celsius = -300  # This will give ValueError