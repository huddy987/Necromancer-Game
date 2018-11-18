import pygame, colors

def draw_score(screen, player_score, screen_width):
    score_font = pygame.font.SysFont('Comic Sans MS', 25)
    score_message = score_font.render('Score: ' + str(round(player_score)), False, colors.white)
    score_width, score_height = score_font.size('Score: ' + str(round(player_score)))
    screen.blit(score_message, (screen_width - score_width - 5, 0))

def draw_health(screen, player_health, screen_width):
    health_font = pygame.font.SysFont('Comic Sans MS', 25)
    health_message = health_font.render('Health: ' + str(player_health), False, colors.white)
    health_width, health_height = health_font.size('Health: ' + str(player_health))
    screen.blit(health_message, (screen_width - health_width - 5, health_height))

def draw_final_score(screen, player_score, screen_width, screen_height):
    score_font = pygame.font.SysFont('Comic Sans MS', 50)
    score_message = score_font.render('Score: ' + str(round(player_score)), False, colors.black)
    score_width, score_height = score_font.size('Score: ' + str(round(player_score)))
    screen.blit(score_message, ((screen_width / 2) - (score_width / 2), (screen_height / 2) - (score_height)))

def draw_final_message(screen, screen_width, screen_height):
    # lose message
    lose_font = pygame.font.SysFont('Comic Sans MS', 100)
    lose_message = lose_font.render('You Lose!', False, (0, 0, 0))
    lose_width, lose_height = lose_font.size('You Lose!')
    screen.blit(lose_message, ((screen_width / 2) - (lose_width / 2), (lose_height / 2)))

    # replay message
    replay_font = pygame.font.SysFont('Comic Sans MS', 50)
    replay_message = replay_font.render('Press return to play again.', False, (0, 0, 0))
    replay_width, replay_height = replay_font.size('Press return to play again.')
    screen.blit(replay_message, ((screen_width / 2) - (replay_width / 2), (screen_height - 100)))
