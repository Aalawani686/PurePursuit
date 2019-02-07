import pygame
import tkinter as tk
from tkinter import *
import os

from Robot import Robot

class Simulator(object):
    lookahead = 200

    def __init__(self, x = 0, y = 0, theta = 0):
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)

        embed = tk.Frame(self.root, width = 1920, height = 1080) #creates embed frame for pygame window
        embed.grid(columnspan = (1920), rowspan = 1080) # Adds grid
        embed.pack(side = LEFT) #packs window to the left

        self.root.update()
        os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
        #os.environ['SDL_VIDEODRIVER'] = 'windib'

        self.screen = pygame.display.set_mode((1920,1080))
        self.screen.fill(pygame.Color(255,255,255))

        pygame.display.init()
        pygame.display.update()

        self.robot = Robot(x, y, theta)

        self.update([0, 0])

    def update(self, newVelocity = [0, 0]):
        self.robot.setVelocity(newVelocity)
        self.robot.update()

        self.screen.fill(pygame.Color(255,255,255))

        pygame.draw.polygon(self.screen, (0,0,0), self.robot.drawRobot(), 1)
        pygame.draw.line(self.screen, (255,0,0), self.robot.drawVelocity()[0][0], self.robot.drawVelocity()[0][1], 1)
        pygame.draw.line(self.screen, (0,255,0), self.robot.drawVelocity()[1][0], self.robot.drawVelocity()[1][1], 1)
        pygame.draw.circle(self.screen, (0,0,0), self.robot.getPosition(), self.lookahead, 1)

        pygame.display.update()
        self.root.update()

simulator = Simulator(1920/2, 1080/2, 0)

while True:
    simulator.update([1, 2])
