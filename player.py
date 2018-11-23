import pygame
import colors
import bullet
import game

class Player(pygame.sprite.Sprite):

    def __init__(self, startingX, startingY, playerSize, playerSpeed, starting_health):

        pygame.sprite.Sprite.__init__(self)
        self.size = playerSize
        self.images = [pygame.image.load("player_images/player0000.png"), pygame.image.load("player_images/player0001.png"), pygame.image.load("player_images/player0002.png")]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.centerx  = startingX
        self.rect.bottom = startingY
        self.speedx = 0
        self.speedy = 0
        self.health = starting_health
        self.score = 0
        self.playerSpeed = playerSpeed
        self.bullet_cooldown = 0
        self.spritetimer = 0

    def update(self, WIDTH, HEIGHT, camera):
        # Update sprite if the chracter is moving
        if self.speedx != 0 or self.speedy != 0:
            if self.spritetimer == 90:
                self.image = self.images[2]
                self.spritetimer = 0
            elif self.spritetimer == 60:
                self.image = self.images[1]
            elif self.spritetimer == 30:
                self.image = self.images[0]
            self.spritetimer += 1

        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_a]:
            if camera.x == 0:
                self.speedx = -1 * self.playerSpeed * 4
            else:
                self.speedx = -1 * self.playerSpeed
        if keystate[pygame.K_d]:
            if camera.x == -WIDTH:
                self.speedx = self.playerSpeed * 4
            else:
                self.speedx = self.playerSpeed
        if keystate[pygame.K_w]:
            if camera.y == 0:
                self.speedy = -1 * self.playerSpeed * 4
            else:
                self.speedy = -1 * self.playerSpeed
        if keystate[pygame.K_s]:
            if camera.y == -HEIGHT:
                self.speedy = self.playerSpeed * 4
            else:
                self.speedy = self.playerSpeed

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

        # Every 60 frames (every second) increment the score by 1
        self.score += (1 / 30)

        # decrement the bullet cooldown so we can shoot again
        if self.bullet_cooldown != 0:
            self.bullet_cooldown -= 1

    def check_shoot(self, cooldown):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE] and (self.speedx != 0 or self.speedy !=0) and (self.bullet_cooldown == 0):
            self.bullet_cooldown = cooldown
            return True
