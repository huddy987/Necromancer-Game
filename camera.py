import pygame
import player

class Camera:
    def __init__(self, CameraX, CameraY):
        self.x = CameraX
        self.y = CameraY

    def update(self, player, WIDTH, HEIGHT):
        self.x -= player.speedx * 4
        self.y -= player.speedy * 4
        if self.x > 0:
            self.x = 0
        if self.y > 0:
            self.y = 0
        if self.x < -WIDTH:
            self.x =  -WIDTH
        if self.y < -HEIGHT:
            self.y = -HEIGHT
