from .animal import Bird
from wild_farm.food import Meat
from wild_farm.food import Fruit
from wild_farm.food import Vegetable
from wild_farm.food import Seed


class Owl(Bird):
    _GETTING_FAT_RATE = 0.25
    _FOOD_PREFERENCES = tuple([Meat])

    def make_sound(self):
        return 'Hoot Hoot'




class Hen(Bird):
    _GETTING_FAT_RATE = 0.35
    _FOOD_PREFERENCES = None

    def make_sound(self):
        return 'Cluck'


