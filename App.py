from matplotlib.pyplot import gray
import pygame
import sys
import time
from math import *
import Pool 

class App():
    def __init__(self):
        py = pygame.init()
        self.board = Pool.Game()
        self.run = True

    def render(self):
        '''-------------------------------------------------'''
        self.display = pygame.display.set_mode((Pool.width,Pool.height))
        pygame.display.set_caption("8 Ball Pool")

        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.board.isStopped() and not self.board.Iswin and not self.board.GameOver:
                    x, y = pygame.mouse.get_pos()
                    dx = self.board.balls[0].x - x
                    dy = self.board.balls[0].y - y
                    angle = atan2(dy,dx) + 0.5*pi
                    force = hypot(dx,dy)/100
                    self.board.ForcetoCue(angle,force)
            
            self.board.draw(self.display)
            self.board.update()
            pygame.display.flip()

Play = App()
Play.render()
