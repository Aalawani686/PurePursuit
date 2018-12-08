import copy
import math

'''
Injecting points
Smoothing
Distances Between Points
Curvature of Path
Velocities
'''

class PathGeneration(object):
    base = None
    injected = None
    smoothed = None
    pathC = None
    pathV = None

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
        if(self.base is None):
            print("Path not created")
            return
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

    def smoothPath(self, a, b, tolerance):
        if(self.injected is None):
            print("Path not injected")
            return
        self.smoothed = copy.deepcopy(self.injected)
        change = tolerance
        while(change >= tolerance):
            change = 0.0
            for i in range(1, len(self.smoothed[0])-1):
                for j in range(0, 2):
                    add = a * (self.injected[j][i] - self.smoothed[j][i])
                    add2 = b * (self.smoothed[j][i-1] + self.smoothed[j][i+1] - (2.0 * self.smoothed[j][i]))

                    aux = self.smoothed[j][i]
                    self.smoothed[j][i] += add
                    self.smoothed[j][i] += add2
                    change += math.fabs(aux - self.smoothed[j][i])

    def radiusPath(self):
        if(self.smoothed is None):
            print("Path not smoothed")
            return
        self.pathC = []
        self.pathC.append(0)
        for node in range(1, len(self.smoothed[0][:-1])):
            x1 = self.smoothed[0][node] + 0.00001
            y1 = self.smoothed[1][node]
            x2 = self.smoothed[0][node - 1]
            y2 = self.smoothed[1][node - 1]
            x3 = self.smoothed[0][node + 1]
            y3 = self.smoothed[1][node + 1]

            c1 = (x1*x1 + y1*y1 - x2*x2 - y2*y2)/(2*(x1 - x2))
            c2 = (y1-y2)/(x1-x2)
            b = (x2*x2 - 2*x2*c1 + y2*y2 - x3*x3 + 2*x3*c1 - y3*y3)/(2*(x3*c2 - y3 + y2 - x2*c2))
            a = c1 - c2*b
            r = math.sqrt((x1-a)**2 + (y1-b)**2)

            self.pathC.append(r)
        self.pathC.append(0)
