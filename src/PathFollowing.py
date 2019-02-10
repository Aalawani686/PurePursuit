import math
from Vector import Vector

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
    lookaheadRadius = 20

    def __init__(self, path, startPoint = [0, 0]):
        self.curPoint = startPoint
        self.path = path

    def lookahead(self, E, L, C):
        d = Vector(L.x1-E.x1, L.y1-E.y1)
        f = Vector(E.x1-C.x1, E.y1-C.y1)
        a = d.dot(d)
        b = 2*f.dot(d)
        c = f.dot(f)-(self.lookaheadRadius*self.lookaheadRadius)
        discriminant = (b*b)-(4*a*c)

        if(discriminant < 0):
    #        return None
            print("target not found")
        else:
            discriminant = math.sqrt(discriminant)
            t1 = (-b-discriminant)/(2*a)
            t2 = (-b+discriminant)/(2*a)
            if(t1 >= 0 and t1 <= 1):
                print("target found")
                intersection = Vector(E.x1+t1*d.x1,E.y1+t1*d.y1)
            if(t2 >= 0 and t2 <= 1):
                print("target found")
                intersection = Vector(E.x1+t2*d.x1,E.y1+t2*d.y1)
            return intersection

    def curvature(self, LAx, LAy, Rx, Ry, theta):
        a = -math.tan(theta)
        b = 1
        c = math.tan(theta)*Rx-Ry
        x = (abs(a*LAx+b*LAy+c))/math.sqrt(a*a+b*b)
        y = LAy-Ry
        rb = Vector(Rx,Ry,Rx+math.cos(theta),Ry+math.sin(theta))
        rl = Vector(Rx,Ry,LAx,LAy)
        if(rb.cross(rl)<0):
            direction = -1
        else:
            direction = 1
        L2 = x*x+y*y
        return (direction*2*x/L2)

    def wheelVelocity(self, V, C, T):
        return V*(2+(C*T))/2, V*(2-(C*T))/2

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
