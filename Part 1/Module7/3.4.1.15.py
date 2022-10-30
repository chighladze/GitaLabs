import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(x - self.get_x(), y - self.get_y())

    def distance_from_point(self, point):
        return math.hypot(point.get_x() - self.get_x(), point.get_y() - self.get_y())


#
# The code copied from the previous lab.
#


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertice1 = vertice1.distance_from_point(vertice2)
        self.__vertice2 = vertice2.distance_from_point(vertice3)
        self.__vertice3 = vertice3.distance_from_point(vertice1)
    #
    # Write code here
    #
    def perimeter(self):
        return self.__vertice1 + self.__vertice2 + self.__vertice3


#
# Write code here
#


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
