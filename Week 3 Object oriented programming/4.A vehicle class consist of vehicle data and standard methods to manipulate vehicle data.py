class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    def fare(self):
        return self.capacity * 110
n=input("Enter name of the vehicle:")
c=int(input("Enter capacity of vehicle:"))
m=int(input("Enter mileage of the vehicle:"))
School_bus = Bus(n,m,c)
print("Total Bus fare is:", School_bus.fare())