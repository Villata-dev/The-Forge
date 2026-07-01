import pygame
import random

class ParticleSystem:
    def __init__(self):
        self.particles = []

    def emit_sparks(self, pos, count=10):
        for _ in range(count):
            velocity = [random.uniform(-3, 3), random.uniform(-5, -1)]
            timer = random.randint(20, 40)
            self.particles.append([list(pos), velocity, timer])

    def update_and_draw(self, surface):
        for particle in self.particles[:]:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 1
            particle[1][1] += 0.2  # Gravedad
            
            pygame.draw.circle(surface, (255, 200, 50), (int(particle[0][0]), int(particle[0][1])), 2)
            if particle[2] <= 0:
                self.particles.remove(particle)
