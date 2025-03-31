import pygame
import os
import random
import math
from os import listdir
from os.path import isfile, join
pygame.init()

# Window settings
pygame.display.set_caption("Platformer")
WIDTH = 1000
HEIGHT = 800
BG_COLOR = (255, 255, 255)
window = pygame.display.set_mode((WIDTH,HEIGHT))

#Clock settings
clock = pygame.time.Clock()
FPS = 60

#Player settings
PLAYER_VEL = 5

def draw():
    """Drawing funcion"""
    pass


def main(window):
    
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)