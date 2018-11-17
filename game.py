
import pygame

def main():

        # Initialize Pygame
        pygame.init()
        pygame.display.set_caption("Necromancy")
        screen = pygame.display.set_mode((800,600))

        # Define the gameplay loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

if __name__=="__main__":
    main()