import pygame
import colors
import bullet

class Player(pygame.sprite.Sprite):

    def __init__(self, startingX, startingY, playerSize, playerSpeed, starting_health):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((playerSize, playerSize))
        self.size = playerSize
        self.image.fill(colors.green)
        self.rect = self.image.get_rect()
        self.rect.centerx  = startingX
        self.rect.bottom = startingY
        self.speedx = 0
        self.speedy = 0
        self.health = starting_health
        self.score = 0
        self.playerSpeed = playerSpeed
        self.bullet_cooldown = 0

    def update(self, WIDTH, HEIGHT):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_a]:
            self.speedx = -1 * self.playerSpeed
        if keystate[pygame.K_d]:
            self.speedx = self.playerSpeed
        if keystate[pygame.K_w]:
            self.speedy = -1 * self.playerSpeed
        if keystate[pygame.K_s]:
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
        self.score += (1 / 60)

        # decrement the bullet cooldown so we can shoot again
        if self.bullet_cooldown != 0:
            self.bullet_cooldown -= 1

    def check_shoot(self, cooldown):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE] and (self.speedx != 0 or self.speedy !=0) and (self.bullet_cooldown == 0):
            self.bullet_cooldown = cooldown
            return True
