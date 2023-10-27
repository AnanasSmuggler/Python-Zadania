# Kod testujący moduł.

import math
from point import Point
import unittest

class TestPoint(unittest.TestCase):
    def setUp(self) -> None:
        self.a = Point(1,1)
        self.b = Point(5,3)
        self.c = Point(-2,-4)
    
    def test_str(self):
        self.assertEqual(self.a.__str__(), "(1, 1)")
        self.assertEqual(self.b.__str__(), "(5, 3)")
        self.assertEqual(self.c.__str__(), "(-2, -4)")
        
    def test_repr(self):
        self.assertEqual(self.a.__repr__(), "Point(1, 1)")
        self.assertEqual(self.b.__repr__(), "Point(5, 3)")
        self.assertEqual(self.c.__repr__(), "Point(-2, -4)")

    def test_eq(self):
        self.assertEqual(self.a.__eq__(self.a), True)
        self.assertEqual(self.a.__eq__(self.b), False)
        self.assertEqual(self.b.__eq__(self.b), True)
        self.assertEqual(self.b.__eq__(self.a), False)
        self.assertEqual(self.c.__eq__(self.c), True)
        self.assertEqual(self.c.__eq__(self.b), False)

    def test_ne(self):
        self.assertEqual(self.a.__ne__(self.a), False)
        self.assertEqual(self.a.__ne__(self.b), True)
        self.assertEqual(self.b.__ne__(self.b), False)
        self.assertEqual(self.b.__ne__(self.a), True)
        self.assertEqual(self.c.__ne__(self.c), False)
        self.assertEqual(self.c.__ne__(self.b), True)
        
    def test_add(self):
        self.assertEqual(self.a.__add__(self.a), Point(2,2))
        self.assertEqual(self.a.__add__(self.b), Point(6,4))
        self.assertEqual(self.a.__add__(self.c), Point(-1,-3))
        self.assertEqual(self.b.__add__(self.a), Point(6,4))
        self.assertEqual(self.b.__add__(self.b), Point(10,6))
        self.assertEqual(self.b.__add__(self.c), Point(3,-1))
        self.assertEqual(self.c.__add__(self.a), Point(-1,-3))
        self.assertEqual(self.c.__add__(self.b), Point(3,-1))
        self.assertEqual(self.c.__add__(self.c), Point(-4,-8))

    def test_sub(self):
        self.assertEqual(self.a.__sub__(self.a), Point(0,0))
        self.assertEqual(self.a.__sub__(self.b), Point(-4,-2))
        self.assertEqual(self.a.__sub__(self.c), Point(3,5))
        self.assertEqual(self.b.__sub__(self.a), Point(4,2))
        self.assertEqual(self.b.__sub__(self.b), Point(0,0))
        self.assertEqual(self.b.__sub__(self.c), Point(7,7))
        self.assertEqual(self.c.__sub__(self.a), Point(-3,-5))
        self.assertEqual(self.c.__sub__(self.b), Point(-7,-7))
        self.assertEqual(self.c.__sub__(self.c), Point(0,0))

    def test_mul(self):
        self.assertEqual(self.a.__mul__(self.a), 2)
        self.assertEqual(self.a.__mul__(self.b), 8)
        self.assertEqual(self.a.__mul__(self.c), -6)
        self.assertEqual(self.b.__mul__(self.a), 8)
        self.assertEqual(self.b.__mul__(self.b), 34)
        self.assertEqual(self.b.__mul__(self.c), -22)
        self.assertEqual(self.c.__mul__(self.a), -6)
        self.assertEqual(self.c.__mul__(self.b), -22)
        self.assertEqual(self.c.__mul__(self.c), 20)
        
    def test_cross(self):
        self.assertEqual(self.a.cross(self.a), 0)
        self.assertEqual(self.a.cross(self.b), -2)
        self.assertEqual(self.a.cross(self.c), -2)
        self.assertEqual(self.b.cross(self.a), 2)
        self.assertEqual(self.b.cross(self.b), 0)
        self.assertEqual(self.b.cross(self.c), -14)
        self.assertEqual(self.c.cross(self.a), 2)
        self.assertEqual(self.c.cross(self.b), 14)
        self.assertEqual(self.c.cross(self.c), 0)

    def test_length(self):
        self.assertEqual(self.a.length(), math.sqrt(2))
        self.assertEqual(self.b.length(), math.sqrt(34))
        self.assertEqual(self.c.length(), math.sqrt(20))
        
    def test_hash(self):
        self.assertEqual(self.a.__hash__(), hash((1,1)))
        self.assertEqual(self.b.__hash__(), hash((5,3)))
        self.assertEqual(self.c.__hash__(), hash((-2,-4)))
        
    def tearDown(self): pass
    

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy