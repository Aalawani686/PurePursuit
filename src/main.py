from PathFollowing import PathFollowing
from PathGeneration import PathGeneration
from Render import Render
import math
import numpy

debug = False
basePath = [[300, 350, 280, 25], [80, 20, -70, 40]]
spacing = 15

pathGen = PathGeneration(basePath)
pathGen.injectPath(spacing)
pathGen.smoothPath(0.3, 0.7, 0.01)
pathGen.radiusPath()
pathGen.velocityPath(40, 5, 1)
pathGen.trapezoidedVelocity()

pathFol = PathFollowing(pathGen.smoothed)
#pathFol.lookahead([0, 0], [2, 1], [5, 7], 7)

if(debug):
    renderDebug = Render()

    renderDebug.drawSubplot(pathGen.base, 1, "Base Path", "scatter",
        [0, 250], [-100, 100])
    renderDebug.drawSubplot(pathGen.injected, 3, "Injected Path", "connect",
        [0, 250], [-100, 100])
    renderDebug.drawSubplot(pathGen.smoothed, 5, "Smoothed Path", "connect",
        [0, 250], [-100, 100])

    renderDebug.drawSubplot([range(len(pathGen.pathR)), pathGen.pathR],
        2, "Path Radius", "scatter", [0 - 1, len(pathGen.pathR)], [1, pathGen.maxR],
        [0, len(pathGen.pathR)-1], True)
    renderDebug.drawSubplot([range(len(pathGen.pathV)), pathGen.pathV],
        4, "Path Velocity", "plot", [0 - 1, len(pathGen.pathV)],
        [min(pathGen.pathV), max(pathGen.pathV) + 10], [0, len(pathGen.pathV)-1])
    renderDebug.drawSubplot(pathGen.pathTV, 6, "Trapezoided Path Velocity", "plot",
        [0 - 1, len(pathGen.pathV)], [min(pathGen.pathV), max(pathGen.pathV) + 10],
        [0, len(pathGen.pathV)-1])
    renderDebug.show()

render = Render(1, 1)
render.drawSubplot(pathGen.smoothed, 1, "Path", "connect", [0, 400], [-100, 100])
render.drawSubplot(pathFol.drawRobot(), 1, "Path", "plot", [0, 400], [-100, 100])
render.show()
