# https://www.pygame.org/docs/ref/pygame.html
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill
from asyncio import constants
import pygame
from constants import *

def main():
    pygame.init()
            
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while 1:
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    print("Starting asteroids!")

if __name__ == "__main__":
    main()

print(f"Screen width: {constants.SCREEN_WIDTH}") 
print(f"Screen height: {constants.SCREEN_HEIGHT}") 