import pygame

class Mushroom(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.frames = [pygame.transform.scale(pygame.image.load(f"mushwalk{i}.png").convert_alpha(), (100, 100)) for i in range(1, 5)]
        self.current_frame = 0
        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=(width // 2, height // 2))
        self.speed = 5
        self.facing_left = False
        self.animation_counter = 0
        self.screen_rect = pygame.Rect(0, 0, width, height)

    def update(self, walls=[]):
        keys = pygame.key.get_pressed()
        moving = any([keys[pygame.K_w], keys[pygame.K_s], keys[pygame.K_a], keys[pygame.K_d]])
        old_x, old_y = self.rect.x, self.rect.y

        if keys[pygame.K_w]: self.rect.y -= self.speed
        if keys[pygame.K_s]: self.rect.y += self.speed
        if keys[pygame.K_a]: self.rect.x -= self.speed; self.facing_left = True
        if keys[pygame.K_d]: self.rect.x += self.speed; self.facing_left = False

        for wall in walls:
            offset = (self.rect.x - wall.rect.x, self.rect.y - wall.rect.y)
            if wall.mask.overlap(pygame.mask.from_surface(self.image), offset):
                self.rect.x, self.rect.y = old_x, old_y
                break

        if moving:
            self.animation_counter += 1
            if self.animation_counter >= 5:
                self.current_frame = (self.current_frame + 1) % 4
                self.animation_counter = 0
        else:
            self.current_frame = 2

        self.image = pygame.transform.flip(self.frames[self.current_frame], self.facing_left, False)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.clamp_ip(self.screen_rect)

    def draw(self, surface):
        surface.blit(self.image, self.rect)