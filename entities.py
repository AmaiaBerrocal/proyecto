import pygame as pg
from pygame.locals import *
import random

#hago una clase para cada cosa que aparece en el juego y que tiene actividad: nave, asteroides y explosion
FPS = 60 #lo uso en Asteroide y en Explosion, por eso lo pongo fuera

class Nave(pg.sprite.Sprite):
    speed = 5

    def __init__(self, x=20, y=300):
    
        pg.sprite.Sprite.__init__(self) #llamo al constructor del que hereda (sprite)

        self.image = pg.image.load('resources/image/spaceship.png').convert_alpha() #cargo la imagen con el fondo transparente
        
        self.rect = self.image.get_rect() #saco el rectangulo que ocupa la imagen
        self.rect.x = x #asigno la x a ese rectangulo
        self.rect.y = y #asigno la y a ese rectangulo
        self.h = self.rect.h #calculo la h de ese rectangulo. No necesito la anchura (w)

    def go_up(self):
        self.rect.y = max(0, self.rect.y - self.speed)  #mueve hacia arriba la nave y no permite que pase de cero

    def go_down(self):
        self.rect.y = min(600 - self.h, self.rect.y + self.speed) #mueve hacia abajo la nave y no permite que pase de 600 

    def test_collisions(self, group): #comprueba si este objeto colisiona con el grupo que se le pasa
        return pg.sprite.spritecollide(self, group, True) #saca del grupo los elementos con los que ha colisionado y me los devuleve en una lista       

    def update(self, dt): #no hace nada pero he tenido que crearla para que el mainloop no se la pegue
        pass


class Asteroide(pg.sprite.Sprite):  
    def __init__(self, x, y, speed=5): 
        self.speed = speed
        
        image_random = self.random_image() #cojo los datos de un archivo aleatorio
        #como cada archivo tiene distinto tamaño, meto los datos con variables
        self.file_name = image_random[0] #asigno el nombre
        self.rows = image_random[2] #asigno numero de filas
        self.columns = image_random[1] #asigno numero de columnas
        self.w = image_random[3]/image_random[1] #asigno ancgura
        self.h = image_random[4]/image_random[2] #asigno altura

        pg.sprite.Sprite.__init__(self) #llamo al constructor del que hereda
        
        self.image = pg.Surface((self.w, self.h), pg.SRCALPHA, 32) #creo una superficie con el alto y ancho de mi imagen
        self.rect = self.image.get_rect() #saco el rectanculo de esa superficie
        self.rect.x = x
        self.rect.y = y
        self.frames = [] #lista vacia en la que metere las imagenes de la animacion
        self.index = 0 #indice de la imagen de la animacion que esta actualmente dibujada
        self.how_many = 0 #numero de imagenes que tendra la animacion
        self.animation_time = FPS #la velocidad a la que se ejecuta a animacion
        
        self.loadFrames() #mete las imagenes de la animacion en la lista de frames
        self.current_time = 0

    def random_image(self):
        pictures = [['asteroidesGrande.png', 8, 3, 350, 137], #nombre archivo, columnas, lineas, alto, ancho
                    ['asteroidesMedio.png', 8, 2, 261, 77], 
                    ['asteroidesMini.png', 8, 2, 149, 36]]
        
        image_random = random.randint(0,2) #elijo un índice al azar(una imagen)
        
        return pictures[image_random] #la devuelvo


    def loadFrames(self):
        sprite_sheet = pg.image.load('resources/image/asteroides/' + self.file_name).convert_alpha()
        for fila in range(self.rows): #recorro el archivo, separo las imagenes y las meto en la lista
            y = fila * self.h
            for column in range(self.columns):
                x = column * self.w

                image = pg.Surface((self.w, self.h), pg.SRCALPHA).convert_alpha()
                image.blit(sprite_sheet, (0,0), (x, y, self.w, self.h)) #cogido de ejercicio de clase.

                self.frames.append(image) #las mete en la lista

        self.how_many = len(self.frames) #actualiza self.how_many
        self.image = self.frames[self.index] #actualiza self.image
  
    def update(self, dt): #animamos los asteroides
        self.current_time += dt #LE ASIGNO VALOR EN LA LINEA 20 DEL MAIN!!!!!

        if self.current_time > self.animation_time:
            self.current_time = 0
            self.index +=1

            if self.index >= self.how_many: #cuando se llega a la ultima imagen, vuelve a la primera
                self.index = 0
        
            self.image = self.frames[self.index]

            self.rect.x -= self.speed #hace que se muevan de dcha a izq


class Explosion(pg.sprite.Sprite):
    def __init__(self, x, y): 
        self.rows = 4 #como solo tengo una imagen, meto los datos a mano
        self.columns = 4
        self.w = 256/4
        self.h = 256/4

        pg.sprite.Sprite.__init__(self)
        
        self.image = pg.Surface((self.w, self.h), pg.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.frames = []
        self.index = 0
        self.how_many = 0
        self.animation_time = FPS
        
        self.loadFrames()
        self.current_time = 0

    def loadFrames(self): #hago lo mismo que antes para conseguir las imagenes del archivo
        sprite_sheet = pg.image.load('resources/image/explosion.png').convert_alpha()
        for fila in range(self.rows):
            y = fila * self.h
            for column in range(self.columns):
                x = column * self.w

                image = pg.Surface((self.w, self.h), pg.SRCALPHA).convert_alpha()
                image.blit(sprite_sheet, (0,0), (x, y, self.w, self.h))

                self.frames.append(image)

        self.how_many = len(self.frames)
        self.image = self.frames[self.index]
  
    def update(self, dt):
        self.current_time += dt #LE ASIGNO EL VALOR EN LA LINEA 20 DEL MAIN!!!!

        if self.current_time > self.animation_time:
            self.current_time = 0
            self.index +=1
            #aqui, cuando acabo la lista, no vulevo a la primera imagen porque quiero que la animacion termine
            self.image = self.frames[self.index]

    def end_animacion(self): #me dice el numero de frames que faltan para que acabe la animacion. Lo necesito para saber cuando tengo que dibujar una nueva nave.
        return self.how_many - self.index #frames totales(en este caso 16) - indice del frame en el que estoy(0-15)