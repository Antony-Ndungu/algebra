from math import sqrt

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError("The coordinates must be nonempty.")
        except TypeError:
            raise TypeError("The coordinates must be an iterable.")

    def __str__(self):
        return "Vector: {}".format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates
    
    def plus(self, v):
        return Vector([x + y for x, y in zip(self.coordinates, v.coordinates)])
    
    def minus(self, v):
        return Vector([x - y for x, y in zip(self.coordinates, v.coordinates)])

    def times_scalar(self, c):
        return Vector([ c * num  for num in self.coordinates])

    def magnitude(self):
        return sqrt(sum([coordinate ** 2 for coordinate in self.coordinates]))
    
    def normalize(self):
        magnitude = self.magnitude()
        try:
            return self.times_scalar(1.0/magnitude)
        except ZeroDivisionError:
            raise Exception("Cannot normalize the zero vector.")