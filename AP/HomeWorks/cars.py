class Vehicle:
    def __init__(self, manufacturer, capacity, max_speed, mileage=0):
        self.manufacturer = manufacturer
        self.capacity = capacity
        self.max_speed = max_speed
        self.mileage = mileage

    def state(self):
        if self.mileage == 0:
            return "This car is new."
        else:
            return f"This car is second-handed and has {self.mileage} mileages."

    def mileageset(self, mileage):
        self.mileage = mileage


class SUV(Vehicle):
    def __init__(self, manufacturer, capacity, max_speed, mileage=0, wheel_drive="4WD"):
        super().__init__(manufacturer, capacity, max_speed, mileage)
        wheel_drive_types = ["2WD", "4WD", "AWD"]
        self.wheel_drive = wheel_drive if wheel_drive in wheel_drive_types else "4WD"

    def WheelDrive(self):
        return f"This car has a {self.wheel_drive} system."


class Truck(Vehicle):

    def __init__(self, manufacturer, capacity, max_speed, mileage=0, load_capacity=4):
        super().__init__(manufacturer, capacity, max_speed, mileage)
        self.load_capacity = load_capacity

    def LoadCapacity(self):
        return f"This car has {self.load_capacity} tons load capacity."
