import pygame
import colors
import math

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, graveSize):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load("./powerup_images/power0000.png"), pygame.image.load("./powerup_images/power0001.png"), pygame.image.load("./powerup_images/power0002.png"), pygame.image.load("./powerup_images/power0003.png"), pygame.image.load("./powerup_images/power0004.png")]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.speed = 0
        self.rect.x  = x
        self.rect.y = y
        self.lifespan = 600
        self.spritetimer = 0

    def update(self, player, camera, WIDTH, HEIGHT, group):
        if self.spritetimer == 80:
            self.image = self.images[2]
            self.spritetimer = 0
        elif self.spritetimer == 60:
            self.image = self.images[1]
        elif self.spritetimer == 40:
            self.image = self.images[1]
        elif self.spritetimer == 20:
            self.image = self.images[0]
        self.spritetimer += 1

        if self.lifespan == 0:
            group.remove(self)
        if not (camera.x == 0 or camera.x == -WIDTH):
            self.rect.x -= player.speedx * 4

        if not (camera.y == 0  or camera.y == -HEIGHT):
            self.rect.y -= player.speedy * 4

        self.lifespan -= 1
