import pygame as pg
from pygame.locals import *
import sys

from entities import *

FPS = 60
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)


class Game:
    clock = pg.time.Clock()

    def __init__(self):
        self.screen = pg.display.set_mode((800,600))
        pg.display.set_caption("ooook")

    def quitGame(self):
        pg.quit()
        sys.exit()


    def handleEvents(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.quitGame()

                    
    def mainloop(self):
        while True:
            dt = self.clock.tick(FPS)
            self.handleEvents()
            self.screen.fill(YELLOW)

            
            pg.display.flip()
    
    

if __name__ == '__main__':
    pg.init() 
    game = Game()
    game.mainloop()




