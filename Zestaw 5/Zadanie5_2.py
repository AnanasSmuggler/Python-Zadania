"""
ZADANIE 5.2

Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach. 
Ułamek będzie reprezentowany przez listę dwóch liczb całkowitych [licznik, mianownik]. Napisać kod testujący moduł fracs. 
Nie należy korzystać z klasy Fraction z modułu fractions. Można wykorzystać funkcję fractions.gcd() implementującą algorytm Euklidesa. 
"""

import fracs
import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac([12, 15], [6, 15]), [6, 5])
        self.assertEqual(fracs.add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(fracs.add_frac([5, 6], [1, 3]), [7, 6])
    
    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac([12, 15], [6, 15]), [2, 5])
        self.assertEqual(fracs.sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(fracs.sub_frac([5, 6], [1, 3]), [1, 2])
    
    def test_mul_frac(self):
        self.assertEqual(fracs.mul_frac([3, 2], [2, 3]), [1, 1])
        self.assertEqual(fracs.mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(fracs.mul_frac([25, 4], [1, 25]), [1, 4])
    
    def test_div_frac(self):
        self.assertEqual(fracs.div_frac([3, 2], [2, 3]), [9, 4])
        self.assertEqual(fracs.div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(fracs.div_frac([25, 4], [1, 25]), [625, 4])

    def test_is_positive(self):
        self.assertEqual(fracs.is_positive([3, 2]), True)
        self.assertEqual(fracs.is_positive([-11, 2]), False)
        self.assertEqual(fracs.is_positive([11, -2]), False)
        self.assertEqual(fracs.is_positive([-11, -2]), True)
        self.assertEqual(fracs.is_positive(self.zero), False)

    def test_is_zero(self):
        self.assertEqual(fracs.is_zero(self.zero), True)
        self.assertEqual(fracs.is_zero([1, 2]), False)

    def test_cmp_frac(self):
        self.assertEqual(fracs.cmp_frac([3, 2], [3, 2]), 0)
        self.assertEqual(fracs.cmp_frac([-11, 2], [0, 3]), -1)
        self.assertEqual(fracs.cmp_frac([11, -2], [-22, 2]), 1)
    
    def test_frac2float(self):
        self.assertEqual(fracs.frac2float([1,2]), 0.5)
        self.assertEqual(fracs.frac2float([4,16]), 0.25)
        self.assertEqual(fracs.frac2float([10,100]), 0.1)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy