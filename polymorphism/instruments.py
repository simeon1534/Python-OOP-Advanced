from abc import ABC, abstractmethod


class Instrument(ABC):

    @abstractmethod
    def play(self):
        pass


def play_instrument(instrument: Instrument):
    return instrument.play()


class Guitar:
    def play(self):
        print("playing the guitar")

guitar = Guitar()
play_instrument(guitar)
