from copy import deepcopy
import pygame
import Pool
from math import radians

def Generate_Bestshots(game):
    shot = None
    MaxDist = 0
    prevpos = game.getAllballPos()
    for i in range(360):
        New = deepcopy(game)
        New.ForcetoCue(radians(i),2)
        New.full_update()
        if New.GameOver: continue

        curpos = New.getAllballPos()
        if prevpos[1:] == curpos[1:]:continue

        CurrDist = New.getDistribution()
        if MaxDist < CurrDist:
            shot = i
            MaxDist = CurrDist

    return shot

if __name__ == '__main__':
    NewGame = Pool.Game()
    f = open("ALL_model\SEARCH")
    while not NewGame.Iswin:
        shot = Generate_Bestshots(NewGame)    
        
        f.write(shot)
        NewGame.ForcetoCue(radians(shot),2)
        while not NewGame.isStopped():
            NewGame.update()
            display = pygame.display.set_mode((Pool.width,Pool.height))
            try:
                NewGame.draw(display)
            except:
                pass
            pygame.display.flip()
    
    print("Win!")
