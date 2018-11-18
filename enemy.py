import pygame
import colors
import math

damage = 1

class Enemy(pygame.sprite.Sprite):
    # Spawn an enemy based on x, y, enemyType and enemy Speed
    # enemyType has no current use
    def __init__(self, x, y, enemyType, enemySpeed, enemySize):
        pygame.sprite.Sprite.__init__(self)
        # Initizalize enemy to be size of global ENEMY_SIZE
        self.image = pygame.Surface((enemySize, enemySize))
        self.image.fill(colors.red)
        self.rect = self.image.get_rect()
        self.speed = enemySpeed
        self.rect.x  = x
        self.rect.y = y
        self.enemyType = enemyType
        self.enemy_health = 2
        #self.speedx = 0        
        
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

    def kill(self, group):
        group.remove(self)

    def collide(self, group):
        self.enemy_health -= 1
        if self.enemy_health == 0:
            self.kill(group)
        