

class Car: 

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"this car has {self.odometer_reading} km on it")

    def update_odometer(self,km):
        self.odometer_reading = km

    def increment_odometer(self,km):
        self.odometer_reading += km

    def fill_gas_tank(self):
        print("gas tank is now full!")

class Battery:

    def __init__(self,battery_size=75):
        self.battery_size = battery_size

    def upgrade_battery(self):
        self.battery_size = 100 if self.battery_size == 75 else 75
        
    def get_battery_size(self):
        print(f"battery size is {self.battery_size} kWh")

    def get_range(self):

        if self.battery_size == 75:
            range = 260

        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} km on a full chanrge.")

class ElectricCar(Car):
     
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()


    def fill_gas_tank(self):
        print("it\'s an electric car u can\'t use gas")

my_tesla = ElectricCar('tesla', 'model s', 2019)

my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()

my_tesla.battery.get_range()