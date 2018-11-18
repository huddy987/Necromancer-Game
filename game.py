import pygame, colors, player, army, enemy, math, text, random, time

def spawnEnemies(time, frequency):
    if (time % frequency) == 0:
        return True
    else:
        return False


def reset(player1, all_enemies, PLAYER_HEALTH, WIDTH, HEIGHT, screen):
    for i in all_enemies:
        all_enemies.remove(i)
    screen.fill(colors.red)
    text.draw_final_score(screen, player1.score, WIDTH, HEIGHT)
    text.draw_final_message(screen, WIDTH, HEIGHT)
    pygame.display.flip()
    player1.rect.x = WIDTH/2
    player1.rect.y = HEIGHT/2

def collisions(armies, all_enemies, player1):
    armyprotect = pygame.sprite.spritecollide(armies, all_enemies, False)
    if armyprotect:
        print(armyprotect)
    for deads in armyprotect:
        all_enemies.remove(deads)
    playerhit = pygame.sprite.spritecollide(player1, all_enemies, False)
    hits = 0
    for i in playerhit:
        hits += 1
    player1.health -= hits


def updates(screen, all_enemies, all_players, all_armies, WIDTH, HEIGHT, player1):
    #all_sprites.draw(screen)
    all_players.draw(screen)
    all_enemies.draw(screen)
    all_armies.draw(screen)
    #Update
    all_players.update(WIDTH, HEIGHT)
    all_enemies.update(WIDTH, HEIGHT, player1)
    all_armies.update(WIDTH, HEIGHT)


def main():
    # Global variables
    WIDTH = 800
    HEIGHT = 600
    ktime = 0

    PLAYER_SIZE = 40
    PLAYER_SPEED = 8
    PLAYER_HEALTH = 5
    FPS = 60

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    all_players = pygame.sprite.Group()
    player1 = player.Player(WIDTH / 2, HEIGHT / 2, PLAYER_SIZE, PLAYER_SPEED, PLAYER_HEALTH)
    all_armies = pygame.sprite.Group()
    armies = army.Army(200, 400, 40, 5)

    all_players.add(player1)
    all_armies.add(armies)

    all_enemies = pygame.sprite.Group()

    running = True
    while running:
        # keep loop running at the right speed
        clock.tick(FPS)
        ktime += 1
        # Detect Collisions,
        collisions(armies, all_enemies, player1)
        # Process exit event
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        if player1.health != 0:
            # Spawn enemies based on frequency
            if spawnEnemies(ktime, 100):
                e = enemy.Enemy(random.randint(0, WIDTH), random.randint(0, HEIGHT), 0, random.randint(2,5), 40)
                all_enemies.add(e)

            screen.fill(colors.black)
            # Draw / render
            updates(screen, all_enemies, all_players, all_armies, WIDTH, HEIGHT, player1)

            text.draw_score(screen, player1.score, WIDTH)
            text.draw_health(screen, player1.health, WIDTH)


            # Every 60 frames (every second) increment the score by 1
            player1.score += (1 / 60)

        # If the player has died, show the score and lose message
        if player1.health == 0:
            reset(player1, all_enemies, PLAYER_HEALTH, WIDTH, HEIGHT, screen)
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_SPACE]:
                player1.health = PLAYER_HEALTH
                player1.score = 0

        # *after* drawing everything, flip the display
        pygame.display.flip()

    pygame.quit()

if __name__=="__main__":
    main()
