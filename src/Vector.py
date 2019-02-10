class Vector(object):
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    def __init__(self,x1,y1,x2=0,y2=0):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def dot(self, a):
        # returning the dot product of two points
        return (self.x1 * a.x1 + self.y1 * a.y1)

    def cross(self, a):
        # returning the z component of a two vector cross product
        return ((self.x2-self.x1) * (a.y2-a.y1) + (a.x2-a.x1) * (self.y2-self.y1))
