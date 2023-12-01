from point import Point
from circle import Circle

p1 = Point(0,0)
p2 = Point(4,0)
p3 = Point(0,3)

c = Circle.from_points([p1,p2,p3])
print(c.pt.getX(), c.pt.getY(), c.radius)