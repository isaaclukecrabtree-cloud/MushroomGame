import pygame
from sprites import Frog, Pond, Tree
from player import Mushroom

pygame.init()

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

background = pygame.transform.scale(pygame.image.load("background.png").convert(), (WIDTH, HEIGHT))
pond = Pond(1025, 50)
frog = Frog(1360, 180)
trees = [Tree(1, 100), Tree(800, 400), Tree(1200, 700), Tree(1, 600)]
mushroom = Mushroom(WIDTH, HEIGHT)
mushroom.rect.center = (300, 100)
walls = [pond] + trees

running = True
while running:
    if pygame.event.get(pygame.QUIT):
        running = False

    mushroom.update(walls=walls)

    screen.blit(background, (0, 0))
    pond.draw(screen)
    frog.draw(screen)
    mushroom.draw(screen)
    [tree.draw(screen) for tree in trees]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()