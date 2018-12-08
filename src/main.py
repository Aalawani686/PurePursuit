import matplotlib.pyplot as plt
#from PathFollowing import PathFollowing
from PathGeneration import PathGeneration


basePath = [[50, 100, 160, 190], [20, -50, 20, -40]]
spacing = 15

pathGen = PathGeneration(basePath)
pathGen.injectPath(spacing)

fig, ax = plt.subplots()
plt.xlim(0, 300)
plt.ylim(-100, 200)
ax.scatter(pathGen.injected[0], pathGen.injected[1])
plt.show()
#pathFol = PathFollowing()
