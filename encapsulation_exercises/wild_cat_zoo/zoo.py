from wild_cat_zoo.animal_base import AnimalBase
from wild_cat_zoo.employee_base import EmployeeBase
from wild_cat_zoo.lion import Lion
from wild_cat_zoo.tiger import Tiger
from wild_cat_zoo.cheetah import Cheetah
from wild_cat_zoo.vet import Vet
from wild_cat_zoo.caretaker import Caretaker
from wild_cat_zoo.keeper import Keeper


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal: AnimalBase, price: int):
        if self.__budget >= price and self.__animal_capacity > 0:
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            type_of_animal = type(animal).__name__
            return f"{animal.name} the {type_of_animal} added to the zoo"
        elif self.__animal_capacity > 0:
            return 'Not enough budget'
        else:
            return 'Not enough space for animal'

    def hire_worker(self, worker: EmployeeBase):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            self.__workers_capacity -= 1
            type_of_worker = type(worker).__name__
            return f"{worker.name} the {type_of_worker} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        prev_number_of_workers = len(self.workers)
        self.workers = [
            worker
            for worker in self.workers
            if worker.name != worker_name
        ]
        next_number_of_workers = len(self.workers)
        if prev_number_of_workers == next_number_of_workers:
            return f"There is no {worker_name} in the zoo"
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        total_due = sum([w.salary for w in self.workers])
        if self.__budget >= total_due:
            self.__budget -= total_due
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_due = sum([a.get_needs() for a in self.animals])
        if self.__budget >= total_due:
            self.__budget -= total_due
            return "You tended all the animals. They are happy. Budget left: {left_budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        total_animals_count = len(self.animals)
        lions = [a.__repr__() for a in self.animals if isinstance(a, Lion)]
        tigers = [a.__repr__() for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [a.__repr__() for a in self.animals if isinstance(a, Cheetah)]

        NEW_LINE = "\n"

        return f'''You have {total_animals_count} animals
        ----- {len(lions)}
        Lions:
        {NEW_LINE.join(lions)}
        ----- {len(tigers)}
        Tigers:
        {NEW_LINE.join(tigers)}
        ----- {len(cheetahs)}
        Cheetahs:
        {NEW_LINE.join(cheetahs)}
            '''

    def workers_status(self):
        total_workers_count = len(self.workers)
        keepers = [a.__repr__() for a in self.workers if isinstance(a, Keeper)]
        caretakers = [a.__repr__() for a in self.workers if isinstance(a, Caretaker)]
        vets = [a.__repr__() for a in self.workers if isinstance(a, Vet)]

        NEW_LINE = "\n"

        return f'''You have {total_workers_count} animals
           ----- {len(keepers)}
           Lions:
           {NEW_LINE.join(keepers)}
           ----- {len(caretakers)}
           Tigers:
           {NEW_LINE.join(caretakers)}
           ----- {len(vets)}
           Cheetahs:
           {NEW_LINE.join(vets)}
               '''


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
