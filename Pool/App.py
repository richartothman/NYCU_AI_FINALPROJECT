from matplotlib.pyplot import gray
import pygame
import sys
import time
from math import *
import Pool 

class App():
    def __init__(self):
        pygame.init()
        self.run = True

    def render(self,pool):
        '''-------------------------------------------------'''
        self.display = pygame.display.set_mode((Pool.width,Pool.height))
        pygame.display.set_caption("8 Ball Pool")
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.MOUSEBUTTONDOWN and pool.isStopped() and not pool.Iswin and not pool.GameOver:
                    x, y = pygame.mouse.get_pos()
                    dx = pool.balls[0].x - x
                    dy = pool.balls[0].y - y
                    angle = atan2(dy,dx) + 0.5*pi
                    force = hypot(dx,dy)/100
                    pool.ForcetoCue(angle,force)
            pool.draw(self.display)
            pool.update()
            pygame.display.flip()

Play = App()
Game = Pool.Game()
Play.render(Game)
