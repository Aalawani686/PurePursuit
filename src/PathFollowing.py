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
