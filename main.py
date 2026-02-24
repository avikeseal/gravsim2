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

#this class represents each object in the simulation
#introducing object variable to the display output:
class Body:
    def __init__(self, x, y, mass, radius, color):
        self.pos = [x, y]
        self.vel = [0, 0]
        self.mass = mass
        self.radius = radius
        self.color = color
        self.path = []
    
    #apply gravity method to calculate force between objects:
    def apply_gravity(self, other):
        dx = other.pos[0] - self.pos[0]
        dy = other.pos[1] - self.pos[1]
        distance = math.sqrt((dx**2) + (dy**2))

        if distance > 0:
            force = (G * self.mass * other.mass)/(distance**2)
            angle = math.atan2(dy, dx)
            force_x = force * math.cos(angle)
            force_y = force * math.sin(angle)

            self.vel[0] += force_x / self.mass
            self.vel[1] += force_y / self.mass
    
    #update position method updates pos based on velocity:
    def update_position(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.path.append((int(self.pos[0]), int(self.pos[1])))

        #remove old path to free up memory:
        if len(self.path) > MAX_PATH_LENGTH:
            self.path.pop(0)

    #draw method handles drawing the object:
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.radius)
        if len(self.path) > 1:
            pygame.draw.lines(screen, YELLOW, False, self.path, 2)


#main game loop variable:
running = True

#main game loop:
while running:
	#A. handle events such as mouse clicks, keyboard press, widndow close etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #exit the loop if the user closes the windo)
