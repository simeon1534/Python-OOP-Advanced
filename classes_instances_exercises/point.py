import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, x, y):
        edna_strana = abs(self.x - x)
        vtora_strana = abs(self.y - y)
        hipotenuza_na_vtora_stepen = edna_strana ** 2 + vtora_strana ** 2
        hipotenuza = math.sqrt(hipotenuza_na_vtora_stepen)
        return hipotenuza


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))
