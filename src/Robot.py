import math

class Robot(object):
    alpha = 0.50/4
    beta = 0.015/4
    delta = 20
    dimensions = [50, 50]

    def __init__(self, x = 0, y = 0, theta = 0):
        self.position = [x, y]
        self.theta = math.degrees(theta)
        self.velocity = [0, 0]

    def getPosition(self):
        return [int(self.position[0]), int(self.position[1])]

    def getTheta(self):
        return self.theta

    def setVelocity(self, velocity):
        self.velocity = velocity

    def update(self):
        self.position[0] += math.cos(self.theta) * (self.velocity[0] + self.velocity[1]) * self.alpha
        self.position[1] += math.sin(self.theta) * (self.velocity[0] + self.velocity[1]) * self.alpha
        self.theta += (self.velocity[0] - self.velocity[1]) * self.beta
        self.theta %= 2 * math.pi

    def drawRobot(self):
        a = [int(self.position[0] + (math.hypot(self.dimensions[0]/2, self.dimensions[1]/2) * math.cos(self.theta + (1*math.pi/4)))),
            int(self.position[1] + (math.hypot(self.dimensions[0]/2, self.dimensions[1]/2) * math.sin(self.theta + (1*math.pi/4))))]
        b = [int(self.position[0] + (math.hypot(self.dimensions[0]/2, self.dimensions[1]/2) * math.cos(self.theta + (3*math.pi/4)))),
            int(self.position[1] + (math.hypot(self.dimensions[0]/2, self.dimensions[1]/2) * math.sin(self.theta + (3*math.pi/4))))]
        c = [int(self.position[0] + (math.hypot(self.dimensions[0]/2, self.dimensions[1]/2) * math.cos(self.theta + (5*math.pi/4)))),
            int(self.position[1] + (math.hypot(self.dimensions[0]/2, self.dimensions[1]/2) * math.sin(self.theta + (5*math.pi/4))))]
        d = [int(self.position[0] + (math.hypot(self.dimensions[0]/2, self.dimensions[1]/2) * math.cos(self.theta + (7*math.pi/4)))),
            int(self.position[1] + (math.hypot(self.dimensions[0]/2, self.dimensions[1]/2) * math.sin(self.theta + (7*math.pi/4))))]

        return [a, b, c, d]

    def drawVelocity(self):
        a = [int(self.position[0] + (math.hypot(self.dimensions[0]/2, self.dimensions[1]/2) * math.cos(self.theta + (7*math.pi/4)))),
            int(self.position[1] + (math.hypot(self.dimensions[0]/2, self.dimensions[1]/2) * math.sin(self.theta + (7*math.pi/4))))]
        b = [a[0] + (math.cos(self.theta) * self.velocity[0] * self.delta),
            a[1] + (math.sin(self.theta) * self.velocity[0] * self.delta)]

        c = [int(self.position[0] + (math.hypot(self.dimensions[0]/2, self.dimensions[1]/2) * math.cos(self.theta + (1*math.pi/4)))),
            int(self.position[1] + (math.hypot(self.dimensions[0]/2, self.dimensions[1]/2) * math.sin(self.theta + (1*math.pi/4))))]
        d = [c[0] + (math.cos(self.theta) * self.velocity[1] * self.delta),
            c[1] + (math.sin(self.theta) * self.velocity[1] * self.delta)]

        return [[a, b], [c, d]]
