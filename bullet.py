import player
import colors
import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player, bullet_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((bullet_size, bullet_size))
        self.image.fill(colors.red)
        self.rect = self.image.get_rect()
        self.rect.centerx  = player.rect.x + player.size / 2
        self.rect.bottom = player.rect.y + player.size / 2
        self.speed = [0,0]
        self.speed[0] = player.speedx * 10
        self.speed[1] = player.speedy * 10

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def kill(self, group):
        group.remove(self)

    def collide(self, group):
        self.kill(group)