from .Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, number, vehicle_type):
        super().__init__(number, vehicle_type)