import unittest
from collections import namedtuple
from sortables import Sortable


class TestSortableSeries(unittest.TestCase):

    t_t = ( ('a', 1), ('b', 2), ('c', 3) ) # tuple of tuples
    l_t = list(t_t) # list of tuples
    st_t = Sortable(t_t) # sortable tuple of tuples
    sl_t = Sortable(l_t) # sortable list of tuples
    TestTuple = namedtuple('TestTuple', ['a', 'b'])
    t_n = ( TestTuple(a=1, b=2),
            TestTuple(a=3, b=4), TestTuple(a=5, b=6) ) # tuple of named tuples
    l_n = list(t_n) # list of named tuples
    st_n = Sortable(t_n) # sortable tuple of named tuples
    sl_n = Sortable(l_n) # sortable list of named tuples

    def test_sorted_t(self):
        self.assertEqual(
            self.st_t.sorted(),
            Sortable(sorted(self.t_t)))

    def test_sorted_l(self):
        self.assertEqual(
            self.sl_t.sorted(),
            Sortable(sorted(self.l_t)))

    def test_sorted_reverse_t(self):
        self.assertEqual(
            self.st_t.sorted(reverse=True),
            Sortable(sorted(self.t_t, reverse=True)))

    def test_sorted_reverse_l(self):
        self.assertEqual(
            self.sl_t.sorted(reverse=True),
            Sortable(sorted(self.l_t, reverse=True)))

    def test_sorted_byindex_t(self):
        self.assertEqual(
            [y for x,y in self.st_t.sorted(key=1)],
            sorted([y for x,y in self.t_t]))

    def test_sorted_byindex_l(self):
        self.assertEqual(
            [y for x,y in self.sl_t.sorted(key=1)],
            sorted([y for x,y in self.l_t]))

    def test_sorted_byindex_reverse_t(self):
        self.assertEqual(
            [y for x,y in self.st_t.sorted(key=1, reverse=True)],
            sorted([y for x,y in self.t_t], reverse=True))

    def test_sorted_byindex_reverse_l(self):
        self.assertEqual(
            [y for x,y in self.sl_t.sorted(key=1, reverse=True)],
            sorted([y for x,y in self.l_t], reverse=True))

    def test_sorted_byattr_t(self):
        self.assertEqual(
            self.st_n.sorted(key='a'),
            Sortable(sorted(self.t_n)))
        self.assertEqual(
            [y for x,y in self.st_n.sorted(key='b')],
            sorted([y for x,y in self.t_n]))

    def test_sorted_byattr_l(self):
        self.assertEqual(
            self.sl_n.sorted(key='a'),
            Sortable(sorted(self.l_n)))
        self.assertEqual(
            [y for x,y in self.sl_n.sorted(key='b')],
            sorted([y for x,y in self.l_n]))

    def test_sorted_byattr_reverse_t(self):
        self.assertEqual(
            self.st_n.sorted(key='a', reverse=True),
            Sortable(sorted(self.t_n, reverse=True)))
        self.assertEqual(
            [y for x,y in self.st_n.sorted(key='b', reverse=True)],
            sorted([y for x,y in self.t_n], reverse=True))

    def test_sorted_byattr_reverse_l(self):
        self.assertEqual(
            self.sl_n.sorted(key='a', reverse=True),
            Sortable(sorted(self.l_n, reverse=True)))
        self.assertEqual(
            [y for x,y in self.sl_n.sorted(key='b', reverse=True)],
            sorted([y for x,y in self.l_n], reverse=True))

    def test_sorted_bymultindex_t(self):
        self.assertEqual(
            [y for x,y in self.st_t.sorted(key=(0,1))],
            sorted([y for x,y in self.t_t]))

    def test_sorted_bymultindex_l(self):
        self.assertEqual(
            [y for x,y in self.sl_t.sorted(key=(0,1))],
            sorted([y for x,y in self.l_t]))

    def test_sorted_bylambda_t(self):
        self.assertEqual(
            self.st_t.sorted(key=lambda x:x[0]),
            Sortable(sorted(self.t_t)))

    def test_sorted_bylambda_l(self):
        self.assertEqual(
            self.sl_t.sorted(key=lambda x:x[0]),
            Sortable(sorted(self.l_t)))


class ExampleClass(object):

    def __init__(self, val):
        self.val = val

    def get_val(self):
        return self.val

    def get_appended_val(self, prefix):
        """An arbitrary way to test the methodcaller with an argument"""
        return '%s%s' % (prefex, self.val)


class TestMethodCaller(unittest.TestCase):

    ex_a = ExampleClass('a')
    ex_b = ExampleClass('b')
    ex_c = ExampleClass('c')
    t = (ex_b, ex_c, ex_a)
    sorted_t = [ex_a, ex_b, ex_c] # sorted always returns a list
    s = Sortable(t)


    def test_sortby_method(self):
        self.assertEqual(
            self.s.sorted(method='get_val'),
            Sortable(self.sorted_t))
