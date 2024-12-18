class Car:
    def __init__(self, year: int, producer, brand, fuel_consumption: float):
        self.year = year
        self.producer = producer
        self.brand = brand
        self.mileage = 0
        self.fuel_consumption = fuel_consumption
    def drive(self):
       hello_text = f'I`m {self.brand} car, I`m going to owner`s affairs'
       return hello_text
    @property
    def cost_of_service(self):
        formula = self.mileage * 7.6
        return formula

camry = Car(2024, 'Japan', 'Toyota', 2.2)
touareg = Car(2015, 'Germany', 'Volkswagen', 5.45)
octavia = Car(2009, 'Czech Republic', 'Škoda', 3.1)

octavia.mileage = 30000

print(octavia.cost_of_service)

print(touareg.drive())
