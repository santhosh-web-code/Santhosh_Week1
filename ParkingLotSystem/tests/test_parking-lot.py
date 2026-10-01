from Models.Bike import Bike
from Models.Car import Car
from Models.ParkingFloor import ParkingFloor
from Models.ParkingLot import ParkingLot
from Models.Parking_slot import ParkingSlot
from Models.Truck import Truck
from services.ParkinglotServices import ParkingLotServices


def test_vehicle_types_expose_number_and_type():
	vehicles = [
		Bike("KA-01-HH-1234", "Bike"),
		Car("LA-01-HH-1237", "Car"),
		Truck("MA-01-HH-1240", "Truck"),
	]

	assert [(vehicle.getNumber(), vehicle.getType()) for vehicle in vehicles] == [
		("KA-01-HH-1234", "Bike"),
		("LA-01-HH-1237", "Car"),
		("MA-01-HH-1240", "Truck"),
	]


def test_parking_lot_services_accepts_and_releases_vehicle(capsys):
	service = ParkingLotServices()
	vehicle = Bike("KA-01-HH-1234", "Bike")

	assert service.parkVehicle(vehicle) is True
	assert service.unParkVehicle(vehicle) is True
	assert capsys.readouterr().out.splitlines() == [
		"KA-01-HH-1234",
		"KA-01-HH-1234",
	]


def test_parking_floor_has_parking_slots():
	slot = ParkingSlot(1)
	floor = ParkingFloor(1, [slot])

	assert floor.floor_id == 1
	assert floor.parking_slots == [slot]

	new_slot = ParkingSlot(2)
	floor.addParkingSlot(new_slot)
	assert floor.parking_slots == [slot, new_slot]


def test_parking_lot_has_parking_floors():
	floor = ParkingFloor(1)
	lot = ParkingLot([floor])

	assert lot.parking_floors == [floor]

	new_floor = ParkingFloor(2)
	lot.addParkingFloor(new_floor)
	assert lot.parking_floors == [floor, new_floor]
