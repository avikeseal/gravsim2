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
screen = pygame.display.set_mode()
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

#bodies:
BODIES = {
        "Moon": {"mass":100, "radius":15, "color": (200, 200, 200)},
            "Earth": {"mass":1000, "radius":25, "color": (50, 100, 255)},
            "Jupiter": {"mass":10000, "radius":45, "color": (255, 180, 100)},
            "Neutron Star": {"mass":500000, "radius":12, "color": (180, 0, 255)},
            "Black Hole": {"mass":9999999, "radius":8, "color": (10, 10, 10)},
         }


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

#selection screen:

#takes the pygame screen to draw on and prompt string so you can reuse the same function twice
def selection_screen(screen, prompt):
    screen.fill((0, 0, 0))  
    font = pygame.font.SysFont(None, 48)
    title = font.render(prompt, True, (255, 255, 255))
    screen.blit(title, (100, 50))

    small_font = pygame.font.SysFont(None, 36)
    #drawing options
    #pulls the name out of the dict and loops thru them to render each one 
    #on screen with a number next to it.
    #enumerate gives us both value and index at the same time
    bodies_list = list(BODIES.keys())
    for i, name in enumerate(bodies_list):
        text = small_font.render(f"{i+1}. {name}", True, (200, 200, 200))
        screen.blit(text, (100, 150 + i * 50))

    pygame.display.flip()


    #listen for keypress:
    #waiting loop - listens for a user key press
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #keypress detection:
                #subtraction converts the keycode into an actual index:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    index = event.key - pygame.K_1
                    if index < len(bodies_list):
                        #once a valid key key is pressed the function 
                        #returns the names of the two chosen bodies
                        return bodies_list[index]

pygame.init()
screen = pygame.display.set_mode()

#selection process:
choice1 = selection_screen(screen, "Select Body 1:")
choice2 = selection_screen(screen, "Select Body 2:")

body1 = Body(x=300, y=400, **BODIES[choice1])
body2 = Body(x=600, y=400, **BODIES[choice2])

#main game loop variable:
running = True

#main game loop:
while running:
	#A. handle events such as mouse clicks, keyboard press, widndow close etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #exit the loop if the user closes the windo)
