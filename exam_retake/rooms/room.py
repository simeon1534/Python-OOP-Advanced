from people.child import Child
from appliances.appliance import Appliance
from typing import List


class Room:
    family_name: str
    budget: float
    members_count: int
    children: List[Child]

    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.__expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):  # (appliance1,appliance2,child1...)
        total = 0

        for arg in args:
            if isinstance(arg, Appliance):
                total += arg.get_monthly_expense() * self.members_count
            else:
                total += arg.cost * 30
        self.expenses = total





