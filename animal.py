
class Animal:
    DAYS_IN_MONTH = 30.0
    MONTHS_IN_YEAR = 12.0
    GROWTH_RATE_AGE = 30.0      # grows with 30 days per grow() call
    GROWTH_RATE_WEIGHT = 1.0    # grows with 1 kilo per grow() call

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age                  # stores days
        self.name = name
        self.gender = gender
        self.weight = weight

        # call setters for the following variables
        self.life_expectancy = None

    def set_life_expectancy(self, life_expectancy):
        self.life_expectancy = life_expectancy

    def get_current_animal_year(self):
        return int(self.age / self.DAYS_IN_MONTH / self.MONTHS_IN_YEAR) + 1

    def get_chance_of_dying(self):
        if self.life_expectancy is not None:
            return self.get_current_animal_year() / self.life_expectancy
        else:
            raise ValueError("life_expectancy not set!")

    def grow(self):
        self.age += self.GROWTH_RATE_AGE
        self.weight += self.GROWTH_RATE_WEIGHT

    def eat(self):
        self.weight += self.GROWTH_RATE_WEIGHT
