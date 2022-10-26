from car_manager import Car
import unittest


class CarTests(unittest.TestCase):
    def setUp(self):
        self.car = Car("Renault", "Megan", 4, 100)

    def test_init(self):
        self.assertEqual(self.car.make, "Renault")
        self.assertEqual(self.car.model, "Megan")
        self.assertEqual(self.car.fuel_consumption, 4)
        self.assertEqual(self.car.fuel_capacity, 100)

    def test_refuel_when_no_fuel(self):
        with self.assertRaises(Exception):
            self.car.refuel(0)

    def test_refuel_when_fuel_positive(self):
        self.car.refuel(1)
        old_fuel = self.car.fuel_amount
        new_fuel = self.car.fuel_amount + 1
        self.assertEqual(new_fuel, old_fuel + 1)

    def test_refuel_when_fuel_positive_and_fuel_over_capacity(self):
        self.car.refuel(105)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_drive_enough_fuel(self):
        self.car.refuel(50)
        old_fuel_amount = self.car.fuel_amount
        self.car.drive(100)  # needed = 4
        self.assertEqual(self.car.fuel_amount, old_fuel_amount - 4)

    def test_drive_enough_not_fuel(self):
        self.car.refuel(50)
        with self.assertRaises(Exception):
            self.car.drive(1300)  # needed = 52

    def test_make_empty_new_value_raise_exception(self):
        with self.assertRaises(Exception):
            self.car.make = ''

    def test_model_empty_new_value_raise_exception(self):
        with self.assertRaises(Exception):
            self.car.model = ''

    def test_fuel_capacity_negative_or_zero_raise_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_capacity = 0

    def test_fuel_consumption_negative_or_zero_raise_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_consumption = 0


if __name__ == '__main__':
    unittest.main()
