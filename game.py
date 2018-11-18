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

# this deals with the army touching the enemy
def collisions(all_enemies, all_armies, player1, all_graves, all_bullets):

    army_collide_dict = pygame.sprite.groupcollide(all_armies,all_enemies, False, False)
    if army_collide_dict:       # key is the army, value is the enemy list
        all_enemies_collided = army_collide_dict.keys()
        for arma in all_enemies_collided:      # get the death here
            arma.collide(all_armies)
            for emma in army_collide_dict[arma]:
                grave = emma.collide(all_enemies) # collide(enemy)
                if grave != 0:
                  all_graves.add(grave)

    # This deals with the bullets (from the wizard) hitting the
    bullets_collide_dict = pygame.sprite.groupcollide(all_bullets,all_enemies, False, False)
    if bullets_collide_dict:       # key is the army, value is the enemy list
        all_bullets_collided = bullets_collide_dict.keys()
        for arma in all_bullets_collided:      # get the death here
            arma.collide(all_bullets)
            for emma in bullets_collide_dict[arma]:
                grave = emma.collide(all_enemies) # collide(enemy)
                if grave != 0:
                  all_graves.add(grave)

def grave_touching(player1, all_graves, all_armies, grave_counter):
        # if the player sprite collides with the graveyard sprite, instantiate an army, add it the army group then kill
        grave_touch = pygame.sprite.spritecollideany(player1, all_graves)
        if grave_touch:
            if grave_counter != 0:
                grave_counter -= 1
            elif grave_counter == 0:
                new_army_guy = army.Army((grave_touch.rect.x) + 39, (grave_touch.rect.y) + 30, 40, grave_touch.speed)
                all_armies.add(new_army_guy)
                all_graves.remove(grave_touch)
                grave_counter = 120
        else:
            grave_counter = 120
        return grave_counter

def music():
    pygame.mixer.music.load("./soundtrack.wav")
    pygame.mixer.music.play(-1)

def updates(screen, all_enemies, all_players, all_armies, WIDTH, HEIGHT, background, player1, camera1, all_bullets, all_graves):

    camera1.update(player1, WIDTH, HEIGHT)
    screen.blit(background, (camera1.x, camera1.y))
    all_graves.draw(screen)
    all_players.draw(screen)
    all_enemies.draw(screen)
    all_armies.draw(screen)
    all_bullets.draw(screen)

    #Update
    all_graves.update(player1, camera1, WIDTH, HEIGHT, all_graves)
    all_players.update(WIDTH, HEIGHT)
    all_enemies.update(WIDTH, HEIGHT, player1)
    all_armies.update(WIDTH, HEIGHT)
    all_bullets.update(all_bullets, player1)

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

    grave_counter = 120

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    background = pygame.image.load("Background.png")
    clock = pygame.time.Clock()

    all_players = pygame.sprite.Group()

    player1 = player.Player(WIDTH / 2, HEIGHT / 2, PLAYER_SIZE, PLAYER_SPEED, PLAYER_HEALTH)
    all_armies = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    armies = army.Army(200, 400, 40, 5)
    camera1 = camera.Camera(WIDTH/2, HEIGHT/2)

    all_players.add(player1)
    all_armies.add(armies)

    all_enemies = pygame.sprite.Group()

    all_graves = pygame.sprite.Group()

    music()

    running = True
    while running:
        # keep loop running at the right speed
        clock.tick(FPS)
        ktime += 1
        # Detect Collisions,
        collisions(all_enemies, all_armies, player1, all_graves, all_bullets)
        #Detect grave touching
        grave_counter = grave_touching(player1, all_graves, all_armies, grave_counter)
        # Process exit event
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        if player1.health != 0:

            # Draw / render
            screen.fill(colors.black)
            updates(screen, all_enemies, all_players, all_armies, WIDTH, HEIGHT, background, player1, camera1, all_bullets, all_graves)

            # Spawn enemies based on frequency
            if spawnEnemies(ktime, 500):
                # world size is window size * 2
                e = enemy.Enemy(random.randint(-WIDTH * 2, WIDTH * 2), random.randint(-HEIGHT * 2, HEIGHT * 2), 0, random.randint(2,5), 40)
                all_enemies.add(e)

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
