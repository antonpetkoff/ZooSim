from animal import Animal
import unittest


class TestAnimals(unittest.TestCase):

    def test_init(self):
        animal = Animal("Tiger", 15, "Dingo", "male", 90)
        self.assertEqual(animal.species, "Tiger")
        self.assertEqual(animal.age, 15)
        self.assertEqual(animal.name, "Dingo")
        self.assertEqual(animal.gender, "male")
        self.assertEqual(animal.weight, 90)


if __name__ == '__main__':
    unittest.main()
