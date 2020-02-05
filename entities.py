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

        self.image = pg.image.load('resources/spaceship.png').convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.h = self.rect.h

    def go_up(self):
       self.rect.y = max(0, self.rect.y - self.speed)
    def go_down(self):
        self.rect.y = min(600- self.h, self.rect.y + self.speed)