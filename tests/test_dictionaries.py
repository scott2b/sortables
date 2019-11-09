import unittest
from sortables import Sortable


class TestSortableDictionary(unittest.TestCase):

    d = { 'a':1, 'b':2, 'c': 3 }
    s = Sortable(d)

    def test_sorted(self):
        self.assertEqual(
            list(self.s.sorted().keys()),
            sorted(self.d.keys()))

    def test_sorted_reverse(self):
        self.assertEqual(
            list(self.s.sorted(reverse=True).keys()),
            sorted(self.d.keys(), reverse=True))

    def test_sorted_byvalue(self):
        self.assertEqual(
            list(self.s.sorted(by_value=True).values()),
            sorted(self.d.values()))

    def test_sorted_byvalue_reverse(self):
        self.assertEqual(
            list(self.s.sorted(by_value=True, reverse=True).values()),
            sorted(self.d.values(), reverse=True))
