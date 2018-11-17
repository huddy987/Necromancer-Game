
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
        while running:
            rectangle = pygame.draw.rect(screen, colors.green, [position_x,position_y, size_x, size_y])
            pygame.display.update()
            screen.fill(colors.black)
            position_x += velocity_x
            position_y += velocity_y

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        if (position_y <= 0):
                            velocity_y = 0
                        else:
                            velocity_y = -1
                    if event.key == pygame.K_s:
                        if (position_y >= height):
                            velocity_y = 0
                        else:
                            velocity_y = 1
                    if event.key == pygame.K_a:
                        if (position_x <= 0):
                            velocity_x = 0
                        else:
                            velocity_x = -1
                    if event.key == pygame.K_d:
                        if (position_x >= height):
                            velocity_x = 0
                        else:
                            velocity_x = 1
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
