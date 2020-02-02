import pygame as pg
from pygame.locals import *
import sys

class HistoriaPantalla():
    color = (255,255,255)
    def __init__(self):
        self.background_img = pg.image.load('resources/back_space.png').convert()
        self.font = pg.font.Font('resources/fonts/font.ttf', 28)
        self.texto = self.font.render("historia que amaia desarrollaf\n lalalalalalaal", True, (100,100,100))
        self.texto_saltar_intro = self.font.render("saltar intro <space>", True, (100,100,100))
        

    def draw(self, screen):
        screen.blit(self.background_img, (0, 0))
        rect = self.texto.get_rect()
        screen.blit(self.texto, (100, 300))
        screen.blit(self.texto_saltar_intro, (400, 550))

    def handleEvents(self, event):
        for ev in event.get():
            if ev.type == KEYDOWN:
                if ev.key == K_SPACE:
                    print("siguiente pantalla")
        
    
