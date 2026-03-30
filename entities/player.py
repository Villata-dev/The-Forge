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

        # Stamina and Dash attributes
        self.stamina_max = 100.0
        self.stamina_actual = 100.0
        self.stamina_regen_rate = 20.0  # units per second
        self.dash_cost = 30.0
        self.dash_speed_multiplier = 3.0
        self.dash_duration = 0.2  # seconds
        self.dash_cooldown = 0.5  # seconds

        self.is_dashing = False
        self.dash_timer = 0.0
        self.dash_cooldown_timer = 0.0

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

        # Dash input handling
        can_dash = (keys[pygame.K_SPACE] or keys[pygame.K_LSHIFT]) and not self.is_dashing and self.dash_cooldown_timer <= 0
        if can_dash and self.direction.length() > 0 and self.stamina_actual >= self.dash_cost:
            self.is_dashing = True
            self.dash_timer = self.dash_duration
            self.stamina_actual -= self.dash_cost

        # Timers update
        if self.dash_timer > 0:
            self.dash_timer -= dt
            if self.dash_timer <= 0:
                self.is_dashing = False
                self.dash_cooldown_timer = self.dash_cooldown

        if self.dash_cooldown_timer > 0:
            self.dash_cooldown_timer -= dt

        # Normalize direction vector to maintain constant speed in diagonals
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()

        # Apply dash speed multiplier
        current_speed = self.speed
        if self.is_dashing:
            current_speed *= self.dash_speed_multiplier
        else:
            # Stamina regeneration
            self.stamina_actual += self.stamina_regen_rate * dt
            if self.stamina_actual > self.stamina_max:
                self.stamina_actual = self.stamina_max

        # Update position based on direction, speed, and delta time
        self.pos += self.direction * current_speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
