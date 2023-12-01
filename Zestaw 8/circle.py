from point import Point
import math

class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius) -> None:
        if radius <= 0:
            raise ValueError("promień ujemny")
        
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self) -> str:       # "Circle(x, y, radius)"
        return f'Circle({self.pt.getX()}, {self.pt.getY()}, {self.radius})'

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    @classmethod
    def from_points(cls, points: list):
        if len(points) != 3:
            raise ValueError("Należy podać dokładnie 3 punkty!")
        
        x1, y1 = points[0].getX(), points[0].getY()
        x2, y2 = points[1].getX(), points[1].getY()
        x3, y3 = points[2].getX(), points[2].getY()

        d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        ux = ((x1**2 + y1**2) * (y2 - y3) + (x2**2 + y2**2) * (y3 - y1) + (x3**2 + y3**2) * (y1 - y2)) / d
        uy = ((x1**2 + y1**2) * (x3 - x2) + (x2**2 + y2**2) * (x1 - x3) + (x3**2 + y3**2) * (x2 - x1)) / d

        center = Point(ux, uy)
        radius = math.sqrt((ux - x1)**2 + (uy - y1)**2)

        return cls(center.getX(), center.getY(), radius)
    
    @property
    def top(self) -> float:
        return self.pt.getY() + self.radius
    
    @property
    def bottom(self) -> float:
        return self.pt.getY() - self.radius
    
    @property
    def left(self) -> float:
        return self.pt.getX() - self.radius
    
    @property
    def right(self) -> float:
        return self.pt.getX() + self.radius
    
    @property
    def width(self) -> float:
        return self.radius * 2
    
    @property
    def height(self) -> float:
        return self.radius * 2
    
    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

    def getPoint(self) -> Point:
        return self.pt
    
    def getRadius(self) -> float:
        return self.radius

    def area(self) -> float:           # pole powierzchni
        return self.radius**2 * math.pi

    def move(self, x, y) -> None:     # przesuniecie o (x, y)
        p = Point(x,y)
        self.pt = self.pt + p

    def cover(self, other) -> object:   # najmniejszy okrąg pokrywający oba
        x1, y1 = self.pt.getX(), self.pt.getY()
        x2, y2 = other.getPoint().getX(), other.getPoint().getY()
        r1, r2 = self.getRadius(), other.getRadius()

        d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

        if d + r1 <= r2:
            return other
        elif d + r2 <= r1:
            return self
        
        ox = (x1 + x2) / 2
        oy = (y1 + y2) / 2


        dox1 = math.sqrt((ox-x1)**2 + (oy-y1)**2)
        dox2 = math.sqrt((ox-x2)**2 + (oy-y2)**2)

        enclosing_radius = max(dox1 + r1, dox2 + r2)


        return Circle(ox, oy,enclosing_radius)
       