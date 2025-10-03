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


    clock = pygame.time.Clock()  # ⏱️ Clock object to control FPS
    dt = 0                       # delta time starts at 0


    while True:  # main game loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # exit the main() function
            
        screen.fill((0, 0, 0))  # fill the screen with black
        pygame.display.flip()  # update the screen

        clock.tick(60)  # limit to 60 FPS
        dt = clock.get_time() / 1000  # delta time in seconds
if __name__ == "__main__":
    main()
