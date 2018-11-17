import pygame
import colors
import player
import army
import enemy

def main():
    # Global variables
    WIDTH = 800
    HEIGHT = 600
    FPS = 30

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    all_players = pygame.sprite.Group()
    player1 = player.Player(400, 300, 40)
    all_enemies = pygame.sprite.Group()
    enemy1 = enemy.Enemy(200, 200, 0, 2, 40)
    enemy2 = enemy.Enemy(10, 10, 0, 3, 40)
    all_armies = pygame.sprite.Group()
    armies = army.Army(200, 400, 40, 5)

    #all_sprites = pygame.sprite.Group()
    all_players.add(player1)
    all_enemies.add(enemy1)
    all_enemies.add(enemy2)
    all_armies.add(armies)

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
        all_players.update(WIDTH, HEIGHT)
        all_enemies.update(WIDTH, HEIGHT, player1)
        all_armies.update(WIDTH, HEIGHT)

        # Draw / render
        screen.fill(colors.black)
        #all_sprites.draw(screen)
        all_players.draw(screen)
        all_enemies.draw(screen)
        all_armies.draw(screen)

        # *after* drawing everything, flip the display
        pygame.display.flip()

    pygame.quit()

if __name__=="__main__":
    main()
