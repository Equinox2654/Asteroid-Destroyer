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
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    running = True
    asteroids_killed = 0
    font = pygame.font.Font(None, 36)
    text = font.render(f"Asteroids Destroyed: {asteroids_killed}", True, (255, 255, 255))
    text_2 = font.render(f"Player Lives: {player.lives}", True, (255, 255, 255))

    #Main Game Loop
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
            print("Exiting game...")

        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000.0  # seconds since last frame

        """Game Code below here"""

        pygame.display.set_caption("Asteroid Destroyer")

        # Draw the text
        screen.blit(text, (10, 10))
        screen.blit(text_2, (10, 50))

        updatable.update(dt)
        for d in drawable:
            d.draw(screen)
        
        for a in asteroids:
            if player.collide(a):
                if player.lives > 0:
                    player.kill()
                    if player.spawn_timer == 0:
                        print(f"Player lives left: {player.lives}")
                    text_2 = font.render(f"Player Lives: {player.lives}", True, (255, 255, 255))
                    a.split()
                if player.lives == 0:
                    print("Game Over!")
                    print("GG!")
                    print(f"Asteroids killed: {asteroids_killed}")
                    running = False
                    return
            for s in updatable:
                if isinstance(s, Shot) and a.collide(s):
                    a.split()
                    s.kill()
                    asteroids_killed += 1
                    text = font.render(f"Asteroids Destroyed: {asteroids_killed}", True, (255, 255, 255))

        #Fix this later
        clock.tick(60)

        pygame.display.flip()

if __name__ == "__main__":
    main()

pygame.quit()