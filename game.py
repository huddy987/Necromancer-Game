import pygame, colors, player, army, enemy, math, text, random, time, camera, bullet

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


def updates(screen, all_enemies, all_players, all_armies, WIDTH, HEIGHT, zoom, background, player1, camera1, all_bullets):

    camera1.update(player1.speedx, player1.speedy, zoom)
    screen.blit(background, (camera1.x, camera1.y))
    #all_sprites.draw(screen)
    all_players.draw(screen)
    all_enemies.draw(screen)
    all_armies.draw(screen)
    all_bullets.draw(screen)
    #Update
    all_players.update(WIDTH, HEIGHT)
    all_enemies.update(WIDTH, HEIGHT, player1)
    all_armies.update(WIDTH, HEIGHT)
    all_bullets.update()

    text.draw_score(screen, player1.score, WIDTH)
    text.draw_health(screen, player1.health, WIDTH)


def main():
    # Global variables
    WIDTH = 800
    HEIGHT = 600
    ktime = 0

    PLAYER_SIZE = 40
    PLAYER_SPEED = 2
    PLAYER_HEALTH = 5
    FPS = 60

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    background = pygame.image.load("Background.png")
    clock = pygame.time.Clock()

    all_players = pygame.sprite.Group()
    # FPS * 2 is the bullet cooldown (2 seconds)
    player1 = player.Player(WIDTH / 2, HEIGHT / 2, PLAYER_SIZE, PLAYER_SPEED, PLAYER_HEALTH)
    all_armies = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    armies = army.Army(200, 400, 40, 5)
    camera1 = camera.Camera(WIDTH/2, HEIGHT/2, 1)

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
                # world size is window size * 2
                e = enemy.Enemy(random.randint(-WIDTH * 2, WIDTH * 2), random.randint(-HEIGHT * 2, HEIGHT * 2), 0, random.randint(2,5), 40)
                all_enemies.add(e)

            screen.fill(colors.black)
            # Draw / render
            updates(screen, all_enemies, all_players, all_armies, WIDTH, HEIGHT, zoom, background, player1, camera1, all_bullets)

            text.draw_score(screen, player1.score, WIDTH)
            text.draw_health(screen, player1.health, WIDTH)

            # Draw bullets
            if player1.check_shoot(FPS * 2) == True:
                new_bullet = bullet.Bullet(player1, 10)
                all_bullets.add(new_bullet)

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
