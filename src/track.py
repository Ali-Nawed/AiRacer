from line import Line_Segment

class Track():
     '''
     Basic straight track
     '''
     def __init__(self, start, end):
         
         self.start = start
         self.end = end
         self.width = [10]
         self._inner_track_wall = [Line_Segment(start, end)]
         self._outer_track_wall = [wall.get_parallel_wall(self.width[i]) for i,wall in enumerate(self._inner_track_wall)]         
        
        
     def check_collision(self, position):
         for wall in self._inner_track_wall:
             if wall.does_intersect(position):
                 return True
         for wall in self._outer_track_wall:
             if wall.does_intersect(position):
                 return True   
         return False
        
     def get_walls(self):
         return (self._inner_track_wall, self._outer_track_wall)