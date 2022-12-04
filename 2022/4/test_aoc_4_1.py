import unittest

from aoc_4_1 import is_fully_containing

f = is_fully_containing


class TestSum(unittest.TestCase):
    def test_no_intersection(self):
        self.assertEqual(f([[32, 34], [85, 100]]), False)
        self.assertEqual(f([[1,1], [2, 2]]), False)

    def test_neg_w_inters(self):
        self.assertEqual(f([[32, 34], [33, 100]]), False)
        self.assertEqual(f([[1,3], [2, 4]]), False)

    def test_first_in_sec(self):
        self.assertEqual(f([[32, 34], [20, 40]]), True)
        self.assertEqual(f([[20,30], [20, 50]]), True)

    def test_sec_in_first(self):
        self.assertEqual(f([[32, 34], [33, 33]]), True)
        self.assertEqual(f([[10, 20], [13,14]]), True)

    def test_same_ranges(self):
        self.assertEqual(f([[32, 32], [32, 32]]), True)


if __name__ == '__main__':
    unittest.main()




