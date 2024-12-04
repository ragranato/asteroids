import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()  
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return        
        screen.fill((0, 0, 0))
        asteroids_to_split = []
        shots_to_remove = []

        for item in updatable:
            item.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if asteroid.collision(shot):
                    print("asteroid hit")                    
                    asteroids_to_split.append(asteroid)
                    shots_to_remove.append(shot)
        for shot in shots_to_remove:
            shot.kill()
        for asteroid in asteroids_to_split:
            asteroid.split(asteroids)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        time = clock.tick(60)
        dt += time / 50000
        
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()