# KidsCanCode - Game Development with Pygame video series
# Shmup game - part 1
# Video link: https://www.youtube.com/watch?v=nGufy7weyGY
# Player sprite and movement
# https://stackoverflow.com/questions/29873814/pygame-mouse-get-pos-the-x-y-co-oridinates-not-updating


import pygame
import math
import random
import colors

army_size = 4               # probably the same
army_speed = 5           # different for different level of army
army_radius = 5   # army will stop moving when it's this close to the pointer
army_number = 100
army_health = 3
damage = 1  # for now



class Army(pygame.sprite.Sprite):
    def __init__(self, startingX, startingY, army_size, army_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((army_size, army_size))
        self.image.fill(colors.blue)
        self.rect = self.image.get_rect()
        self.rect.centerx = startingX
        self.rect.bottom = startingY
        self.speedx = 0
        self.speedy = 0
        self.army_health = army_health
        self.army_speed = army_speed

    def update(self, WIDTH, HEIGHT):
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


    def collide(self, damage):
        self.army_health -= damage
        if self.army_health == 0:
            del self
        else :
            self.speedy = - self.speedy
            self.speedx = - self.speedx

        # if edge collision with other army, stop.
