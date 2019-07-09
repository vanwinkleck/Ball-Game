
from math import sqrt

class Point:
    """A model for a two-dimensional Cartesian point."""
    def __init__(self, x=0, y=0):
        """Construct a point with initial coordinates (x,y).

        Default (x,y) is (0,0).
        """
        self._x = x
        self._y = y
        
    def getX(self):
        """Return the x-coordinate of the point."""
        return self._x

    def getY(self):
        """Return the y-coordinate of the point."""
        return self._y

    def setX(self, val):
        """Set the x-coordinate of the point to the given value.

        The value should be numeric.
        """
        self._x = val

    def setY(self, val):
        """Set the y-coordinate of the point to the given value.

        The value should be numeric.
        """
        self._y = val

    def scale(self, factor):
        self._x *= factor
        self._y *= factor
     
    def distance(self, other):
        dx = self._x - other._x
        dy = self._y - other._y
        return sqrt(dx * dx + dy * dy)              # imported from math module

    def magnitude(self):
        return self.distance( Point() )

    def normalize(self):
        mag = self.magnitude()
        if mag > 0:
            self.scale(1/mag)
            
    def __str__(self):
        return '<' + str(self._x) + ',' + str(self._y) + '>'

    def __add__(self, other):
        return Point(self._x + other._x, self._y + other._y)
    
    def __sub__(self, other):
        return Point(self._x - other._x, self._y - other._y)

    def __eq__ (self, other):
        if self._x == other._x and self._y == other._y:
            return True
        else:
            return False

    def __mul__(self, operand):
        if isinstance(operand, (int,float)):        # multiply by constant
            return Point(self._x * operand, self._y * operand)
        elif isinstance(operand, Point):            # dot product
            return self._x * operand._x + self._y * operand._y

    def __rmul__(self, operand):
        return self * operand


if __name__ == '__main__':
    pt1 = Point (25, 40)
    print ('pt1 = <' + str(pt1.getX()) + ',' + str(pt1.getY()) + '>')
    print ('pt1.magnitude() =', pt1.magnitude())
    pt2 = Point (10, 75)
    print ('pt2 = <' + str(pt2.getX()) + ',' + str(pt2.getY()) + '>')
    pt1.setX (pt2.getY())
    pt1.setY (pt2.getX())
    print ('pt1 = <' + str(pt1.getX()) + ',' + str(pt1.getY()) + '>')
    pt1.normalize()
    print ('pt1 = <' + str(pt1.getX()) + ',' + str(pt1.getY()) + '>')
    
    
