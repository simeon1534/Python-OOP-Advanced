from rooms.room import Room
from people.child import Child
from appliances.tv import TV
from appliances.fridge import Fridge
from appliances.laptop import Laptop


class YoungCoupleWithChildren(Room):
    room_cost = 30
    appliances = [TV(), Fridge(), Laptop()]
    children_list = []

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children: Child):
        budget = salary_one + salary_two
        members_count = 2 + len(children)
        super().__init__(family_name, budget, members_count)
        self.children = list(children)
        self.calculate_expenses(*self.appliances,*self.children)

        self.expenses += YoungCoupleWithChildren.room_cost


