# KidsCanCode - Game Development with Pygame video series
# Shmup game - part 1
# Video link: https://www.youtube.com/watch?v=nGufy7weyGY
# Player sprite and movement
# https://stackoverflow.com/questions/29873814/pygame-mouse-get-pos-the-x-y-co-oridinates-not-updating

"""
to instantiate an army object:
 >>> army = Army()
has to be added to all armies by
>>> all_armies.add(army)
>> all_armies.update()
>> all_armies.draw(screen)
"""

import pygame
import math
import random

WIDTH = 480
HEIGHT = 600
FPS = 60

army_size = 4               # probably the same
army_speed = 5           # different for different level of army
army_colour = (0, 0, 255)  # BLUE
army_radius = 40    # army will stop moving when it's this close to the pointer
army_number = 100

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()

class Army(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((army_size, army_size))
        self.image.fill(army_colour)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        # the army will follow the mouse pointer
        self.speedx = 0
        self.speedy = 0
        x_mouse, y_mouse = pygame.mouse.get_pos()
        keystate = pygame.key.get_pressed()
        x_distance = - ( ( self.rect.x ) - ( x_mouse ) )
        y_distance = - ( ( self.rect.y ) - ( y_mouse ) )
        theta = math.atan2(y_distance, x_distance)

        self.speedx = (army_speed)*(math.cos(theta))
        self.speedy = (army_speed)*(math.sin(theta))
        if abs((self.rect.x) - (x_mouse)) < army_radius:
            self.speedx = 0
        if abs((self.rect.y) - (y_mouse)) < army_radius:
            self.speedy = 0  # glitches otherwise


        # Not 100% accuracy
        if (random.random()) > 0.75:
            self.speedx = 0
            self.speedy = 0

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # stops the box at the edge of the screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

        # if edge collision with other army, stop.
