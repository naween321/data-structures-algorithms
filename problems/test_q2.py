import unittest
from . import q2



class TestQ1(unittest.TestCase):
    def test_one(self):
        result = q2.arrange([5, 2, 3, 1, 9, 10])
        self.assertEqual(result, [[1, 2, 3], [5], [9, 10]])


if __name__ == '__main__':
    unittest.main()
