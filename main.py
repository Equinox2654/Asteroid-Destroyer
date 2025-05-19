# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (updatable, drawable, asteroids)
AsteroidField.containers = (updatable)
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
asteroid_field = AsteroidField()
Shot.containers = (updatable, drawable)


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    running = True

    #Main Game Loop
    while running:
        # Initialising pygame
        pygame.init()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000.0  # seconds since last frame

        """Game Code below here"""
        updatable.update(dt)
        for d in drawable:
            d.draw(screen)
        
        for a in asteroids:
            if player.collide(a):
                print("Game Over!")
                running = False
            for s in updatable:
                if isinstance(s, Shot) and a.collide(s):
                    a.split()
                    s.kill()

        #Fix this later
        clock.tick(60)

        pygame.display.flip()

if __name__ == "__main__":
    main()

pygame.quit()