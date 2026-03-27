import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.pos = pygame.math.Vector2(x, y)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 250.0

        # Placeholder image: a red rectangle
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=self.pos)

    def update(self, dt):
        self.direction = pygame.math.Vector2(0, 0)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y -= 1
        if keys[pygame.K_s]:
            self.direction.y += 1
        if keys[pygame.K_a]:
            self.direction.x -= 1
        if keys[pygame.K_d]:
            self.direction.x += 1

        # Normalize direction vector to maintain constant speed in diagonals
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()

        # Update position based on direction, speed, and delta time
        self.pos += self.direction * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
