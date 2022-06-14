import pygame
import Pool
from math import radians

if __name__ == '__main__':
    NewGame = Pool.Game()
    f = open("ALL_model\SEARCH")
    for line in f:
        
        NewGame.ForcetoCue(radians(int(line)),2)
        while not NewGame.isStopped():
            NewGame.update()
            display = pygame.display.set_mode((Pool.width,Pool.height))
            try:
                NewGame.draw(display)
            except:
                pass
            pygame.display.flip()