from circleshape import *
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        # velocity = super().velocity
        self.position += self.velocity * dt
    
    def split(self, asteroids):
        
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.umiform(20, 50)
            new_vector1 = self.velocity.rotate(rand_angle)
            new_vector2 = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            new_asteroid1.velocity = new_vector1 * 1.2
            new_asteroid2.velocity = new_vector2 * 1.2

            asteroids.append(new_asteroid1)
            asteroids.append(new_asteroid2)

