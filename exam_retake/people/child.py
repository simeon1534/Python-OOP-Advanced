class Child:
    cost: float

    def __init__(self, food_cost: int, *toys_cost):
        self.food_cost = food_cost
        self.toys_cost = sum(toys_cost)
        self.cost = self.food_cost + self.toys_cost

