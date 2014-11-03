import unittest

from zoo import Zoo


class TestZoo(unittest.TestCase):

    def test_init(self):
        zoo = Zoo(10, 100)
        self.assertEqual(10, zoo.capacity)
        self.assertEqual(100, zoo.budget)

#TODO Test adding animals

if __name__ == '__main__':
    unittest.main()
