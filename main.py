# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

#Main Game Loop
while constants.running:
    # Initialising pygame
    pygame.init()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            constants.running = False

    screen.fill((0, 0, 0))

    pygame.display.flip()

if __name__ == "__main__":
    main()

pygame.quit()