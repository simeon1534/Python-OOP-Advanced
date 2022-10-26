from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    def feed(self, food):
        if self._FOOD_PREFERENCES is not None \
                and not isinstance(food, self._FOOD_PREFERENCES):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += (food.quantity * self._GETTING_FAT_RATE)

    @property
    @abstractmethod
    def _GETTING_FAT_RATE(self):
        pass

    @property
    @abstractmethod
    def _FOOD_PREFERENCES(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass


class Mammal(Animal):
    living_region: str

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Bird(Animal):
    wing_size: float

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"
