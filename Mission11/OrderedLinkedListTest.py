import unittest
from OrderedLinkedList import *


class OrderedLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.list = [1, 2, 3]
        self.size = 3
        self.inc_size = 4
        self.dec_size = 2
        self.first = 1
        self.set_first = 3
        self.print = [1, 2, 3, 4]
        self.t = OrderedLinkedList(self.list)

    def test_size(self):
        self.assertEqual(self.t.size(), self.size)

    def test_inc_size(self):
        self.t.inc_size()
        self.assertEqual(self.t.size(), self.inc_size)

    def test_dec_size(self):
        self.t.dec_size()
        self.assertEqual(self.t.size(), self.dec_size)


if __name__ == '__main__':
    unittest.main()
