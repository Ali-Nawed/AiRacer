import numpy as np
from vector import Vector
from invalid_vector import Invalid_Vector
class Line_Segment():
    '''
    Wall class defined by a start and end point in a 2d plane
    A track will be made from a series of walls
    '''
    def __init__(self, start, end):

        self.EPS = 1e-5
        self.start = start
        self.end = end
        self._vector = Vector(self.end.getX() - self.start.getX(),
                              self.end.getY() - self.start.getY())

    def get_length_squared(self):
        return (self.end - self.start).norm()  

    def get_length(self):
        return np.sqrt(self.get_length_squared())
    
    def get_norm(self):
        return

    def does_intersect(self, position):
        '''
        checks if a point intersects this wall
        '''
        
        start_to_end = self.end - self.start

        start_to_postition = position - self.start

        cross_prod = start_to_end.cross_product(start_to_postition)

        if (np.abs(cross_prod) > self.EPS):
            return False

        dot_prod = start_to_end.dot(start_to_postition)

        if (dot_prod < 0 or dot_prod > self.get_length_squared()):
            return False
        
        return True

    def intersection(self, other):
        '''
        checks if and where 2 lines segments
        '''
        A = np.array([self._vector._point, -1*other._vector._point]).T
        b = other.start._point - other.end._point

        soln = np.linalg.lstsq(A, b)

        rank = soln[2]

        if rank < 2:
            return Invalid_Vector()
        
        t = soln[0][0]
        return (1-t)*self.start + t*self.end        

    def get_parallel_wall(self, distance):
        '''
        returns a Wall object that is a line which is parallel to this wall
        at some distance away ie distance = 0 returns the same wall
        positive distance returns a wall on the left side
        negative distance returns a wall on the right side
        '''

        if distance >= 0:
            return self._vector.translate(distance, np.pi/2)
        else:
            return self._vector.translate(-distance, -np.pi/2)
        



        





