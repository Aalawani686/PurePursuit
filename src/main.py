#from PathFollowing import PathFollowing
from PathGeneration import PathGeneration
from Render import Render

debug = True
basePath = [[50, 100, 160, 190], [20, -50, 20, -40]]
spacing = 15

if(debug):
    render = Render()

pathGen = PathGeneration(basePath)
pathGen.injectPath(spacing)
pathGen.smoothPath(0.6, 0.4, 0.01)
pathGen.radiusPath()

if(debug):
    render.drawSubplot(pathGen.base, 1, "Base Path", [0, 250], [-100, 100])
    render.drawSubplot(pathGen.injected, 4, "Injected Path", [0, 250], [-100, 100])
    render.drawSubplot(pathGen.smoothed, 7, "Smoothed Path", [0, 250], [-100, 100])
    render.show()
