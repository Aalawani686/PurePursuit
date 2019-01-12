class wheelVel:
    V = 0 # Target velocity
    L = 0 # Target left wheel velocity
    R = 0 # Target right wheel velocity
    C = 0 # Curvature
    T = 0 # Track width

    def calculate(self):
        self.L = self.V * (2 + (self.C * self.T)) / 2
        self.R = self.V * (2 - (self.C * self.T)) / 2

    def getLeft(self):
        return self.L

    def getRight(self):
        return self.R

    def setCurvature(self, curvature):
        self.C = curvature

    def setVelocity(self, velocity):
        self.V = velocity

    def __init__(self, curvature, trackWidth):
        self.C = curvature
        self.T = trackWdith

    def __init__(self, curvature, trackWidth, targetVelocity):
        self.C = curvature
        self.T = trackWidth
        self.V = targetVelocity
        self.calculate()
