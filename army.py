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
        self.images = [pygame.image.load("./army_images/army0000.png"), pygame.image.load("./army_images/army0001.png"), pygame.image.load("./army_images/army0002.png")]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = startingX
        self.rect.bottom = startingY
        self.speedx = 0
        self.speedy = 0
        self.army_health = army_health
        self.army_speed = army_speed
        self.spritetimer = 0
        self.offsetx = random.uniform(-100,100)
        self.offsety = random.uniform(-100,100)

    def update(self, WIDTH, HEIGHT):
        # the army will follow the mouse pointer
        self.speedx = 0
        self.speedy = 0
        x_mouse, y_mouse = pygame.mouse.get_pos()
        keystate = pygame.key.get_pressed()
        x_distance = - ( (self.rect.x) - (x_mouse - self.offsetx) )
        y_distance = - ( (self.rect.y) - (y_mouse - self.offsety) )
        theta = math.atan2(y_distance, x_distance)

        self.speedx = (army_speed)*(math.cos(theta))
        self.speedy = (army_speed)*(math.sin(theta))

        # just stops it when it gets too close to the cursor
        if abs((self.rect.x) - (x_mouse - self.offsetx)) < army_radius:
            self.speedx = 0
        if abs((self.rect.y) - (y_mouse - self.offsety)) < army_radius:
            self.speedy = 0  # glitches otherwise


        # Not 100% accuracy
        if (random.random()) > 0.9:
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

        # Update sprite image
        if self.speedx != 0 or self.speedy != 0:
            if self.spritetimer == 30:
                self.image = self.images[2]
                self.spritetimer = 0
            elif self.spritetimer == 20:
                self.image = self.images[1]
            elif self.spritetimer == 10:
                self.image = self.images[0]
            self.spritetimer += 1

    def kill(self, group):
        group.remove(self)

    def collide(self, group):
        self.army_health -= 1
        if self.army_health == 0:
            self.kill(group)

        # if edge collision with other army, stop.
