from animal import Animal
import unittest


class TestAnimals(unittest.TestCase):

    def setUp(self):
        self.animal = Animal("Wolf", 1000, "Kumcho", "male", 60)

    def test_init(self):
        animal = Animal("Tiger", 600, "Dingo", "male", 90)
        self.assertEqual(animal.species, "Tiger")
        self.assertEqual(animal.age, 600)
        self.assertEqual(animal.name, "Dingo")
        self.assertEqual(animal.gender, "male")
        self.assertEqual(animal.weight, 90)

    def test_set_life_expectancy(self):
        self.animal.set_life_expectancy(20)
        self.assertEqual(self.animal.life_expectancy, 20)

    def test_get_current_animal_year(self):
        self.assertEqual(self.animal.get_current_animal_year(), 3)

    def test_get_chance_of_dying_valid_life_expectancy(self):
        self.animal.set_life_expectancy(20)
        self.assertEqual(self.animal.get_chance_of_dying(), 0.15)

    def test_get_chance_of_dying_value_error(self):
        with self.assertRaises(ValueError):
            self.animal.get_chance_of_dying()

    def test_grow(self):
        self.animal.grow()
        self.assertEqual(self.animal.age, 1000 + self.animal.GROWTH_RATE_AGE)
        self.assertEqual(self.animal.weight,
                         60 + self.animal.GROWTH_RATE_WEIGHT)

    def test_eat(self):
        self.animal.eat()
        self.assertEqual(self.animal.weight,
                         60 + self.animal.GROWTH_RATE_WEIGHT)


if __name__ == '__main__':
    unittest.main()
