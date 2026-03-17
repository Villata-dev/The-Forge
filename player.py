import pygame

class Player:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.width = 50
        self.height = 50
        self.color = (255, 0, 0)  # Red square
        self.speed = 200.0  # Pixels per second

    def update(self, dt):
        keys = pygame.key.get_pressed()

        dx = 0
        dy = 0

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx += 1

        # Normalize diagonal movement speed
        if dx != 0 and dy != 0:
            factor = (self.speed * dt) / (2**0.5)
            self.x += dx * factor
            self.y += dy * factor
        else:
            self.x += dx * self.speed * dt
            self.y += dy * self.speed * dt

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (int(self.x), int(self.y), self.width, self.height))
