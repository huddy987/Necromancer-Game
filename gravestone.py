import pygame
import colors
import math

class GraveStone(pygame.sprite.Sprite):
    def __init__(self, x, y, graveSize):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((graveSize, graveSize))
        self.image.fill(colors.yellow)
        self.rect = self.image.get_rect()
        self.speed = 0
        self.rect.x  = x
        self.rect.y = y
        