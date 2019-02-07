import math

'''
Closest Point
Lookahead Point
Curvature of Arc
Wheel Velocities
Controlling Wheel Velocities
Tuning
Stopping
'''

class PathFollowing(object):
    curPoint = None
    path = None

    robotLoc = [300, 80]
    robotAng = -55
    robotW = 20
    robotL = 20

    def __init__(self, path, startPoint = [0, 0]):
        self.curPoint = startPoint
        self.path = path

    def wheelVelocity(self, V, C, T):
        return [V*(2+(C*T))/2, V*(2-(C*T))/2]
    '''
    def lookahead(self, E, L, C, r):
        def dot(a, b):
            return sum(x * y for x, y in zip(a, b))

        d = [L[0]-E[0], L[1]-E[1]]
        f = [E[0]-C[0], E[1]-C[1]]

        a = dot(d, d)
        b = 2*dot(f, d)
        c = dot(f, f)-(r*r)
        discriminant = (b*b)-(4*a*c)

        if(discriminant < 0):
            return None
        else:
            discriminant = math.sqrt(discriminant)
            t1 = (-b-discriminant)/(2*a)
            t2 = (-b+discriminant)/(2*a)
            if(t1 >= 0 and t1 <= 1):
                return [E[0]+(t1*d[]), ]
            if(t2 >= 0 and t2 <= 1):
                print(t2)
                return
            return None
    '''
    def drawRobot(self):
        x = []
        x.append(self.robotLoc[0] + (math.hypot(self.robotW/2, self.robotL/2) * math.cos(math.radians(self.robotAng + 45))))
        x.append(self.robotLoc[0] + (math.hypot(self.robotW/2, self.robotL/2) * math.cos(math.radians(self.robotAng + 135))))
        x.append(self.robotLoc[0] + (math.hypot(self.robotW/2, self.robotL/2) * math.cos(math.radians(self.robotAng + 225))))
        x.append(self.robotLoc[0] + (math.hypot(self.robotW/2, self.robotL/2) * math.cos(math.radians(self.robotAng + 315))))
        x.append(self.robotLoc[0] + (math.hypot(self.robotW/2, self.robotL/2) * math.cos(math.radians(self.robotAng + 45))))
        y = []
        y.append(self.robotLoc[1] + (math.hypot(self.robotW/2, self.robotL/2) * math.sin(math.radians(self.robotAng + 45))))
        y.append(self.robotLoc[1] + (math.hypot(self.robotW/2, self.robotL/2) * math.sin(math.radians(self.robotAng + 135))))
        y.append(self.robotLoc[1] + (math.hypot(self.robotW/2, self.robotL/2) * math.sin(math.radians(self.robotAng + 225))))
        y.append(self.robotLoc[1] + (math.hypot(self.robotW/2, self.robotL/2) * math.sin(math.radians(self.robotAng + 315))))
        y.append(self.robotLoc[1] + (math.hypot(self.robotW/2, self.robotL/2) * math.sin(math.radians(self.robotAng + 45))))
        return [x, y]
