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

    def __init__(self, path, startPoint = [0, 0]):
        self.curPoint = startPoint
        self.path = path

    def wheelVelocity(self, V, C, T):
        return [V*(2+(C*T))/2, V*(2-(C*T))/2]
