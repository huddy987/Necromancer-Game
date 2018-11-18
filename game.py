import pygame
import colors
import player
import army
import enemy
import random

def spawnEnemies(time, frequency):
    if (time % frequency) == 0:
        return True
    else:
        return False

def main():  
    # Global variables
    WIDTH = 800
    HEIGHT = 600
    FPS = 30
    ktime = 0
    
    PLAYER_SIZE = 40
    PLAYER_SPEED = 8

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    all_players = pygame.sprite.Group()
    player1 = player.Player(400, 300, PLAYER_SIZE, PLAYER_SPEED)
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

        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
                
        # Spawn enemies based on frequency
        if spawnEnemies(ktime, 100):
            e = enemy.Enemy(random.randint(0, WIDTH), random.randint(0, HEIGHT), 0, random.randint(2,5), 40)
            all_enemies.add(e)  
    
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
