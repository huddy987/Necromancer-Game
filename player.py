import pygame
import colors

class Player(pygame.sprite.Sprite):
    def __init__(self, startingX, startingY, playerSize, starting_health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((playerSize, playerSize))
        self.image.fill(colors.green)
        self.rect = self.image.get_rect()
        self.rect.centerx  = startingX
        self.rect.bottom = startingY
        self.speedx = 0
        self.speedy = 0
        self.health = starting_health
        self.score = 0

    def update(self, WIDTH, HEIGHT):
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

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
