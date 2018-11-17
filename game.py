
import pygame
import colors

def main():
        # Global variables
        width = 800
        height = 600


        # Initialize Pygame
        pygame.init()
        pygame.display.set_caption("bruh")
        screen = pygame.display.set_mode((width, height))
        screen.fill(colors.black)
        pygame.display.update()

        # Define the gameplay loop
        running = True
        position_x = 100
        position_y = 100
        size_x = 10
        size_y = 10
        velocity_x = 0
        velocity_y = 0
        w_flag = 0
        a_flag = 0
        s_flag = 0
        d_flag = 0
        while running:
            rect = pygame.draw.rect(screen, colors.green, [position_x,position_y, size_x, size_y])
            pygame.display.update()
            screen.fill(colors.black)
            position_x += velocity_x
            position_y += velocity_y

            # Edge collision

            # D case
            if (position_x + size_x >= width):
                if velocity_x > 1:
                    velocity_x = 0
                    d_flag = 1
            # A case
            elif (position_x <= 0):
                if velocity_x < 1:
                    velocity_x = 0
                    a_flag = 1
            # S case
            if (position_y + size_y >= height):
                if velocity_y > 1:
                    velocity_y = 0
                    s_flag = 1
            #W case
            elif (position_y <= 0):
                if velocity_y < 1:
                    velocity_y = 0
                    w_flag = 1

            print(s_flag)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and w_flag == 0:
                        velocity_y = -5
                        s_flag = 0
                    if event.key == pygame.K_s and s_flag == 0:
                        velocity_y = 5
                        w_flag = 0
                    if event.key == pygame.K_a and a_flag == 0:
                        velocity_x = -5
                        d_flag = 0
                    if event.key == pygame.K_d and d_flag == 0:
                        velocity_x = 5
                        a_flag = 0
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        velocity_y = 0
                    if event.key == pygame.K_s:
                        velocity_y = 0
                    if event.key == pygame.K_a:
                        velocity_x = 0
                    if event.key == pygame.K_d:
                        velocity_x = 0

                if event.type == pygame.QUIT:
                    running = False

if __name__=="__main__":
    main()
