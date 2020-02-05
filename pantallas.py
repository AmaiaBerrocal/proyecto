import pygame as pg
from pygame.locals import *
import sys

from entities import *

FPS = 60
WHITE = (255, 255, 255)

class InicioPantalla():
    def __init__(self):
        self.background_img = pg.image.load('resources/backgrounds/back_space.png').convert()
        
        self.font_texto = pg.font.Font('resources/fonts/PressStart2P.ttf', 50)
        self.texto = self.font_texto.render("LA BÚSQUEDA", True, (100,100,100))

        self.font_texto_start = pg.font.Font('resources/fonts/PressStart2P.ttf', 20)
        self.texto_start = self.font_texto_start.render("Empezar <espacio>", True, (100,100,100))

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
                    print("Paso a HistoriaPantalla")


class HistoriaPantalla():
    def __init__(self):
        self.background_img = pg.image.load('resources/backgrounds/back_space.png').convert()
        
        self.font_historia = pg.font.Font('resources/fonts/PressStart2P.ttf', 28)
        self.historia = self.font_historia.render("historia", True, (100,100,100))
        
        self.font_saltar_intro = pg.font.Font('resources/fonts/PressStart2P.ttf', 20)
        self.saltar_intro = self.font_saltar_intro.render("Saltar intro <espacio>", True, (100,100,100))

        #self.music = pg.mixer.Sound('resources/sounds/<SONIDO>')
        

    def draw(self, screen):
        screen.blit(self.background_img, (0, 0))
        
        screen.blit(self.historia, (100, 300))
        screen.blit(self.saltar_intro, (250, 550))

    def handleEvents(self, event):
        for ev in event.get():
            if ev.type == QUIT:
                pg.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_SPACE:
                    print("Paso a JuegoPantalla")
                    pantantallaActiva = InicioPantalla()


class JuegoPantalla:
    def __init__(self):
        self.background_img = pg.image.load('resources/backgrounds/back_space.png').convert()
      
        self.font_puntos = pg.font.Font('resources/fonts/PressStart2P.ttf', 20)
        self.marcadorP = self.font_puntos.render("Puntos:", True, WHITE)
        self.puntos = self.font_puntos.render("0", True, WHITE)
        self.font_vidas = pg.font.Font('resources/fonts/PressStart2P.ttf', 20)
        self.marcadorV = self.font_vidas.render("Vidas:", True, WHITE)
        self.vidas = self.font_vidas.render("3", True, WHITE)
        
        #self.music = pg.mixer.Sound('resources/sounds/<SONIDO>')

        self.player = Nave()
    
    def draw(self, screen):
        screen.blit(self.background_img, (0, 0))
        screen.blit(self.marcadorP, (550, 20))
        screen.blit(self.puntos, (700, 20)) #igual tengo que poner la y más cerca del borde
        screen.blit(self.marcadorV, (550, 40))
        screen.blit(self.vidas, (700, 40))
        screen.blit(self.player.image, self.player.rect)

    def handleEvents(self, event):
        for event in event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    self.player.go_up()
                if event.key == K_DOWN:
                    self.player.go_down()

        keys_pressed = pg.key.get_pressed()
        if keys_pressed[K_UP]:
            self.player.go_up()
        if keys_pressed[K_DOWN]:
            self.player.go_down()  
                     
    
class ScorePantalla:
    def __init__(self):
        self.background_img = pg.image.load('resources/backgrounds/back_space.png').convert()
        
        self.font_puntuacion = pg.font.Font('resources/fonts/PressStart2P.ttf', 28)
        self.puntuacion = self.font_puntuacion.render("Puntuación", True, (100,100,100))
        
        self.font_texto_salir = pg.font.Font('resources/fonts/PressStart2P.ttf', 20)
        self.texto_salir = self.font_texto_salir.render("Salir <espacio>", True, (100,100,100))

        #self.music = pg.mixer.Sound('resources/sounds/<SONIDO>')

    def draw(self, screen):
        screen.blit(self.background_img, (0, 0))
        
        screen.blit(self.puntuacion, (100, 300))
        screen.blit(self.texto_salir, (250, 550))

    def handleEvents(self, event):
        for ev in event.get():
            if ev.type == QUIT:
                pg.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_SPACE:
                    print("Paso a InicioPantalla")
                    





