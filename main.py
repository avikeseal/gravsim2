#!usr/bin/env bash python3

import pygame 
import math
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

#screen dimensions:
WIDTH, HEIGHT = 1300, 1000
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GRAVITY SIMULATION II")

#create a clock object to control the frame rate:
clock = pygame.time.Clock()
FPS = 60

#initializing pygame:
pygame.init()
pygame.font.init()

#colors:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (135, 206, 250)
YELLOW = (255, 255, 0)

#gravitational constant:
G = 13

#storage cap on max pos and vel values:
MAX_PATH_LENGTH = 500
MAX_V_LENGTH = 500


#introducing object variable to the display output:
class Skull(pygame.sprite.Sprite):
    """
    represents the player object in the game.
    Inherits from pygame.sprite.Sprite for easier management.

    """
    def __init__(self):
        super().__init__()
        #load the image for the object:

#main game loop variable:
running = True

#main game loop:
while running:
	#A. handle events such as mouse clicks, keyboard press, widndow close etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #exit the loop if the user closes the windo)
