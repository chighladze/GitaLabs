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


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
