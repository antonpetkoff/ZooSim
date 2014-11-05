from random import random
import json


class Animal:
    MONTHS_IN_YEAR = 12

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age                  # stores months
        self.name = name
        self.gender = gender
        self.weight = weight

        self.is_dead = False

        self.life_expectancy = None
        self.food_type = None
        self.gestation_period = None
        self.newborn_weight = None
        self.average_weight = None
        self.weight_age_ratio = None
        self.food_weight_ratio = None

    def load_json(self, directory):
        json_contents = {}
        with open(directory) as jsonInput:
            json_contents = json.load(jsonInput)

        if self.species in json_contents.keys():
            specifics = json_contents[self.species]
            self.life_expectancy = specifics["life_expectancy"]
            self.food_type = specifics["food_type"]
            self.gestation_period = specifics["gestation_period"]
            self.newborn_weight = specifics["newborn_weight"]
            self.average_weight = specifics["average_weight"]
            self.weight_age_ratio = specifics["weight_age_ratio"]
            self.food_weight_ratio = specifics["food_weight_ratio"]
        else:
            raise ValueError("{} species not in JSON".format(self.species))

    def __getitem__(self, attr):
        return self.specifics[attr]

    def get_current_animal_year(self):
        return int(self.age / self.MONTHS_IN_YEAR) + 1

    def get_chance_of_dying(self):
        if self.life_expectancy is not None:
            return self.get_current_animal_year() / self.life_expectancy
        else:
            raise ValueError("No specifics loaded from JSON!")

    def grow(self):
        self.age += self.weight_age_ratio
        self.weight += self.weight * self.food_weight_ratio

    def eat(self):
        self.weight += self.weight * self.food_weight_ratio

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
