# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    dt = 0
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    #Main Game Loop
    while constants.running:
        # Initialising pygame
        pygame.init()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                constants.running = False

        screen.fill((0, 0, 0))

        """Game Code below here"""
        player.update(dt)
        player.draw(screen)

        #pygame.time.Clock.tick(60)  # Limit to 60 FPS
        dt = pygame.time.get_ticks() / 1000.0

        pygame.display.flip()

if __name__ == "__main__":
    main()

pygame.quit()