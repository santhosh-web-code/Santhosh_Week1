from .Vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, number, vehicle_type):
        super().__init__(number, vehicle_type)