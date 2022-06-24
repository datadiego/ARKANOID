from arkanoid import ANCHO, ALTO, FPS
import random
import pygame as pg
from pygame.sprite import Sprite
import os
randint = random.randint
class Pala(Sprite):
    fps_ani = 12
    limite_iteracion = FPS // fps_ani
    iteracion = 0
    vel = 8
    margen_inferior = 70
    def __init__(self):
        super().__init__()
        self.sprites = []
        for i in range(3):
            self.sprites.append(
                pg.image.load(
                    os.path.join("resources", "images", f"electric0{i}.png")
                )
            )

        self.siguiente_imagen = 0
        self.img = self.sprites[self.siguiente_imagen]
        self.rect = self.img.get_rect(midbottom=(ANCHO/2, ALTO-self.margen_inferior))

    def update(self):
        estado_teclas = pg.key.get_pressed()
        if estado_teclas[pg.K_LEFT]:
            self.mueve_izquierda()
        if estado_teclas[pg.K_RIGHT]:
            self.mueve_derecha()
        self.iteracion += 1
        if self.iteracion == self.limite_iteracion:
            self.siguiente_imagen += 1
            if self.siguiente_imagen >= len(self.sprites):
                self.siguiente_imagen = 0
            self.img = self.sprites[self.siguiente_imagen]
            self.iteracion = 0

    def mueve_derecha(self):
        self.rect.x += self.vel
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO

    def mueve_izquierda(self):
        self.rect.x -= self.vel
        if self.rect.left < 0:
            self.rect.left = 0

class Ladrillo(Sprite):
    def __init__(self, fila, columna):
        super().__init__()
        ladrillo_verde = os.path.join("resources", "images", "greenTile.png")
        self.image = pg.image.load(ladrillo_verde)
        ancho = self.image.get_width()
        alto = self.image.get_height()

        self.rect = self.image.get_rect(x=columna * ancho, y=fila* alto)

class Bola(Sprite):
    vel_x = -5
    vel_y = -5
    def __init__(self, **kwargs):
        super().__init__()
        self.image = pg.image.load(os.path.join("resources", "images", "ball1.png"))
        self.rect = self.image.get_rect(**kwargs)

    def update(self, pala, iniciado):
        if not iniciado:
            self.rect.midbottom = pala.rect.midtop
        else:
            self.rect.x += self.vel_x
            self.rect.y += self.vel_y

            if self.rect.left < 0 or self.rect.right > ANCHO:
                self.vel_x = -self.vel_x
            if self.rect.top < 0:
                self.vel_y = -self.vel_y
            if self.rect.bottom > ALTO:
                self.game_over()
    
    def game_over(self):
        pass
                
