import pygame

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 64, 64)
        self.color = (200, 30, 30) # Rojo Forge
        self.speed = 300 # Pixeles por segundo
        self.direction = pygame.math.Vector2()

    def input(self):
        keys = pygame.key.get_pressed()
        
        # Eje Y (Arriba / Abajo)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        # Eje X (Izquierda / Derecha)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, dt):
        # Normalizar vector para evitar moverse mas rapido en diagonal
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt

    def update(self, dt):
        self.input()
        self.move(dt)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=8)
        # Borde para darle un poco de estilo
        pygame.draw.rect(surface, (255, 100, 100), self.rect, 2, border_radius=8)
