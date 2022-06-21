from arkanoid import ANCHO, ALTO
import random
import pygame as pg
import os
randint = random.randint
class Pala:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.img = pg.image.load(os.path.join("resources", "images", "electric00.png"))
        self.x = (ANCHO - self.img.get_width()) / 2 
        self.y = ALTO-70
        self.vel = 5
    
    def muestra_pala(self):
        self.pantalla.blit(self.img,(self.x, self.y))

    def mueve_derecha(self):
        self.x += self.vel
        if self.x > ANCHO - self.img.get_width():
            self.x = ANCHO - self.img.get_width()

    def mueve_izquierda(self):
        self.x -= self.vel
        if self.x < 0:
            self.x = 0

class Bola:
    def __init__(self, pantalla):
        self.vel_x = randint(-5,5)
        self.vel_y = randint(1,5)
        self.pantalla = pantalla
        self.img = pg.image.load(os.path.join("resources", "images", "ball1.png"))
        self.x = (ANCHO - self.img.get_width())/2
        self.y = 200
    def reset_bola(self):
        self.x = (ANCHO - self.img.get_width())/2
        self.y = 200 
    def check_border(self):
        if self.x < 0:  
            self.vel_x = -self.vel_x
        if self.x > ANCHO-self.img.get_width():
            self.vel_x = -self.vel_x
        if self.y < 0:
            self.vel_y = -self.vel_y
        if self.y > ALTO -self.img.get_height():
            self.reset_bola()

    def mover_bola(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.check_border()

    def muestra_bola(self):
        self.pantalla.blit(self.img,(self.x, self.y))
