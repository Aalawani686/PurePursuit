import matplotlib.pyplot as plt
import math
import copy

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x, y):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

def distanceForm(xi, yi, xii, yii):
    sq1 = (xi-xii)*(xi-xii)
    sq2 = (yi-yii)*(yi-yii)
    return math.sqrt(sq1 + sq2)

def smoothing(path, a, b, tolerance, length):
    newPath = copy.deepcopy(path)
    change = tolerance

    while(change >= tolerance):
        change = 0.0
        for i in range(1, length-1):
            for j in range(0, 2):
                # print(str(path[j][i]) + " " + str(newPath[j][i]))
                add = a * (path[j][i] - newPath[j][i])
                add2 = b * (newPath[j][i-1] + newPath[j][i+1] - (2.0 * newPath[j][i]))


                aux = newPath[j][i]
                newPath[j][i] += add
                newPath[j][i] += add2
                change += math.fabs(aux - newPath[j][i])


                # print(str(i)+" "+str(j)+" "+str(add)+" "+str(add2)+" "+str(change))

        # plt.scatter(array[0], array[1])

    return newPath

array = [0] * 2
array[0] = [0] * 50
array[1] = [0] * 50

spacing = 15
p1 = Point(0, 0)
p2 = Point(90, 0)
p3 = Point(130, -50)
p4 = Point(200, -60)
# start_point = 100

deltaY = p2.y - p1.y
deltaX = p2.x - p1.x
deltaYY = p3.y - p2.y
deltaXX = p3.x - p2.x
deltaYYY = p4.y - p3.y
deltaXXX = p4.x - p3.x

distance = distanceForm(p1.x, p1.y, p2.x, p2.y)
distance2 = distanceForm(p2.x, p2.y, p3.x, p3.y)
distance3 = distanceForm(p3.x, p3.y, p4.x, p4.y)

num_points_that_fit = (int)(math.ceil(distance / spacing))
num_points_that_fit2 = (int)(math.ceil(distance2 / spacing))
num_points_that_fit3 = (int)(math.ceil(distance3 / spacing))

# vector = vector.normalize() * spacing
X = (int)(deltaX/distance * spacing)
Y = (int)(deltaY/distance * spacing)
XX = (int)(deltaXX/distance2 * spacing)
YY = (int)(deltaYY/distance2 * spacing)
XXX = (int)(deltaXXX/distance3 * spacing)
YYY = (int)(deltaYYY/distance3 * spacing)

for i in range(0, num_points_that_fit):
    array[0][i] = (p1.x + X * i)
    array[1][i] = (p1.y + Y * i)

for i in range(0, num_points_that_fit2):
    array[0][num_points_that_fit + i] = (p2.x + XX * i)
    array[1][num_points_that_fit + i] = (p2.y + YY * i)

for i in range(0, num_points_that_fit3):
    array[0][num_points_that_fit2 + num_points_that_fit + i] = (p3.x + XXX * i)
    array[1][num_points_that_fit2 + num_points_that_fit + i] = (p3.y + YYY * i)

fig, ax = plt.subplots()
plt.xlim(0, 300)
plt.ylim(-100, 200)
fig2, ax2 = plt.subplots()
plt.xlim(0, 300)
plt.ylim(-100, 200)


# vector = end_point - start_point
#print(num_points_that_fit2+num_points_that_fit)

ax.scatter(array[0], array[1])
array = smoothing(array, .7, .3, 0.01, num_points_that_fit3 + num_points_that_fit2 + num_points_that_fit)
ax2.scatter(array[0], array[1])

distance = [0] * len(array[0])
for k in range (1, len(distance)):
    distance[k] = distance[k-1] + distanceForm((int)(array[0][k-1]), (int)(array[1][k-1]), (int)(array[0][k]), (int)(array[1][k]))
    if(k == len(distance)-1):
         break
    x1 = array[0][k-1]+0.00001
    x2 = array[0][k]
    x3 = array[0][k+1]
    y1 = array[1][k-1]
    y2 = array[1][k]+0.00001
    y3 = array[1][k+1]
    c1 = (x1*x1 + y1*y1 - x2*x2 - y2*y2)/(2*(x1 - x2))
    c2 = (y1-y2)/(x1-x2)
    b = (x2*x2 - 2*x2*c1 + y2*y2 - x3*x3 + 2*x3*c1 - y3*y3)/(2*(x3*c2 - y3 + y2 - x2*c2))
    a = c1 - c2*b
    r = math.sqrt((x1-a)**2 + (y1-b)**2)
    if(r<50):
        circle1 = plt.Circle((a, b), r, color='r')
        ax2.add_artist(circle1)
    print("Curvature: " + str(1/r) + "   Radius: " + str(r))
    # print("Distance of " + str(k) + ": " + str(distance[k]))

plt.show()
