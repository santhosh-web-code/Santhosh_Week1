from .Parking_slot import ParkingSlot


class ParkingFloor:
    def __init__(self, floor_id, parking_slots=None):
        self.floor_id = floor_id
        self.parking_slots = list(parking_slots or [])

    def addParkingSlot(self, parking_slot):
        if not isinstance(parking_slot, ParkingSlot):
            raise TypeError("parking_slot must be a ParkingSlot")
        self.parking_slots.append(parking_slot)
