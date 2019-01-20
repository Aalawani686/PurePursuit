import matplotlib.pyplot as plt
import math
import copy
import time
from matplotlib.animation import FuncAnimation

class Calc:

    def distanceForm(self, xi, yi, xii, yii):
        sq1 = (xi-xii)*(xi-xii)
        sq2 = (yi-yii)*(yi-yii)
        return math.sqrt(sq1 + sq2)

    def delta(self, xi, xii):
        return xi-x

    def smoothing(self, path, a, b, tolerance, length):
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

        return newPath
