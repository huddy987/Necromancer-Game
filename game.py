import sys, pygame
import colors
width = 500
height = 400

display = pygame.display.set_mode([width, height])
# TODO: make this an appropriate name
pygame.display.set_caption("Hackathon game")
display.fill(colors.black)
pygame.display.update()

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
