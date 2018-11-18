import pygame
import player

class Camera:
    def __init__(self, CameraX, CameraY):
        self.x = CameraX
        self.y = CameraY

    def update(self, player_x, player_y):
        self.x -= player_x * 4
        self.y -= player_y * 4
        if self.x > 0:
            self.x = 0
        if self.y > 0:
            self.y = 0
        if self.x < -800:
            self.x =  -800
        if self.y < -600:
            self.y = -600
