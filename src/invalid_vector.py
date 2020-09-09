from vector import Vector

class Invalid_Vector(Vector):
    """
    Vector that reprents no point, used when returning
    the output of an intersection being none
    """
    def __init__(self):

        super(float('inf'), float('inf'))