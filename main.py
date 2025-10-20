import pygame
from sprites import Frog, Pond, Tree
from player import Mushroom

pygame.init()

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

grass_tile = pygame.transform.scale(pygame.image.load("grass.png").convert(), (40, 40))
path_tile = pygame.transform.scale(pygame.image.load("path.png").convert(), (40, 40))
background = pygame.Surface((WIDTH, HEIGHT))
for x in range(0, WIDTH, 40):
    for y in range(0, HEIGHT, 40):
        background.blit(grass_tile, (x, y))

path_positions = [(280, 200), (300, 200), (340, 200)]  # Example path
for pos in path_positions:
    background.blit(path_tile, pos)

pond = Pond(1025, 50)
frog = Frog(1360, 180)
trees = [Tree(1, 100), Tree(800, 400), Tree(1200, 700), Tree(1, 600), Tree(620, 195), Tree(1670, 625)]
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