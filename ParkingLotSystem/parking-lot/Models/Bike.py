from .Vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, number, vehicle_type):
        super().__init__(number, vehicle_type)