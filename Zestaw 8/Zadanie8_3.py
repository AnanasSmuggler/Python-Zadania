"""
ZADANIE 8.3 (KLASA CIRCLE)

Wzbogacić klasę Circle o nowe funkcjonalności (plik circles.py).

Stworzyć metodę klasy o nazwie 'from_points', która pozwoli utworzyć okrąg z listy lub krotki zawierającej trzy punkty. Punkty będą leżeć na okręgu [trudne!]. Wywołanie:
circle = Circle.from_points((point1, point2, point3))

Za pomocą dekoratora @property dodać atrybuty wirtualne zwracające liczbę (współrzędną): top, left, bottom, right, width, height. Dodać atrybuty wirtualne zwracające Point: topleft, bottomleft, topright, bottomright. Wymienione atrybuty wirtualne opisują prostokąt ograniczający dany okrąg (bounding box).

W osobnym pliku (test_circles.py) przygotować testy klasy Circle w formacie dla modułu 'pytest'.

Autor: Jan Kaleta
"""

from point import Point
from circle import Circle
import pytest
import math

class TestCircle:
    @pytest.fixture
    def circleA(self):
        return Circle(3, -2, 4)

    @pytest.fixture
    def circleB(self):
        return Circle(-4, 5, 3)

    @pytest.fixture
    def circleC(self):
        return Circle(1, 2, 6)

    def test_from_points(self):
        p1 = Point(0,0)
        p2 = Point(4,0)
        p3 = Point(0,3)

        c = Circle.from_points([p1,p2,p3])
        assert c.pt == Point(2,1.5)
        assert math.isclose(c.radius, 2.5)

    def test_bounding_box(self):
        c = Circle(0,0,4)

        assert c.top == 4
        assert c.bottom == -4
        assert c.right == 4
        assert c.left == -4
        assert c.topleft == Point(-4,4)
        assert c.topright == Point(4,4)
        assert c.bottomleft == Point(-4,-4)
        assert c.bottomright == Point(4,-4)

    def test_init(self):
        with pytest.raises(ValueError, match="promień ujemny"):
            Circle(0,0,-3)

        with pytest.raises(ValueError, match="promień ujemny"):
            Circle(0,0,0)

    def test_repr(self, circleA, circleB, circleC):
        assert repr(circleA) == "Circle(3, -2, 4)"
        assert repr(circleB) == "Circle(-4, 5, 3)"
        assert repr(circleC) == "Circle(1, 2, 6)"

    def test_eq(self, circleA, circleB, circleC):
        assert circleA == Circle(3, -2, 4)
        assert circleA != circleB
        assert circleB == Circle(-4, 5, 3)
        assert circleB != circleC
        assert circleC == Circle(1, 2, 6)
        assert circleC != circleA

    def test_ne(self, circleA, circleB, circleC):
        assert not circleA.__ne__(circleA)
        assert circleA.__ne__(circleB)
        assert not circleB.__ne__(circleB)
        assert circleB.__ne__(circleA)
        assert not circleC.__ne__(circleC)
        assert circleC.__ne__(circleB)

    def test_area(self, circleA, circleB, circleC):
        a1 = math.pi * 4**2
        a2 = math.pi * 3**2
        a3 = math.pi * 6**2
        assert circleA.area() == a1
        assert circleB.area() == a2
        assert circleC.area() == a3

    def test_move(self, circleA, circleB, circleC):
        cA = Circle(3, -2, 4)
        cB = Circle(-4, 5, 3)
        cC = Circle(1, 2, 6)
        cA.move(2, 2)
        cB.move(-2, 2)
        cC.move(2, -2)
        assert cA.getPoint() == Point(5, 0)
        assert cB.getPoint() == Point(-6, 7)
        assert cC.getPoint() == Point(3, 0)

    def test_cover(self, circleA, circleB, circleC):
        c1 = circleA.cover(circleB)
        c2 = circleB.cover(circleC)
        c3 = circleC.cover(circleA)
        assert math.isclose(c1.getPoint().getX(), -0.5, rel_tol=1e-1)
        assert math.isclose(c1.getPoint().getY(), 1.5, rel_tol=1e-1)
        assert math.isclose(c1.getRadius(), 8.9, rel_tol=1e-1)
        assert math.isclose(c2.getPoint().getX(), -1.5, rel_tol=1e-1)
        assert math.isclose(c2.getPoint().getY(), 3.5, rel_tol=1e-1)
        assert math.isclose(c2.getRadius(), 8.9, rel_tol=1e-1)
        assert math.isclose(c3.getPoint().getX(), 2, rel_tol=1e-1)
        assert math.isclose(c3.getPoint().getY(), 0, rel_tol=1e-1)
        assert math.isclose(c3.getRadius(), 8.2, rel_tol=1e-1)
