import random

list_of_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'D', 'K', 'A']
suits = ['spades', 'hearts', 'diamonds', 'clubs']


class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} of {self.suit}"


class Deck(list):
    def __init__(self):
        super().__init__()
        self.cards = []
        for card in list_of_cards:
            for suit in suits:
                self.cards.append(Card(card, suit))

    @staticmethod
    def shuffle(deck_instance: 'Deck'):
        random.shuffle(deck_instance.cards)
        return deck_instance

    def __str__(self):
        res = []
        for obj in self.cards:
            res.append(str(obj))
        return ', '.join(res)



