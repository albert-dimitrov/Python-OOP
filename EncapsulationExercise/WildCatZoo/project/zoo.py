from OOP.EncapsulationExercise.WildCatZoo.project.caretaker import Caretaker
from OOP.EncapsulationExercise.WildCatZoo.project.cheetah import Cheetah
from OOP.EncapsulationExercise.WildCatZoo.project.keeper import Keeper
from OOP.EncapsulationExercise.WildCatZoo.project.lion import Lion
from OOP.EncapsulationExercise.WildCatZoo.project.tiger import Tiger
from OOP.EncapsulationExercise.WildCatZoo.project.vet import Vet


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        if price > self.__budget:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)

        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)

        return f"{worker_name} fired successfully"

    def pay_workers(self):
        money_needed = sum([s.salary for s in self.workers])

        if money_needed > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= money_needed

        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        money_needed = sum([c.money_for_care for c in self.animals])

        if money_needed > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= money_needed

        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == 'Lion']
        tigers = [a for a in self.animals if a.__class__.__name__ == 'Tiger']
        cheetahs = [a for a in self.animals if a.__class__.__name__ == 'Cheetah']

        animals_info = f'You have {len(self.animals)} animals\n'

        animals_info += f'----- {len(lions)} Lions:\n'
        animals_info += "\n".join([lion.__repr__() for lion in lions])

        animals_info += f"\n----- {len(tigers)} Tigers:\n"
        animals_info += "\n".join([tiger.__repr__() for tiger in tigers])

        animals_info += f"\n----- {len(cheetahs)} Cheetahs:\n"
        animals_info += "\n".join([cheetah.__repr__() for cheetah in cheetahs])

        return animals_info

    def workers_status(self):
        keeper = [x for x in self.workers if x.__class__.__name__ == 'Keeper']
        caretaker = [x for x in self.workers if x.__class__.__name__ == 'Caretaker']
        vet = [x for x in self.workers if x.__class__.__name__ == 'Vet']

        workers_info = f"You have {len(self.workers)} workers"

        workers_info += f"\n----- {len(keeper)} Keepers:\n"
        workers_info += "\n".join([k.__repr__() for k in keeper])

        workers_info += f"\n----- {len(caretaker)} Caretakers:\n"
        workers_info += "\n".join([c.__repr__() for c in caretaker])

        workers_info += f"\n----- {len(vet)} Vets:\n"
        workers_info += "\n".join([v.__repr__() for v in vet])

        return workers_info

