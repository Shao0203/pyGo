class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def show_battery(self):
        print(f'The battery has {self.battery_size}mA.')

    def update_battery(self, cost):
        self.battery_size -= cost

    def get_range(self):
        if self.battery_size >= 100:
            range = 1000
        elif self.battery_size >= 60:
            range = 600
        elif self.battery_size >= 40:
            range = 400
        print(f'this car can ran {range} miles')

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
