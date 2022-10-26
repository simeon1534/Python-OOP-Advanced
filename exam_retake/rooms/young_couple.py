from rooms.room import Room
from appliances.tv import TV
from appliances.fridge import Fridge
from appliances.laptop import Laptop


class YoungCouple(Room):
    room_cost = 20
    appliances = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        budget = salary_one + salary_two
        members_count = 2
        super().__init__(family_name, budget, members_count)
        self.calculate_expenses(*self.appliances)
        self.expenses += YoungCouple.room_cost

