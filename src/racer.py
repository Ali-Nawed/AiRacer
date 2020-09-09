from vector import Vector
from line import Line_Segment
import numpy as np

class Racer():

    def __init__(self, position):
        self.position = self.position
        self.speed = 0
        self.direction = 0
        self.fov_distance = 10
        self.field_of_view = [Vector.create_vector(self.fov_distance, 0),
                    Vector.create_vector(self.fov_distance, np.pi/4),
                    Vector.create_vector(self.fov_distance, -np.pi/4)]
    
    def move(self, view):
        #updates its position and returns
        return self.position
    
    def get_positon(self):
        return self.position
    
    def get_speed(self):
        return self.speed

    def get_direction(self):
        return self.direction

    def get_fov(self):
        return [Line_Segment(self.position, self.position + Vector.create_vector(self.fov_distance, self.direction + view.direction)) for view in self.field_of_view]

    