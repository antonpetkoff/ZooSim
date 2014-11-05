import unittest

from zoo import Zoo
from animal import Animal


class TestZoo(unittest.TestCase):

    def setUp(self):
        self.zoo = Zoo(10, 100)

    def test_init(self):
        self.assertEqual(10, self.zoo.capacity)
        self.assertEqual(100, self.zoo.budget)

    def test_accommodate_animal(self):
        the_tiger = Animal("Tiger", 15, "Dingo", "male", 90)
        self.zoo.accommodate_animal(the_tiger)
        self.assertIn(the_tiger, self.zoo.animals)

    def test_cant_accommodate_animal_with_duplicate_name(self):
        the_tiger = Animal("Tiger", 15, "Dingo", "male", 90)
        the_copycat = Animal("Tiger", 15, "Dingo", "male", 90)
        self.zoo.accommodate_animal(the_tiger)
        with self.assertRaises(ValueError):
            self.zoo.accommodate_animal(the_copycat)

    def test_accomodate_same_names_diff_species(self):
        the_tiger = Animal("Tiger", 15, "Dingo", "male", 90)
        the_cat = Animal("Cat", 15, "Dingo", "male", 90)
        self.zoo.accommodate_animal(the_tiger)
        self.zoo.accommodate_animal(the_cat)
        self.assertIn(the_tiger, self.zoo.animals)
        self.assertIn(the_cat, self.zoo.animals)

    def test_accommodate_to_full_zoo(self):
        zoo_1_animal = Zoo(1, 100)
        the_tiger = Animal("Tiger", 15, "Dingo", "male", 90)
        the_cat = Animal("Cat", 15, "Dingo", "male", 90)
        zoo_1_animal.accommodate_animal(the_tiger)
        zoo_1_animal.accommodate_animal(the_cat)
        self.assertNotIn(the_cat, zoo_1_animal.animals)

    def test_get_income(self):
        the_tiger = Animal("Tiger", 15, "Dingo", "male", 90)
        the_cat = Animal("Cat", 15, "Dingo", "male", 90)
        self.zoo.accommodate_animal(the_tiger)
        self.zoo.accommodate_animal(the_cat)
        self.assertEqual(2 * self.zoo.ANIMAL_INCOME, self.zoo.get_income())

##### NO FOOD/WIGHT RATIO
    def test_get_outcome(self):
        the_tiger = Animal("Tiger", 15, "Dingo", "male", 90)
        the_tiger.set_food_type("meat")
        the_cat = Animal("Cat", 15, "Dingo", "male", 90)
        the_cat.set_food_type("grass")
        self.zoo.accommodate_animal(the_tiger)
        self.zoo.accommodate_animal(the_cat)
        self.assertEqual(self.zoo.MEAT_PRICE + self.zoo.GRASS_PRICE, self.zoo.get_outcome())

    def test_remove_dead_animal(self):
        the_tiger = Animal("Tiger", 15, "Dingo", "male", 90)
        the_tiger.life_expectancy = 1000
        the_cat = Animal("Cat", 15, "Dingo", "male", 90)
        the_cat.life_expectancy = 0.0001
        self.zoo.accommodate_animal(the_tiger)
        self.zoo.accommodate_animal(the_cat)
        self.zoo.remove_dead_animals()
        self.assertNotIn(the_cat, self.zoo.animals)

    def test_alive_animal_not_removed(self):
        the_tiger = Animal("Tiger", 15, "Dingo", "male", 90)
        the_tiger.life_expectancy = 1000000000
        self.zoo.accommodate_animal(the_tiger)
        self.zoo.remove_dead_animals()
        self.assertIn(the_tiger, self.zoo.animals)


#TODO Test adding animals
if __name__ == '__main__':
    unittest.main()
