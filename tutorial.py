# Pygame template - skeleton for a new pygame project

import pygame
import random
import colors
import math

WIDTH = 480
HEIGHT = 600
FPS = 30
ENEMY_SIZE = 40

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx  = WIDTH / 2
        self.rect.bottom = HEIGHT / 2
        self.speedx = 0
        self.speedy = 0
    
    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -5
        if keystate[pygame.K_d]:
            self.speedx = 5
        if keystate[pygame.K_w]:
            self.speedy = -5 
        if keystate[pygame.K_s]:
            self.speedy = 5             
        self.rect.x += self.speedx
        self.rect.y += self.speedy

class Enemy(pygame.sprite.Sprite):
    # Spawn an enemy based on x, y
    def __init__(self, x, y, enemyType, enemySpeed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((ENEMY_SIZE, ENEMY_SIZE))
        self.image.fill(colors.red)
        self.rect = self.image.get_rect()
        self.speed = enemySpeed
        self.rect.x  = x
        self.rect.y = y
        self.enemyType = enemyType
        #self.speedx = 0        
        
#https://stackoverflow.com/questions/20044791/how-to-make-an-enemy-follow-the-player-in-pygame
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
    
    def update(self):
        #print(player.rect.x)
        #print(player.rect.y)
        self.followPlayer(player)

all_sprites = pygame.sprite.Group()
player = Player()
enemy = Enemy(200,200, 0, 2)
enemy2 = Enemy(10, 10, 0, 3)
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(enemy2)

# Game loop
running = True

while running:
    # keep loop running at the right speed
    clock.tick(FPS)

    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()