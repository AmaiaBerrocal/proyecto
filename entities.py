import pygame as pg
from pygame.locals import *


FPS = 60


class Nave(pg.sprite.Sprite):
    speed = 10
    lives = 3

    def __init__(self, x=20, y=300):
        self.x = x
        self.y = y

        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load('resources/image/spaceship.png').convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.h = self.rect.h

    def go_up(self):
       self.rect.y = max(0, self.rect.y - self.speed)

    def go_down(self):
        self.rect.y = min(600- self.h, self.rect.y + self.speed)

class Asteroide(pg.sprite.Sprite):  
    def __init__(self, x, y): 
        self.speed = 5
        
        self.w = 350/8
        self.h = 137/3

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

    def loadFrames(self):
        sprite_sheet = pg.image.load('resources/image/asteroides/asteroidesGrande.png').convert_alpha()
        for fila in range(3):
            y = fila * self.h
            for column in range(8):
                x = column * self.w

                image = pg.Surface((self.w, self.h), pg.SRCALPHA).convert_alpha()
                image.blit(sprite_sheet, (0,0), (x, y, self.w, self.h))

                self.frames.append(image)

        self.how_many = len(self.frames)
        self.image = self.frames[self.index]
  
    def update(self, dt):
        self.current_time += dt

        if self.current_time > self.animation_time:
            self.current_time = 0
            self.index +=1

            if self.index >= self.how_many:
                self.index = 0
        
            self.image = self.frames[self.index]

            self.rect.x -= self.speed
            


