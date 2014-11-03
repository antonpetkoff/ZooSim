import unittest

from zoo import Zoo
from animal import Animal


class TestZoo(unittest.TestCase):

    def test_init(self):
        zoo = Zoo(10, 100)
        self.assertEqual(10, zoo.capacity)
        self.assertEqual(100, zoo.budget)

    def test_accommodate_animal(self):
        zoo = Zoo(10, 100)
        the_tiger = Animal("Tiger", 15, "Dingo", "male", 90)
        zoo.accommodate_animal(the_tiger)
        self.assertIn(the_tiger, zoo.animals)

    def test_cant_accommodate_animal_with_duplicate_name(self):
        zoo = Zoo(10, 100)
        the_tiger = Animal("Tiger", 15, "Dingo", "male", 90)
        the_copycat = Animal("Tiger", 15, "Dingo", "male", 90)
        zoo.accommodate_animal(the_tiger)
        with self.assertRaises(ValueError):
            zoo.accommodate_animal(the_copycat)

    def test_accomodate_same_names_diff_species(self):
        zoo = Zoo(10, 100)
        the_tiger = Animal("Tiger", 15, "Dingo", "male", 90)
        the_cat = Animal("Cat", 15, "Dingo", "male", 90)
        zoo.accommodate_animal(the_tiger)
        zoo.accommodate_animal(the_cat)
        self.assertIn(the_tiger, zoo.animals)
        self.assertIn(the_cat, zoo.animals)

    def test_accommodate_to_full_zoo(self):
        zoo = Zoo(1, 100)
        the_tiger = Animal("Tiger", 15, "Dingo", "male", 90)
        the_cat = Animal("Cat", 15, "Dingo", "male", 90)
        zoo.accommodate_animal(the_tiger)
        zoo.accommodate_animal(the_cat)
        self.assertNotIn(the_cat, zoo.animals)

    def test_get_income(self):
        zoo = Zoo(10, 100)
        the_tiger = Animal("Tiger", 15, "Dingo", "male", 90)
        the_cat = Animal("Cat", 15, "Dingo", "male", 90)
        zoo.accommodate_animal(the_tiger)
        zoo.accommodate_animal(the_cat)
        self.assertEqual(2 * zoo.ANIMAL_INCOME, zoo.get_income())

    def test_get_outcome(self):
        zoo = Zoo(10, 100)
        the_tiger = Animal("Tiger", 15, "Dingo", "male", 90)
        the_tiger.set_food_type("meat")
        the_cat = Animal("Cat", 15, "Dingo", "male", 90)
        the_cat.set_food_type("grass")
        zoo.accommodate_animal(the_tiger)
        zoo.accommodate_animal(the_cat)
        self.assertEqual(zoo.MEAT_PRICE + zoo.GRASS_PRICE, zoo.get_outcome())



#TODO Test adding animals
if __name__ == '__main__':
    unittest.main()
