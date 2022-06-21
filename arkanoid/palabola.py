from arkanoid import ANCHO, ALTO
import pygame as pg
import os

class Pala():
    def __init__(self, pantalla):
        self.width = 100
        self.height = 20
        self.x = ANCHO / 2 - self.width/2
        self.y = ALTO-50
        self.pantalla = pantalla
        self.img = pg.image.load(os.path.join("resources", "images", "electric00.png"))
        #self.bola = Bola(ANCHO/2, self.y, self.height)
    
    def muestra_pala(self):
        self.pantalla.blit(self.img,(self.x, self.y))
        pg.display.flip()

class Bola(pg.Rect):
    def __init__(self, x, y, size):
        self.ball_size = size
        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.pegado_a_paleta = True
        super(Bola, self).__init__(self.x-(self.ball_size/2), self.y-(self.ball_size), self.ball_size, self.ball_size)