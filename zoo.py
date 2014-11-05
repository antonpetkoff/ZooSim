
class Zoo:
    ANIMAL_INCOME = 60
    MEAT_PRICE = 4
    GRASS_PRICE = 2

    def __init__(self, capacity, budget):
        self.capacity = capacity
        self.budget = budget
        self.animals = []

    def accommodate_animal(self, animal):
        if self.is_empty():
            for a in self.animals:
                if animal.species == a.species and animal.name == a.name:
                    raise ValueError("Name already taken: {}".format(a.name))
            self.animals.append(animal)

    def is_empty(self):
        return len(self.animals) < self.capacity

    def get_income(self):
        income = len(self.animals) * self.ANIMAL_INCOME
        return income

    #TO ADD food/weigh ratio
    def get_outcome(self):
        outcome = 0
        for animal in self.animals:
            if animal.food_type == "meat":
                outcome += self.MEAT_PRICE
            else:
                outcome += self.GRASS_PRICE
        return outcome

    def calculate_budget(self):
        self.budget = self.budget + self.get_income() - self.get_outcome()

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def remove_dead_animals(self):
        for animal in self.animals:
            if not animal.is_alive():
                self.remove_animal(animal)

    def can_afford_food(self):
        return self.budget > 0
