import pygame
from entities.weapon_hitbox import WeaponHitbox

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, obstacle_sprites):
        super().__init__()
        self.pos = pygame.math.Vector2(x, y)
        self.direction = pygame.math.Vector2(0, 0)
        self.facing_direction = pygame.math.Vector2(0, 1)  # Default facing down
        self.speed = 250.0
        self.obstacle_sprites = obstacle_sprites

        # Placeholder image: a red rectangle
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=self.pos)

        # Hitbox for collisions (at the feet)
        self.hitbox = self.rect.inflate(-10, -30)
        self.hitbox.midbottom = self.rect.midbottom

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

    def attack(self, groups):
        WeaponHitbox(self, groups)

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # Moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # Moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # Moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # Moving up
                        self.hitbox.top = sprite.hitbox.bottom

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

        if self.direction.length() > 0:
            self.facing_direction = self.direction.copy().normalize()

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

        # Movement and collision
        velocity = self.direction * current_speed * dt

        # Horizontal movement
        self.hitbox.x += round(velocity.x)
        self.collision('horizontal')

        # Vertical movement
        self.hitbox.y += round(velocity.y)
        self.collision('vertical')

        # Keep within screen boundaries (assuming 800x600)
        if self.hitbox.left < 0: self.hitbox.left = 0
        if self.hitbox.right > 800: self.hitbox.right = 800
        if self.hitbox.top < 0: self.hitbox.top = 0
        if self.hitbox.bottom > 600: self.hitbox.bottom = 600

        self.rect.midbottom = self.hitbox.midbottom
        self.pos.x = self.rect.centerx
        self.pos.y = self.rect.centery

