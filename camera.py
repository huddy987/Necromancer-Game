import pygame
import player

class Camera:
    def __init__(self, CameraX, CameraY):
        self.x = CameraX
        self.y = CameraY

    def update(self, player, HEIGHT, WIDTH):
        self.x -= player.speedx * 4
        self.y -= player.speedy * 4
        if self.x > 0:
            self.x = 0
        if self.y > 0:
            self.y = 0
        if self.x < -HEIGHT:
            self.x =  -HEIGHT
        if self.y < -WIDTH:
            self.y = -WIDTH
