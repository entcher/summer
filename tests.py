import unittest
from main import sum

class TestSum(unittest.TestCase):

    def test_3(self):
        self.assertEqual(sum(1, 2), 3)

    def test_4(self):
        self.assertEqual(sum(2, 2), 4)

    def test_5(self):
        self.assertEqual(sum(3, 2), 5)
