import pygame as pg
from pygame.locals import *
import sys

from entities import *
from pantallas import *

FPS = 60
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)


class Game:
    clock = pg.time.Clock()

    def __init__(self):
        self.screen = pg.display.set_mode((800,600))
        pg.display.set_caption("La búsqueda")
        self.pantallaActiva = JuegoPantalla()
                    
    def mainloop(self):
        while True:
            dt = self.clock.tick(FPS)
            
            self.pantallaActiva.draw(self.screen)
            self.pantallaActiva.handleEvents(pg.event)
            
            pg.display.flip()
    

if __name__ == '__main__':
    pg.init() 
    game = Game()
    game.mainloop()




