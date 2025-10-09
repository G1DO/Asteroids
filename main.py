# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * 
from player import Player




def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()  # sets up pygame's internal systems (graphics, sound, input, etc.)
    clock = pygame.time.Clock()  # ⏱️ Clock object to control FPS
    dt = 0                       # delta time starts at 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    


    updatable =pygame.sprite.Group()
    drawable =pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)              
  

    while True:  # main game loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # exit the main() function
            
        updatable.update(dt)    
        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)   # خلفية سوداء
            # ارسم السفينة
        pygame.display.flip()    # اعرض التحديث
        clock.tick(60)  # limit to 60 FPS
        dt = clock.get_time() / 1000  # delta time in seconds
        


   
       
if __name__ == "__main__":
    main()
