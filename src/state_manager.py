from track import Track
from racer import Racer
from vector import Vector
import numpy as np
class State_Manager():
    
    def __init__(self):

        self.start = Vector(0,5)
        self.end = Vector(0, -5)

        self.track = Track(self.start, self.end)

        self.racer = Racer(Vector(0,0))
    
    def get_state(self):
        return

    def get_view(self, position, direction):
        fov = self.racer.get_fov()
        view_array = np.zeros(len(fov))
        for i,view in enumerate(fov):
            nearest_object_in_view = self.racer.fov_distance
            for inner_wall, outer_wall in zip(self.track.get_walls()):
                nearest_object_in_view = min(view.intersection(inner_wall).magnitude(), nearest_object_in_view)
                nearest_object_in_view = min(view.intersection(outer_wall).magnitude(), nearest_object_in_view)
            view_array[i] += nearest_object_in_view
        return view_array
    
    def update(self):
        self.racer.move(self.get_view(self.racer.get_positon()))
    



    