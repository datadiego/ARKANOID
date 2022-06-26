from arkanoid import ANCHO, ALTO, FPS
import random
import pygame as pg
from pygame.sprite import Sprite
import os
import csv
from arkanoid.funciones_records import bubble_sort, extrae_nombres_records, extrae_valores_records, limit_array

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
        self.puntos = 10
            

class Bola(Sprite):
    vel_x = -5
    vel_y = -14
    vidas = 1
    def __init__(self, **kwargs):
        super().__init__()
        self.image = pg.image.load(os.path.join("resources", "images", "ball1.png"))
        self.rect = self.image.get_rect(**kwargs)
        self.en_movimiento = False

    def colision(self, otro):
        if self.rect.colliderect(otro):
            self.vel_y = -self.vel_y
            #TODO: La bola puede quedarse atrapada en medio de la pala

    def update(self, pala):
        if not self.en_movimiento:
            self.rect.midbottom = pala.rect.midtop
        else:
            self.rect.x += self.vel_x
            self.rect.y += self.vel_y

            if self.rect.left < 0 or self.rect.right > ANCHO:
                self.vel_x = -self.vel_x
            if self.rect.top < 0:
                self.vel_y = -self.vel_y
            if self.rect.bottom > ALTO:
                self.perder_vida()
                self.en_movimiento = False

    def perder_vida(self):
        self.vidas -= 1
        print(f"Tienes {self.vidas} vidas")
        #TODO: ???? Las bolas no deberian tener vidas, esto deberia de poderse manipular en la escena partida, esta solucion es la mas facil
       
    def escribe_records(self, puntos):
        csv_filer = open("puntuaciones.csv", "a")
        csv_file = open("puntuaciones.csv", "r")
        limite_records = 10
        if csv_file.read() == "":
            print("No hay records previos")
            nombre_jugador = self.valida_input()
            csv_file = open("puntuaciones.csv", "w")
            csv_file.write(nombre_jugador)
            csv_file.write(",")
            csv_file.write(str(puntos))
            csv_file.write("\n")
            return
        else:
            print("Ya hay records previos") 
            valores = extrae_valores_records("puntuaciones.csv")
            nombres = extrae_nombres_records("puntuaciones.csv")
            print(valores)
            print(nombres)
            min_record = min(valores)
            '''
            if puntos > min_record:
                nombre_jugador = self.valida_input()
                csv_file = open("puntuaciones.csv", "a")
                csv_file.write(nombre_jugador)
                csv_file.write(",")
                csv_file.write(str(puntos))
                csv_file.write("\n")
            '''

            if puntos > min_record or len(valores) < limite_records:
                nombre_jugador = self.valida_input()
                valores.append(puntos)
                nombres.append(nombre_jugador)
                bubble_sort(valores, nombres)
                limit_array(valores, limite_records)
                limit_array(valores, limite_records)
                csv_file = open("puntuaciones.csv", "w")
                for i in range(len(valores)):
                    csv_file.write(nombres[i])
                    csv_file.write(",")
                    csv_file.write(str(valores[i]))
                    csv_file.write("\n")


                
        csv_file.close()
        #TODO: Los records deberian de ordenarse segun la puntuación

    def game_over(self, puntos):
        if self.vidas == 0:
            self.escribe_records(puntos)
            return False
        else:
            return True
    def valida_input(self):
        output = ""
        while output == "":
            output = str(input("Nombre: "))
        return output
                
