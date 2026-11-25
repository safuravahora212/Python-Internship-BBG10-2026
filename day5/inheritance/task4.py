class Bird:
    def fly(self):
        print("Bird is flying with wings")

class Airplane:
    def fly(self):
        print("Airplane is flying with engine")

class Drone:
    def fly(self):
        print("Drone is flying with propellers")

# Test 
for obj in [Bird(), Airplane(), Drone()]:
    obj.fly()