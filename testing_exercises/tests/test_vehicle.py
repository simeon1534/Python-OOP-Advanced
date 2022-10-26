from vehicle import Vehicle, Car, Truck
import unittest


class TestVehicles(unittest.TestCase):
    def test_initialising_vehicles(self):
        Car(100,25)
        Truck(100,25)

    def test_car_refuel(self):
        self.car = Car(100,25)
        self.car.refuel(50)
        self.assertEqual(self.car.fuel_quantity, 150)

    def test_car_drive_enough_fuel(self):
        self.car = Car(100,5)
        self.car.drive(10)
        self.assertEqual(self.car.fuel_quantity, 41)

    def test_car_drive_not_enough_fuel(self):
        self.car = Car(100,50)
        old_fuel = self.car.fuel_quantity
        self.car.drive(2)
        self.assertEqual(self.car.fuel_quantity , old_fuel)

    def test_truck_refuel(self):
        self.truck = Truck(100,1)
        self.truck.refuel(10)
        self.assertEqual(self.truck.fuel_quantity, 109.5)

    def test_truck_drive_enough_fuel(self):
        self.truck = Truck(100, 1)
        self.truck.drive(10) # 26
        self.assertEqual(self.truck.fuel_quantity, 74)

    def test_truck_drive_not_enough_fuel(self):
        self.truck = Truck(100, 1)
        old_fuel = self.truck.fuel_quantity
        self.truck.drive(50)
        self.assertEqual(self.truck.fuel_quantity,old_fuel )


if __name__ == '__main__':
    unittest.main()
