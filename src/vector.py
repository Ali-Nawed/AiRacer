import numpy as np

class Vector():
    '''
    stores data about point in 2d plane
    and contains methods for operations with other points
    '''
    
    def __init__(self, x, y): 
        self._point = np.asarray([x, y])
    
    @staticmethod
    def create_vector(distance, direction):
        return Vector(distance*np.cos(direction), distance*np.sin(direction))

    def getX(self):
        return self._point[0]
    
    def getY(self):
        return self._point[1]

    def norm(self):
        return np.linalg.norm(self._point)
    
    def magnitude(self):
        return np.sqrt(np.linalg.norm(self._point))

    def slope(self, other):
        '''
        returns the slope where this point contains (x1, y1)
        '''
        return (other.getY() - self.getY()) / (other.getX() - self.getX())

    def cross_product(self, other):
        return np.cross(self._point, other._point)
    
    def dot(self, other):
        return np.dot(self._point, other._point)
    
    def translate(self, distance, direction):
        new_vector = self.create_vector(distance, direction + self.get_direction())
        return Vector(new_vector.getX() + self.getX(),
        new_vector.getY() + self.getY())

    def reflect_x(self):
        return Vector(self.getX(), -self.getY())

    def reflect_y(self):
        return Vector(-self.getX(), self.getY())

    def get_direction(self):
        return np.arctan2(self.getY(), self.getX())

    def __eq__(self, other):
        return self._point == other._point
    
    def __add__(self, other):
        return Vector(self.getX() + other.getX(), self.getY() + other.getY())

    def __sub__(self, other):
        return Vector(self.getX() - other.getX(), self.getY() - other.getY())
    
    def __mul__(self, integer):
        return Vector(integer*self.getX(), integer*self.getY())



