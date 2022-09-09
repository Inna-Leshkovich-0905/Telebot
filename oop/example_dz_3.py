class Car:
    # Статические поля (переменные класса)
    default_color = 'Grey'
    default_weight = 5000
    default_fuel = 'diesel'
    default_transmission = 'manual'
    def __init__(self, model, color, transmission, fuel):
        # Динамические поля (переменные объекта)
        self.model = model
        self.color = color
        self.transmission = transmission
        self.fuel = fuel

    def turn_on(self):
        pass

    def ride(self):
        pass

car_object = Car('BMW', 'red', 'automatic', 'petrol')

print(car_object.model)
print(car_object.color)
print(car_object.transmission)
print(car_object.fuel)

print(car_object.default_color)
print(car_object.default_weight)
print(car_object.default_transmission)
print(car_object.default_fuel)


print(dir(Car))