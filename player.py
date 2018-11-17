import pygame
import colors

class Player(pygame.sprite.Sprite):
    def __init__(self, startingX, startingY, playerSize):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((playerSize, playerSize))
        self.image.fill(colors.green)
        self.rect = self.image.get_rect()
        self.rect.centerx  = startingX
        self.rect.bottom = startingY
        self.speedx = 0
        self.speedy = 0
    
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
    """
    def __init__(self, position, max_vel, size):
        self._max_vel = max_vel
        # Position 0 is x coordinate, position 1 is y coordinate
        self._position = position

        # velocity 0 is x, velocity 1 is y (initally 0)
        self._velocity = [0, 0]

        # size 0 is x size, size 1 is y size
        self._size = size

        # keydown flags
        self._w_flag = 0
        self._a_flag = 0
        self._s_flag = 0
        self._d_flag = 0


    # draws self
    def draw(self, screen):
        pygame.draw.rect(screen, colors.green, [self._position[0],self._position[1], self._size[0], self._size[1]])

    def check_edge_collision(self, screen_width, screen_height):
        # D case
        if (self._position[0] + self._size[0] >= screen_width):
            if self._velocity[0] > 0:
                self._velocity[0] = 0
                self._d_flag = 1
        # A case
        elif (self._position[0] <= 0):
            if self._velocity[0] < 0:
                self._velocity[0] = 0
                self._a_flag = 1
        # S case
        if (self._position[1] + self._size[1] >= screen_height):
            if self._velocity[1] > 0:
                self._velocity[1] = 0
                self._s_flag = 1
        #W case
        elif (self._position[1] <= 0):
            if self._velocity[1] < 0:
                self._velocity[1] = 0
                self._w_flag = 1

    # updates velocity
    def update_velocity(self):
        self._velocity = [0, 0]
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w] and self._w_flag == 0:
            self._velocity[1] = -self._max_vel
            self._s_flag = 0
        if keystate[pygame.K_s] and self._s_flag == 0:
            self._velocity[1] = self._max_vel
            self._w_flag = 0
        if keystate[pygame.K_a] and self._a_flag == 0:
            self._velocity[0] = -self._max_vel
            self._d_flag = 0
        if keystate[pygame.K_d] and self._d_flag == 0:
            self._velocity[0] = self._max_vel
            self._a_flag = 0

    #updates movement
    def move(self):
        # update position
        self._position[0] += self._velocity[0]
        self._position[1] += self._velocity[1]
        """
