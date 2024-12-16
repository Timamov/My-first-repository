import dotenv
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def info(self):
        information = f'brand: {self.brand}, model: {self.model}'
        return information
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors
    def info(self):
        super().info()
        information = f'brand: {self.brand}, model: {self.model}, count of doors: {self.num_doors}'
        return information
class Bike(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model)
        self.type = type
    def info(self):
        super().info()
        information = f'brand: {self.brand}, model: {self.model}, type: {self.type}'
        return information
class Truck(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity
    def info(self):
        super().info()
        information = f'brand: {self.brand}, model: {self.model}, capacity: {self.capacity}'
        return information

car1 = Car('Hyundai', 'Accent', 5)
car2 =  Car('Opel', 'Zafira', 7)
car3 = Car('Smart', 'Fortwo', 3)

print(car1.info())
print(car2.info())
print(car3.info())

bike1 = Bike('Azimute', 'kid0151', 'for town')
bike2 = Bike('MAXXPRO', 'profi10876', 'for mountains')
bike3 = Bike('Xiaomi', 'Mi Electrobike 3 pro', 'for town')

print(bike1.info())
print(bike2.info())
print(bike3.info())

truck1 = Truck('DAF', 'XF', '8 tonns')
truck2 = Truck('MAN', '0151', '24 tonns')
truck3 = Truck('Sitrack', '25', '78 tonns')

print(truck1.info())
print(truck2.info())
print(truck3.info())
