from .animal import Mammal
from wild_farm.food import Meat
from wild_farm.food import Fruit
from wild_farm.food import Vegetable


class Mouse(Mammal):
    _GETTING_FAT_RATE = 0.10
    _FOOD_PREFERENCES = tuple([Vegetable, Fruit])

    def make_sound(self):
        return 'Squeak'


class Dog(Mammal):
    _GETTING_FAT_RATE = 0.40
    _FOOD_PREFERENCES = tuple([Meat])

    def make_sound(self):
        return 'Woof!'


class Cat(Mammal):
    _GETTING_FAT_RATE = 0.30
    _FOOD_PREFERENCES = tuple([Vegetable, Meat])

    def make_sound(self):
        return 'Meow'


class Tiger(Mammal):
    _GETTING_FAT_RATE = 1
    _FOOD_PREFERENCES = tuple([Meat])

    def make_sound(self):
        return 'ROAR!!!'
