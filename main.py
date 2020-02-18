import pygame as pg
from pygame.locals import *
import sys

from entities import *
from pantallas import *

FPS = 60 #el mainloop se ejecuta 60 veces por segundo

class Game:
    clock = pg.time.Clock() 

    def __init__(self):
        self.screen = pg.display.set_mode((800,600)) #creo la pantalla
        pg.display.set_caption("La búsqueda") #titulo de pantalla
        self.pantallaActiva = AnimacionPantalla() #pantalla que se esta dibujando (tengo que gestionar el cambio)
                    
    def mainloop(self): #bucle principal del juego
        while True:
            dt = self.clock.tick(FPS) #se asegura de que haya pasado el tiempo que queremos y sino espera
            
            self.pantallaActiva.handleEvents(pg.event) #los eventos los maneja la pantalla activa porque son diferentes en cada una
            self.pantallaActiva.update(dt) #actualiza la pantalla
            self.pantallaActiva.draw(self.screen) #pinta la pantalla
            
            pg.display.flip() #muestra la pantalla
    

if __name__ == '__main__':
    pg.init() #inicio pygame
    game = Game() #instancio mi clase juego
    game.mainloop() #ejecuto el mainloop de mi instacia