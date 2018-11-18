import player
import colors
import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player, bullet_size):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load("./bullet_images/bullet0000.png"), pygame.image.load("./bullet_images/bullet0000.png"), pygame.image.load("./bullet_images/bullet0001.png"), pygame.image.load("./bullet_images/bullet0002.png"), pygame.image.load("./bullet_images/bullet0003.png"), pygame.image.load("./bullet_images/bullet0004.png"), pygame.image.load("./bullet_images/bullet0005.png")]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.centerx  = player.rect.x + player.size / 2
        self.rect.bottom = player.rect.y + player.size / 2
        self.speed = [0,0]
        self.speed[0] = player.speedx * 5
        self.speed[1] = player.speedy * 5
        # Lifetime in frames = 2 seconds
        self.lifetime = 120
        self.spritetimer = 0


    def kill(self, group):
        group.remove(self)

    def collide(self, group):
        self.kill(group)

    def update(self, group, player):
        self.rect.x += (self.speed[0] - player.speedx)
        self.rect.y += (self.speed[1] - player.speedy)
        self.lifetime -= 1
        if (self.lifetime == 0):
            self.kill(group)

        if self.spritetimer == 30:
            self.image = self.images[5]
            self.spritetimer = 0
        elif self.spritetimer == 25:
            self.image = self.images[4]
        elif self.spritetimer == 20:
            self.image = self.images[3]
        elif self.spritetimer == 15:
            self.image = self.images[2]
        elif self.spritetimer == 10:
            self.image = self.images[1]
        elif self.spritetimer == 5:
            self.image = self.images[0]
        self.spritetimer += 1
