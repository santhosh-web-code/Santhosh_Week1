from .ParkingFloor import ParkingFloor


class ParkingLot:
    def __init__(self, parking_floors=None):
        self.parking_floors = list(parking_floors or [])

    def addParkingFloor(self, parking_floor):
        if not isinstance(parking_floor, ParkingFloor):
            raise TypeError("parking_floor must be a ParkingFloor")
        self.parking_floors.append(parking_floor)
