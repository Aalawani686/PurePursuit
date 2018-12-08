'''
Closest Point
Lookahead Point
Curvature of Arc
Wheel Velocities
Controlling Wheel Velocities
Tuning
Stopping
'''

class PathFollowing(objects):
    curPoint = None
    path = None

    def __init__(self, startPoint = [0, 0], path):
        self.curPoint = startPoint
        self.path = path
