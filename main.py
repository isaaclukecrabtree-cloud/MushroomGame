import pygame
import sys
from sprites import Frog, Pond, Grass, Tree
from player import Mushroom

pygame.init()

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mushroom Game")
clock = pygame.time.Clock()

background = pygame.transform.scale(pygame.image.load("background.png").convert(), (WIDTH, HEIGHT))
pond = Pond(1025,50 )
frog = Frog(1360, 180)
tree1 = Tree(1, 100)
tree2 = Tree(800, 400)
tree3 = Tree(1200, 700)
tree4 = Tree(1, 600)
mushroom = Mushroom(WIDTH, HEIGHT)
mushroom.rect.center = (300, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mushroom.update(walls=[pond])

    screen.blit(background, (0, 0))
    pond.draw(screen)
    tree1.draw(screen)
    tree2.draw(screen)
    tree3.draw(screen)
    tree4.draw(screen)
    frog.draw(screen)
    mushroom.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()