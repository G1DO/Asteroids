# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * 




def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()  # sets up pygame's internal systems (graphics, sound, input, etc.)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:  # main game loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # exit the main() function
            
        screen.fill((0, 0, 0))  # fill the screen with black
        pygame.display.flip()  # update the screen


if __name__ == "__main__":
    main()
