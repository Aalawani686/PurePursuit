import matplotlib.pyplot as plt
import math
import copy
import time
from matplotlib.animation import FuncAnimation
import calc

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

c = calc.Calc()
pointX = []
# X position at a point
pointY = []
# Y position at a point
pointR = []
# radius at a point
pointD = []
# point to a distance

segmentDis = []
# length of a segment

numSegments = 3

segments = [[0] for i in range(3)]
# 0 - X delta between points
# 1 - Y delta between points
# 2 - Number of points in segment

vector = [[0] for i in range(numSegments)]
# unit vector * spacing

spacing = 15
p1 = Point(90, 20)
p2 = Point(100, -50)
p3 = Point(160, 20)
p4 = Point(190, -40)

segments[1].append(p2.y - p1.y)
segments[0].append(p2.x - p1.x)
segments[1].append(p3.y - p2.y)
segments[0].append(p3.x - p2.x)
segments[1].append(p4.y - p3.y)
segments[0].append(p4.x - p3.x)

segmentDis.append(c.distanceForm(p1.x, p1.y, p2.x, p2.y))
segmentDis.append(c.distanceForm(p2.x, p2.y, p3.x, p3.y))
segmentDis.append(c.distanceForm(p3.x, p3.y, p4.x, p4.y))

for i in range(0, len(segments[0])):
    segments[2].append((int)(math.ceil(segmentDis[i] / spacing)))

for i in range(0, len(vector)):
    vector[i].append()

'''vector[0].append((int)(segments[0]/segmentDis[0] * spacing))
vector[1].append((int)(segments[0]/segmentDis[0] * spacing))
vector[0].append((int)(segments[1]/segmentDis[1] * spacing))
vector[1].append((int)(segments[1]/segmentDis[1] * spacing))
vector[0].append((int)(segments[2]/segmentDis[2] * spacing))
vector[1].append((int)(segments[2]/segmentDis[2] * spacing))


Y = (int)(deltaY/distance * spacing)
XX = (int)(deltaXX/distance2 * spacing)
YY = (int)(deltaYY/distance2 * spacing)
XXX = (int)(deltaXXX/distance3 * spacing)
YYY = (int)(deltaYYY/distance3 * spacing)'''
