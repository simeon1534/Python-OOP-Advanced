from typing import List
from rooms.room import Room


class Everland:
    rooms: List[Room]

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total = 0
        for room in self.rooms:
            total += room.expenses
        return total

    def pay(self):
        result = []
        for room in self.rooms:
            if room.budget >= room.expenses:
                plashtane = f"{room.family_name} paid {room.expenses}$ and have {room.budget - room.expenses}$ left."
                room.budget -= room.expenses
                result.append(plashtane)
            else:
                neplashtane = f"{room.family_name} does not have enough budget and must leave the hotel."
                self.rooms.remove(room)
                result.append(neplashtane)
        return '\n'.join(result)

