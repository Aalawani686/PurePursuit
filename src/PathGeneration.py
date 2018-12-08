import math

'''
Injecting points
Smoothing
Distances Between Points
Curvature of Path
Velocities
'''

class PathGeneration(object):
    base = []
    injected = []
    smoothed = []
    pathC = []
    pathV = []

    def __init__(self, base):
        if(len(base) < 2):
            print("Path base waypoints less than 2")
            return
        self.base = base

    def distance(self, x1, y1, x2 = None, y2 = None):
        if(x2 is None or y2 is None):
            return math.sqrt((x1**2) + (y1**2))
        else:
            return math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))


    def injectPath(self, spacing):
        x = []
        y = []
        for node in range(len(self.base[0][:-1])):
            deltaX = self.base[0][node + 1] - self.base[0][node]
            deltaY = self.base[1][node + 1] - self.base[1][node]
            toInject = (int)(math.ceil(self.distance(deltaX, deltaY)/spacing))
            for iter in range(toInject):
                x.append(self.base[0][node] + ((int)(deltaX * iter / toInject)))
                y.append(self.base[1][node] + ((int)(deltaY * iter / toInject)))
        self.injected = [x, y]
