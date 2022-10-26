from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass

    @abstractmethod
    def create_chair(self):
        pass


class VictorianFactory(AbstractFactory):
    def create_table(self):
        return Table('Victorian')

    def create_sofa(self):
        return Sofa('Victorian')

    def create_chair(self):
        return Chair('Victorian')


class ModernFactory(AbstractFactory):
    def create_table(self):
        return Table('Modern')

    def create_sofa(self):
        return Sofa('Modern')

    def create_chair(self):
        return Chair('Modern')


class FuturisticFactory(AbstractFactory):
    def create_table(self):
        return Table('Futuristic')

    def create_sofa(self):
        return Sofa('Futuristic')

    def create_chair(self):
        return Chair('Futuristic')


class Sofa:
    def __init__(self, name):
        self.name = name


class Table:
    def __init__(self, name):
        self.name = name


class Chair:
    def __init__(self, name):
        self.name = name


factory = ModernFactory()
table = factory.create_table()
print(table.name)
