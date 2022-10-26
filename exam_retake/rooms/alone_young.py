from .room import Room
from appliances.tv import TV


class AloneYoung(Room):
    room_cost = 10
    appliances = [TV()]

    def __init__(self, family_name: str, pension: float):
        budget = pension
        members_count = 1
        super().__init__(family_name, budget, members_count)
        self.calculate_expenses(*self.appliances)
        self.expenses += AloneYoung.room_cost
