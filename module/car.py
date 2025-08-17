from battery import Battery


class Car:
    """create a car"""

    def __init__(self, make, model, year):
        """initialize the car attribute"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def show_car(self):
        """show details of car"""
        return f'{self.year} {self.make} {self.model}'.title()

    def read_odometer(self):
        return f'This car has {self.odometer} kms on it.'

    def update_odometer(self, kms):
        if kms > self.odometer:
            self.odometer = kms
        else:
            print('Warning: you can set odometer back')

    def drive(self, kms=0):
        if kms >= 0:
            self.odometer += kms
        else:
            print('you cannot reduce the odometer!!!')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
