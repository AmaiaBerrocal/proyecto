import pygame as pg
from pygame.locals import *
import sys

class HistoriaPantalla():
    
    def __init__(self):
        self.background_img = pg.image.load('resources/backgrounds/back_space.png').convert()
        
        self.font = pg.font.Font('resources/fonts/font.ttf', 28)
        self.texto = self.font.render("historia", True, (100,100,100))
        self.texto_saltar_intro = self.font.render("saltar intro <space>", True, (100,100,100))

        #self.music = pg.mixer.Sound('resources/sounds/<SONIDO>')
        

    def draw(self, screen):
        screen.blit(self.background_img, (0, 0))
        rect = self.texto.get_rect()
        screen.blit(self.texto, (100, 300))
        screen.blit(self.texto_saltar_intro, (400, 550))

    def handleEvents(self, event):
        for ev in event.get():
            if ev.type == QUIT:
                pg.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_SPACE:
                    print("siguiente pantalla")
        

class InicioPantalla():
   
    def __init__(self):
        self.background_img = pg.image.load('resources/backgrounds/back_space.png').convert()
        
        self.font_texto = pg.font.Font('resources/fonts/PressStart2P.ttf', 50)
        self.texto = self.font_texto.render("TITULO", True, (100,100,100))

        self.font_texto_start = pg.font.Font('resources/fonts/PressStart2P.ttf', 28)
        self.texto_start = self.font_texto_start.render("Start <space>", True, (100,100,100))

        #self.music = pg.mixer.Sound('resources/sounds/<SONIDO>')
        

    def draw(self, screen):
        screen.blit(self.background_img, (0, 0))
    
        screen.blit(self.texto, (100, 300))
        screen.blit(self.texto_start, (400, 550))

    def handleEvents(self, event):
        for ev in event.get():
            if ev.type == QUIT:
                pg.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_SPACE:
                    print("inicio de juego")

    
