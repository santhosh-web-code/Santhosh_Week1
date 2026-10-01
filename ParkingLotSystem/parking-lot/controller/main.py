import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from Models.Bike import Bike
from Models.Car import Car
from Models.Truck import Truck
from services.ParkinglotServices import ParkingLotServices

def main():
    parking_lot_services = ParkingLotServices()
    b1 = Bike("KA-01-HH-1234", "Bike")

    c1 = Car("LA-01-HH-1237", "Car")
    t1 = Truck("MA-01-HH-1240", "Truck")

    result = parking_lot_services.parkVehicle(b1)
    print("Vehicle parked") if result else print("Vehicle not parked")

    result = parking_lot_services.parkVehicle(c1)
    print("Vehicle parked") if result else print("Vehicle not parked")

    result = parking_lot_services.parkVehicle(t1)
    print("Vehicle parked") if result else print("Vehicle not parked")

main()