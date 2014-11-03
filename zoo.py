
class Zoo:
    ANIMAL_INCOME = 60
    MEAT = 4
    GRASS = 2
    FOLIAGE = 2
    BAMBOO = 2

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

    def remove_animal(self, animal):
        for a in self.animals:
            if a is animal:
                self.animals.remove(a)

    def is_empty(self):
        return len(self.animals) < self.capacity

    def get_income(self):
        outcome = len(self.animals) * self.ANIMAL_INCOME
        return outcome

    #TO ADD 
    def get_outcome(self):
        pass




    # #####The zoo can accommodate an animal
    # #####It has daily incomes depending on how much animals it has (the more animals it has, the more interesting it will be to go into that zoo, right?)
    # It has daily outcomes depending on how much do the animals eat (every food has its price)
    # #####Sadly, animals can die in the zoo :/
    # The animals can reproduce again half an year (6 months) after their gestation period is over.
