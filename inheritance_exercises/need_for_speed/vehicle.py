from typing import ClassVar


class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: ClassVar[float] = 1.25
    fuel_consumption: float
    fuel: float
    horse_power: int

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.__class__.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        fuel_needed = kilometers * self.fuel_consumption
        if fuel_needed > self.fuel:
            return
        self.fuel -= fuel_needed




obj = Vehicle(50, 150)
print(obj.fuel_consumption)
