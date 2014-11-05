from zoo import Zoo
from animal import Animal


class ZooSimulator:
    PRINT_ANIMAL_FORMAT = "{} - {}, {}, {}"

    def __init__(self):
        #add initializing
        pass

    def print_animals(self):
        for animal in self.zoo.animals:
            print(self.PRINT_ANIMAL_FORMAT.format(animal.name, animal.species, animal.age, animal.weight))
