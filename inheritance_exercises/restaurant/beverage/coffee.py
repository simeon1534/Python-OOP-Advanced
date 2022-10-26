from restaurant.beverage.hot_beverage import HotBeverage
from typing import ClassVar


class Coffee(HotBeverage):
    COFFEE_MILLILITERS: ClassVar[int] = 50
    COFFEE_PRICE: ClassVar[int] = 3.50
    __caffeine: float

    def __init__(self, name, caffeine):
        super().__init__(name, self.__class__.COFFEE_PRICE, self.__class__.COFFEE_MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

    @caffeine.setter
    def caffeine(self, value):
        self.__caffeine = value

coffee1 = Coffee('Name', 44)
print(coffee1._milliliters)