import pygame

class Mushroom(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.frames = [
            pygame.transform.scale(pygame.image.load("mushwalk1.png"), (100, 100)),
            pygame.transform.scale(pygame.image.load("mushwalk2.png"), (100, 100)),
            pygame.transform.scale(pygame.image.load("mushwalk3.png"), (100, 100)),
            pygame.transform.scale(pygame.image.load("mushwalk4.png"), (100, 100))
        ]
        self.current_frame = 0
        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=(width // 2, height // 2))
        self.speed = 5
        self.rotation = 270
        self.animation_counter = 0
        self.width = width
        self.height = height

    def update(self):
        keys = pygame.key.get_pressed()
        moving = False

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
            moving = True
        if keys[pygame.K_s]:
            self.rect.y += self.speed
            moving = True
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.rotation = 90
            moving = True
        if keys[pygame.K_d]:
            self.rect.x += self.speed
            self.rotation = 270
            moving = True

        if moving:
            self.animation_counter += 1
            if self.animation_counter >= 5:
                self.current_frame = (self.current_frame + 1) % 4
                self.animation_counter = 0
        else:
            self.current_frame = 2

        current_image = self.frames[self.current_frame]
        if self.rotation == 90:
            current_image = pygame.transform.flip(current_image, True, False)

        self.image = current_image
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.clamp_ip(pygame.Rect(0, 0, self.width, self.height))

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Frog(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.frames = [
            pygame.transform.scale(pygame.image.load("frogstill.png"), (250, 250)),
            pygame.transform.scale(pygame.image.load("frogswirl1.png"), (250, 250)),
            pygame.transform.scale(pygame.image.load("frogswirl2.png"), (250, 250)),
            pygame.transform.scale(pygame.image.load("frogswirl3.png"), (250, 250)),
        ]
        self.current_frame = 0
        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=(x, y))
        self.animation_counter = 0

    def update(self):
        self.animation_counter += 1
        if self.animation_counter >= 5:
            self.current_frame = (self.current_frame + 1) % 4
            self.animation_counter = 0
        self.image = self.frames[self.current_frame]

    def draw(self, surface):
        surface.blit(self.image, self.rect)