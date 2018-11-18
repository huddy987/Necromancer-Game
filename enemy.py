import pygame
import colors
import math
import gravestone

class Enemy(pygame.sprite.Sprite):
    # Spawn an enemy based on x, y, enemyType and enemy Speed
    # enemyType has no current use
    def __init__(self, x, y, enemyType, enemySpeed, enemySize):
        pygame.sprite.Sprite.__init__(self)
        # Initizalize enemy to be size of global ENEMY_SIZE
        self.images = [pygame.image.load("enemy_images/enemy0000.png"), pygame.image.load("enemy_images/enemy0001.png"), pygame.image.load("enemy_images/enemy0002.png")]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.speed = enemySpeed
        self.rect.x  = x
        self.rect.y = y
        self.enemyType = enemyType
        self.health = 2     # Change this to a passed value
        self.spritetimer = 0

    #https://stackoverflow.com/questions/20044791/how-to-make-an-enemy-follow-the-player-in-pygame

    # Allows the enemy to follow the player by calculating the
    # distnace vector between the enemy and the player and multiplying it by the speed of the enemy
    def followPlayer(self, player):
        dx = self.rect.x - player.rect.x
        dy = self.rect.y - player.rect.y
        distance = math.hypot(dx, dy)
        if distance != 0:
            xSpeed = dx/distance
            ySpeed = dy/distance
            self.rect.x -= xSpeed * self.speed
            self.rect.y -= ySpeed * self.speed
        else:
            self.rect.x += 0
            self.rect.y += 0

    def update(self, WIDTH, HEIGHT, player):
        self.followPlayer(player)
        if self.spritetimer == 90:
            self.image = self.images[2]
            self.spritetimer = 0
        elif self.spritetimer == 60:
            self.image = self.images[1]
        elif self.spritetimer == 30:
            self.image = self.images[0]
        self.spritetimer += 1
        self.followPlayer(player)

    def kill(self, player, group):
        grave = gravestone.GraveStone(self.rect.x, self.rect.y, 40, self.speed)
        group.remove(self)
        player.score += 2
        return grave

    def collide(self, player, group):
        self.health -= 1
        if self.health == 0:
            grave = self.kill(player, group)
            return grave
        else:
            return 0
