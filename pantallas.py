import pygame as pg
from pygame.locals import *
import sys
import sqlite3

from entities import *

FPS = 60
WHITE = (255, 255, 255)

class InicioPantalla:
    def __init__(self):
        self.background_img = pg.image.load('resources/backgrounds/back_space.png').convert()
        
        self.font_texto = pg.font.Font('resources/fonts/PressStart2P.ttf', 50)
        self.texto = self.font_texto.render("LA BÚSQUEDA", True, (WHITE))

        self.font_texto_start = pg.font.Font('resources/fonts/PressStart2P.ttf', 20)
        self.texto_start = self.font_texto_start.render("Empezar <espacio>", True, (WHITE))

        #self.music = pg.mixer.Sound('resources/sounds/<SONIDO>')
        

    def draw(self, screen):
        screen.blit(self.background_img, (0, 0))
    
        screen.blit(self.texto, (120, 200))
        screen.blit(self.texto_start, (400, 550))

    def handleEvents(self, event):
       
        for ev in event.get():
            if ev.type == QUIT:
                pg.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_SPACE:
                    print("Paso a HistoriaPantalla")

    def update(self):
        pass
       

class HistoriaPantalla:
    def __init__(self):

        self.background_img = pg.image.load('resources/backgrounds/back_space.png').convert()
       
        self.alto_linea = 25
        self.margen = 6 
        self.font_historia = pg.font.Font('resources/fonts/PressStart2P.ttf', self.alto_linea)   
        
        self.font_saltar_intro = pg.font.Font('resources/fonts/PressStart2P.ttf', 20)
        self.saltar_intro = self.font_saltar_intro.render("Saltar intro <espacio>", True, (WHITE))

        #self.music = pg.mixer.Sound('resources/sounds/<SONIDO>')
        

    def draw(self, screen):
        screen.blit(self.background_img, (0, 0))
        screen.blit(self.saltar_intro, (300, 550))
        
        texto = ["Año 2051. Tras siglos de", 
                 "expolio, el planeta Tierra",
                 "ya no puede proporcionar", 
                 "el hogar que antaño fue",
                 "para los seres humanos.", 
                 "El fin se aproxima, y un grupo",
                 "de valientes voluntarias,",
                 "bajo el mando de la capitana",
                 "Zur, emprenden la arriesgada",
                 "misión de encontrar un",
                 "nuevo hogar para la humanidad."]
        
        y = 100
        for linea in texto:
            linea_pygame = self.font_historia.render(linea, True, (WHITE))
            screen.blit(linea_pygame, (50, y))
            y += self.alto_linea + self.margen
              

    def handleEvents(self, event):
        for ev in event.get():
            if ev.type == QUIT:
                pg.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_SPACE:
                    print("Paso a JuegoPantalla")
                    pantantallaActiva = InicioPantalla()

    def update(self):
        pass
    

class JuegoPantalla:
    def __init__(self, creation_time=60):
        self.background_img = pg.image.load('resources/backgrounds/back_space.png').convert()
      
        self.font_puntos = pg.font.Font('resources/fonts/PressStart2P.ttf', 20)
        self.marcadorP = self.font_puntos.render("Puntos:", True, WHITE)
        self.puntos = self.font_puntos.render("0", True, WHITE)
        self.font_vidas = pg.font.Font('resources/fonts/PressStart2P.ttf', 20)
        self.marcadorV = self.font_vidas.render("Vidas:", True, WHITE)
        self.vidas = self.font_vidas.render("0", True, WHITE)
        
        self.score = 0

        self.current_time = 0
        self.creation_time = creation_time
        #self.music = pg.mixer.Sound('resources/sounds/<SONIDO>')

        self.player = Nave()
        self.enemies = []
    
    def random_y(self):
        return random.randint(0,600)
        
    def handleEvents(self, event):
        for ev in event.get():
            if ev.type == QUIT:
                pg.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_UP:
                    self.player.go_up()
                if ev.key == K_DOWN:
                    self.player.go_down()

        keys_pressed = pg.key.get_pressed()
        if keys_pressed[K_UP]:
            self.player.go_up()
        if keys_pressed[K_DOWN]:
            self.player.go_down()  
    
    def create_asteriod(self):
        self.current_time += 1
        if self.current_time >= self.creation_time:
            self.enemies.append(Asteroide(820, self.random_y()))
            self.current_time = 0
    
    def test_collisions(self, borra=False):
        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy):
                self.player = Explosion(self.player.rect.x, self.player.rect.y)
                #TODO: sonido explosion

        
    def update(self, dt):       
        self.score += 1
        self.puntos = self.font_puntos.render(str(self.score), True, WHITE)
        
        self.create_asteriod()
        
        self.test_collisions()
        
        for enemy in self.enemies:
            if enemy.rect.x < -40:
                self.enemies.remove(enemy)
            enemy.update(dt)
        self.player.update(dt)
        

    def draw(self, screen):
        screen.blit(self.background_img, (0, 0))
        screen.blit(self.marcadorP, (550, 20))
        screen.blit(self.puntos, (700, 20)) 
        screen.blit(self.marcadorV, (550, 40))
        screen.blit(self.vidas, (700, 40))
        screen.blit(self.player.image, self.player.rect)
        
        for enemy in self.enemies:
            screen.blit(enemy.image, enemy.rect)


class ScorePantalla:
    def __init__(self):
        self.background_img = pg.image.load('resources/backgrounds/back_space.png').convert()
        
        self.font_puntuacion = pg.font.Font('resources/fonts/PressStart2P.ttf', 28)
        self.puntuacion = self.font_puntuacion.render("Puntuación", True, (WHITE))
        
        self.font_texto_salir = pg.font.Font('resources/fonts/PressStart2P.ttf', 20)
        self.texto_salir = self.font_texto_salir.render("Salir <espacio>", True, (WHITE))

        #self.music = pg.mixer.Sound('resources/sounds/<SONIDO>')
        
        self.alto_linea = 25
        self.margen = 6 
        self.scores = []
        self.read_database()
        

    def read_database(self):
        conn = sqlite3.connect('data/database.db')
        cursor = conn.cursor()

        rows = cursor.execute('SELECT * from score;')
        self.scores = []
        for row in rows:
            self.scores.append(row)
            
        conn.commit()
        conn.close()     
        

    def draw(self, screen):
        screen.blit(self.background_img, (0, 0))
        
        screen.blit(self.puntuacion, (100, 100))
        screen.blit(self.texto_salir, (250, 550))
        
        y = 150
        for row in self.scores:
            row_scores = self.font_puntuacion.render(row[0]+'-'+str(row[1]), True, (WHITE))
            screen.blit(row_scores, (50, y))
            y += self.alto_linea + self.margen     


    def handleEvents(self, event):
        for ev in event.get():
            if ev.type == QUIT:
                pg.quit()
                sys.exit()
            if ev.type == KEYDOWN:
                if ev.key == K_SPACE:
                    print("Paso a InicioPantalla")

    def update(self, dt):
        pass
                  





