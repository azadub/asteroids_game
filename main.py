# https://www.pygame.org/docs/ref/pygame.html
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()   
    dt = 0     
    player = player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        
    while 1:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()
    
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()

