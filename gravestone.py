import pygame
import colors
import math

class GraveStone(pygame.sprite.Sprite):
    def __init__(self, x, y, graveSize, enemySpeed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./grave0000.png")
        self.rect = self.image.get_rect()
        self.speed = 0
        self.rect.x  = x
        self.rect.y = y
        self.speed = enemySpeed
        # lifespan is ((60 * 10) / 60) = 10 seconds
        self.lifespan = 600

    def update(self, player, camera, WIDTH, HEIGHT, group):
        if self.lifespan == 0:
            group.remove(self)
        if not (camera.x == 0 or camera.x == -WIDTH):
            self.rect.x -= player.speedx * 4

        if not (camera.y == 0  or camera.y == -HEIGHT):
            self.rect.y -= player.speedy * 4

        self.lifespan -= 1
