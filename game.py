import pygame, colors, player, army, enemy, math, text

def main():
    # Global variables
    WIDTH = 800
    HEIGHT = 600
    FPS = 60

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    all_players = pygame.sprite.Group()
    player1 = player.Player(WIDTH / 2, HEIGHT / 2, 40, 50)
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

        if player1.health != 0:
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


            # Every 60 frames (every second) increment the score by 1
            player1.score += (1 / 60)

            # Update score
            text.draw_score(screen, player1.score, WIDTH)

        # If the player has died, show the score and lose message
        if player1.health == 0:
            screen.fill(colors.red)
            text.draw_final_score(screen, player1.score, WIDTH, HEIGHT)
            text.draw_final_message(screen, WIDTH, HEIGHT)

        # *after* drawing everything, flip the display
        pygame.display.flip()

    pygame.quit()

if __name__=="__main__":
    main()
