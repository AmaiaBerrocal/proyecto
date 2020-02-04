import pygame as pg
from pygame.locals import *

FPS = 60


class Nave(pg.sprite.Sprite):
    pictures = 'spaceship.xcf'
    speed = 10
    lives = 3

    def __init__(self, x=355, y=580):
        self.x = x
        self.y = y
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load('resources/{}'.format(self.pictures)).convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.h = self.rect.h

    def go_up(self):
        self.rect.y = max(0, self.rect.y - self.speed) 

    def go_down(self):
        self.rect.y = min(self.rect.y + self.speed, 800-self.h)