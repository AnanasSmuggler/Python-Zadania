from point import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self) -> str:         # "[(x1, y1), (x2, y2)]"
        return f'[{self.pt1.__str__()}, {self.pt2.__str__()}]'

    def __repr__(self) -> str:        # "Rectangle(x1, y1, x2, y2)"
        return f'Rectangle({self.pt1.getX()}, {self.pt1.getY()}, {self.pt2.getX()}, {self.pt2.getY()})'

    def __eq__(self, other: object) -> bool:   # obsługa rect1 == rect2
        return self.pt1.__eq__(other.getPt1()) and self.pt2.__eq__(other.getPt2())
    
    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def getPt1(self) -> Point:
        return self.pt1

    def getPt2(self) -> Point:
        return self.pt2

    def center(self) -> Point:         # zwraca środek prostokąta
        return Point((self.pt1.getX() + self.pt2.getX()) / 2, (self.pt1.getY() + self.pt2.getY()) / 2)

    def area(self) -> float:            # pole powierzchni
        return abs(self.pt1.getX() - self.pt2.getX()) * abs(self.pt1.getY() - self.pt2.getY())

    def move(self, x, y) -> None:      # przesunięcie o (x, y)    """ 
        p = Point(x,y)
        self.pt1 = self.pt1.__add__(p)
        self.pt2 = self.pt2.__add__(p)