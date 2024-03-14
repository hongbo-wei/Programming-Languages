class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()
    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it')
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    def fill_gas_tank(self):
        print('Please fill the gas tank with #95 oil.')

class Battery():
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f'This car has a {self.battery_size}-KWh battery.')
    def get_range(self, car_model):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f'{car_model.title()} can go about {range} miles on a full charge.')
    # exercise 9.9
    def update_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    def fill_gas_tank(self):
        print('This car has no gas tank')


my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range('model s')

# exercise 9-9 Update Battery
print('\nBefore updated:')
my_tesla.battery.get_range('model s')
my_tesla.battery.update_battery()
print('Battery updated: ')
my_tesla.battery.get_range('model s')