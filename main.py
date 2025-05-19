# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from player import Player

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
clock = pygame.time.Clock()

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    #Main Game Loop
    while constants.running:
        # Initialising pygame
        pygame.init()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                constants.running = False

        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000.0  # seconds since last frame

        """Game Code below here"""
        player.update(dt)
        player.draw(screen)

        #Fix this later
        clock.tick(60)


        pygame.display.flip()

if __name__ == "__main__":
    main()

pygame.quit()