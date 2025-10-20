import pygame
import sys
from spriteclasses import Mushroom, Frog

pygame.init()

# Screen setup
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mushroom Game")
clock = pygame.time.Clock()

# Game loop
frog=Frog(1440,300)
mushroom = Mushroom(WIDTH, HEIGHT)
mushroom.rect.center = (620,150)
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mushroom.update()

    background = pygame.transform.scale(pygame.image.load("background.png"), (1920, 1080))
    screen.blit(background, (0, 0))
    mushroom.draw(screen)
    frog.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()