import unittest
from skills2 import *

class TestSkills2(unittest.TestCase):

    def setUp(self):
        self.string1 = "I do not like green eggs and ham."
        self.list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
        self.list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
        self.words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "San", "I", "am"]

    def test_count_unique(self):
        self.assertEqual(count_unique(self.string1), {'a': 2, ' ': 7, 'e': 4, 'd': 2, 'g': 3, 'I': 1, 'h': 1, 'k': 1, 'm': 1, 'l': 1, 'o': 2, 'n': 3, 'i': 1, 's': 1, 'r': 1, 't': 1, '.': 1})

    def test_common_items(self):
        self.assertEqual(common_items(self.list1, self.list2), [8, 2, -5, 6])

    def test_common_items2(self):
        self.assertEqual(common_items2(self.list1, self.list2), [-5, 6, 8, 2])

    def test_sum_zero(self):
        self.assertEqual(sum_zero(self.list1), [[2,-2], [5,-5]])

    

if __name__ == "__main__":
    unittest.main()