import pygame
import random

class Frog(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("frogstill.png").convert_alpha(), (250, 250))
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Pond(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("pond.png").convert_alpha(), (700, 400))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Tree(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        size = random.randint(100, 400)
        self.image = pygame.transform.scale(pygame.image.load("tree.png").convert_alpha(), (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.collision_rect = pygame.Rect(x + size // 3, y + 3 * size // 4, size // 3, size // 4)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Grass(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("windgrass1.png").convert_alpha(), (300, 300))
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)