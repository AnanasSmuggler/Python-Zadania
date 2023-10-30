# Kod testujący moduł.

import math
from point import Point
from rectangles import Rectangle
import unittest

class TestPoint(unittest.TestCase):
    def setUp(self) -> None:
        self.rectA = Rectangle(0,0,4,2)
        self.rectB = Rectangle(-1,-1,-3,-6)
        self.rectC = Rectangle(-4,3,5,-4)

    def test_str(self):
        self.assertEqual(self.rectA.__str__(), "[(0, 0), (4, 2)]")
        self.assertEqual(self.rectB.__str__(), "[(-1, -1), (-3, -6)]")
        self.assertEqual(self.rectC.__str__(), "[(-4, 3), (5, -4)]")
   
    def test_repr(self):
        self.assertEqual(self.rectA.__repr__(), "Rectangle(0, 0, 4, 2)")
        self.assertEqual(self.rectB.__repr__(), "Rectangle(-1, -1, -3, -6)")
        self.assertEqual(self.rectC.__repr__(), "Rectangle(-4, 3, 5, -4)")

    def test_eq(self):
        self.assertEqual(self.rectA.__eq__(self.rectA), True)
        self.assertEqual(self.rectA.__eq__(self.rectB), False)
        self.assertEqual(self.rectB.__eq__(self.rectB), True)
        self.assertEqual(self.rectB.__eq__(self.rectA), False)
        self.assertEqual(self.rectC.__eq__(self.rectC), True)
        self.assertEqual(self.rectC.__eq__(self.rectB), False)

    def test_ne(self):
        self.assertEqual(self.rectA.__ne__(self.rectA), False)
        self.assertEqual(self.rectA.__ne__(self.rectB), True)
        self.assertEqual(self.rectB.__ne__(self.rectB), False)
        self.assertEqual(self.rectB.__ne__(self.rectA), True)
        self.assertEqual(self.rectC.__ne__(self.rectC), False)
        self.assertEqual(self.rectC.__ne__(self.rectB), True)
    
        
    def test_center(self):
        self.assertEqual(self.rectA.center(), Point(2,1))
        self.assertEqual(self.rectB.center(), Point(-2,-3.5))
        self.assertEqual(self.rectC.center(), Point(0.5,-0.5))
    

    def test_area(self):
        self.assertEqual(self.rectA.area(), 8)
        self.assertEqual(self.rectB.area(), 10)
        self.assertEqual(self.rectC.area(), 63)

    def test_move(self):
        rA = Rectangle(0,0,4,2)
        rB = Rectangle(-1,-1,-3,-6)
        rC = Rectangle(-4,3,5,-4)
        rA.move(2,2)
        rB.move(-2,2)
        rC.move(2,-2)
        self.assertEqual(rA.getPt1(), Point(2,2))
        self.assertEqual(rA.getPt2(), Point(6,4))
        self.assertEqual(rB.getPt1(), Point(-3,1))
        self.assertEqual(rB.getPt2(), Point(-5,-4))
        self.assertEqual(rC.getPt1(), Point(-2,1))
        self.assertEqual(rC.getPt2(), Point(7,-6))

    def tearDown(self): pass
    

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy