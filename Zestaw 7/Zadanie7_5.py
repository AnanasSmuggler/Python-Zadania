# Kod testujący moduł.

import math
from point import Point
from circle import Circle
import unittest

class TestCircle(unittest.TestCase):
    def setUp(self) -> None:
        self.circleA = Circle(3, -2, 4)
        self.circleB = Circle(-4, 5, 3)
        self.circleC = Circle(1, 2, 6)

    def test_init(self):
        with self.assertRaises(ValueError) as context:
            Circle(0,0,-2)

        with self.assertRaises(ValueError) as context2:
            Circle(0,0,0)

        self.assertEqual(str(context.exception), "promień ujemny")
        self.assertEqual(str(context2.exception), "promień ujemny")
   
    def test_repr(self):
        self.assertEqual(self.circleA.__repr__(), "Circle(3, -2, 4)")
        self.assertEqual(self.circleB.__repr__(), "Circle(-4, 5, 3)")
        self.assertEqual(self.circleC.__repr__(), "Circle(1, 2, 6)")


    def test_eq(self):
        self.assertEqual(self.circleA == Circle(3, -2, 4), True)
        self.assertEqual(self.circleA == self.circleB, False)
        self.assertEqual(self.circleB == Circle(-4, 5, 3), True)
        self.assertEqual(self.circleB == self.circleC, False)
        self.assertEqual(self.circleC == Circle(1, 2, 6), True)
        self.assertEqual(self.circleC == self.circleA, False)

    def test_ne(self):
        self.assertEqual(self.circleA.__ne__(self.circleA), False)
        self.assertEqual(self.circleA.__ne__(self.circleB), True)
        self.assertEqual(self.circleB.__ne__(self.circleB), False)
        self.assertEqual(self.circleB.__ne__(self.circleA), True)
        self.assertEqual(self.circleC.__ne__(self.circleC), False)
        self.assertEqual(self.circleC.__ne__(self.circleB), True)


    def test_area(self):
        a1 = math.pi * 4**2
        a2 = math.pi * 3**2
        a3 = math.pi * 6**2
        self.assertEqual(self.circleA.area(), a1)
        self.assertEqual(self.circleB.area(), a2)
        self.assertEqual(self.circleC.area(), a3)


    def test_move(self):
        cA = Circle(3, -2, 4)
        cB = Circle(-4, 5, 3)
        cC = Circle(1, 2, 6)
        cA.move(2,2)
        cB.move(-2,2)
        cC.move(2,-2)
        self.assertEqual(cA.getPoint(), Point(5,0))
        self.assertEqual(cB.getPoint(), Point(-6,7))
        self.assertEqual(cC.getPoint(), Point(3,0))

    def test_cover(self):
        c1 = self.circleA.cover(self.circleB)
        c2 = self.circleB.cover(self.circleC)
        c3 = self.circleC.cover(self.circleA)
        self.assertAlmostEqual(c1.getPoint().getX(), -0.5, places=1)
        self.assertAlmostEqual(c1.getPoint().getY(), 1.5, places=1)
        self.assertAlmostEqual(c1.getRadius(), 8.9, places=1)
        self.assertAlmostEqual(c2.getPoint().getX(), -1.5, places=1)
        self.assertAlmostEqual(c2.getPoint().getY(), 3.5, places=1)
        self.assertAlmostEqual(c2.getRadius(), 8.9, places=1)
        self.assertAlmostEqual(c3.getPoint().getX(), 2, places=1)
        self.assertAlmostEqual(c3.getPoint().getY(), 0, places=1)
        self.assertAlmostEqual(c3.getRadius(), 8.2, places=1)

    def tearDown(self): pass
    

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy