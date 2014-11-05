from random import random


class Animal:
    MONTHS_IN_YEAR = 12
    GROWTH_RATE_AGE = 1.0      # grows with 1 month per grow() call
    GROWTH_RATE_WEIGHT = 1.0    # grows with 1 kilo per grow() call

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age                  # stores months
        self.name = name
        self.gender = gender
        self.weight = weight

        self.is_dead = False
        self.newborn_weight = self.weight / 10

        # call setters for the following variables
        self.life_expectancy = None
        self.food_type = None

    def set_life_expectancy(self, life_expectancy):
        self.life_expectancy = life_expectancy

    def set_food_type(self, food_type):
        self.food_type = food_type

    def get_current_animal_year(self):
        return int(self.age / self.MONTHS_IN_YEAR) + 1

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

    def is_alive(self):
        if not self.is_dead:
            chance_of_dying = self.get_chance_of_dying()
            if random() < chance_of_dying:
                self.is_dead = True
                return False
            else:
                return True
        else:
            return False
