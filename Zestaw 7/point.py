import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x: float, y: float):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self) -> str:         # zwraca string "(x, y)"
        return f'({self.x}, {self.y})'

    def __repr__(self) -> str:        # zwraca string "Point(x, y)"
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other) -> bool:   # obsługa point1 == point2
        return self.x == other.x and self.y == other.y if isinstance(other, Point) else False

    def __ne__(self, other) -> bool:        # obsługa point1 != point2
        return self.x != other.x or self.y != other.y if isinstance(other, Point) else False

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other) -> float:  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return (self.x * other.x) + (self.y * other.y)
        
    def getX(self) -> float:
        return self.x

    def getY(self) -> float:
        return self.y

    def cross(self, other) -> float:         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self) -> float:          # długość wektora
        return math.sqrt(self.x**2 + self.y**2)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points