import unittest
from XYRobot import XYRobot


class TestXYRobot(unittest.TestCase):
    def setUp(self):
        self.r2d2 = XYRobot("R2-D2", 100.0, 100.0)
        self.forward = (150, 100)
        self.turn_left = (270)
        self.backward = (50, 100)
        self.turn_right = (90)

    def test_move_forward(self):
        self.r2d2.move_forward(50)
        self.assertEqual(self.r2d2.position(), self.forward)

    def test_turn_left(self):
        self.r2d2.turn_left()
        self.assertEqual(self.r2d2.angle(), self.turn_left)

    def test_move_backward(self):
        self.r2d2.move_backward(50)
        self.assertEqual(self.r2d2.position(), self.backward)

    def test_turn_right(self):
        self.r2d2.turn_right()
        self.assertEqual(self.r2d2.angle(), self.turn_right)


if __name__ == '__main__':
    unittest.main()
