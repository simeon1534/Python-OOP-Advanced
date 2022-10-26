from restaurant.product import Product


class Food(Product):
    grams: float

    def __init__(self, name, price, grams):
        super().__init__(name, price)
        self._grams = grams

    @property
    def grams(self):
        return self._grams

    @grams.setter
    def grams(self, value):
        self._grams = value