from .room import Room


class AloneOld(Room):
    room_cost = 10

    def __init__(self, family_name: str, pension: float):
        budget = pension
        members_count = 1
        super().__init__(family_name, budget, members_count)
        self.expenses += AloneOld.room_cost
