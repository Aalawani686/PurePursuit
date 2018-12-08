#from PathFollowing import PathFollowing
from PathGeneration import PathGeneration
from Render import Render
import math

debug = True
basePath = [[140, 175, 130, 25], [80, 20, -70, 40]]
spacing = 15

if(debug):
    render = Render()

pathGen = PathGeneration(basePath)
pathGen.injectPath(spacing)
pathGen.smoothPath(0.3, 0.7, 0.01)
pathGen.radiusPath()
pathGen.velocityPath(40, 5, 1)
pathGen.trapezoidedVelocity()

if(debug):
    render.drawSubplot(pathGen.base, 1, "Base Path", "scatter",
        [0, 250], [-100, 100])
    render.drawSubplot(pathGen.injected, 4, "Injected Path", "scatter",
        [0, 250], [-100, 100])
    render.drawSubplot(pathGen.smoothed, 7, "Smoothed Path", "scatter",
        [0, 250], [-100, 100])

    render.drawSubplot([range(len(pathGen.pathR)), pathGen.pathR],
        2, "Path Radius", "scatter", [0 - 1, len(pathGen.pathR)], [1, pathGen.maxR],
        [0, len(pathGen.pathR)-1], True)
    render.drawSubplot([range(len(pathGen.pathV)), pathGen.pathV],
        5, "Path Velocity", "plot", [0 - 1, len(pathGen.pathV)],
        [min(pathGen.pathV), max(pathGen.pathV) + 10], [0, len(pathGen.pathV)-1])
    render.drawSubplot(pathGen.pathTV, 8, "Trapezoided Path Velocity", "plot",
        [0 - 1, len(pathGen.pathV)], [min(pathGen.pathV), max(pathGen.pathV) + 10],
        [0, len(pathGen.pathV)-1])

    render.show()
