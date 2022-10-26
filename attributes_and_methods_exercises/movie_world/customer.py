

class Customer:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []  # LIST WITH DVD INSTANCES

    def __repr__(self):
        res = [dvd_obj.name for dvd_obj in self.rented_dvds]

        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({', '.join(res)}) "
