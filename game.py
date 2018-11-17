import pygame
import colors
import player

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
        clock = pygame.time.Clock()

        #initialize Player
        character = player.Player([100, 100], 5, [10, 10])

        # Define the gameplay loop
        running = True
        while running:
            screen.fill(colors.black)

            # check player/wall collision
            character.check_edge_collision(width, height)

            # update player velocity
            character.update_velocity()

            # move player
            character.move()

            # draw the player
            character.draw(screen)

            # check for input events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()

if __name__=="__main__":
    main()
