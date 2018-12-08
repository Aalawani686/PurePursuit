import matplotlib.pyplot as plt
#from PathFollowing import PathFollowing
from PathGeneration import PathGeneration


debug = True

basePath = [[50, 100, 160, 190], [20, -50, 20, -40]]
spacing = 15

pathGen = PathGeneration(basePath)
pathGen.injectPath(spacing)
pathGen.smoothPath(0.6, 0.4, 0.01)
pathGen.radiusPath()

fig, ax = plt.subplots()
plt.xlim(0, 300)
plt.ylim(-100, 200)
ax.scatter(pathGen.smoothed[0], pathGen.smoothed[1])
plt.show()
#pathFol = PathFollowing()
