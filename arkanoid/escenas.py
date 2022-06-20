import pygame as pg
class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla

class Portada(Escena):
    def bucle_principal(self):
        loop = True
        while loop == True:
            for evento in pg.event.get():
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_ESCAPE:
                        loop = False   
                if evento.type == pg.QUIT:
                    self.pantalla.fill((255,0,0))
                    loop = False
                    
            

class Partida(Escena):
    def bucle_principal(self):
        loop = True
        while loop == True:
            for evento in pg.event.get():
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_ESCAPE:
                        loop = False   
                if evento.type == pg.QUIT:
                    self.pantalla.fill((0,255,0))
                    loop = False
            

class Hall_of_fame(Escena):
    def bucle_principal(self):
        self.pantalla.fill((0,0,255))
        loop = True
        while loop == True:
            for evento in pg.event.get():
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_ESCAPE:
                        loop = False   
                if evento.type == pg.QUIT:
                    self.pantalla.fill((0,0,255))
                    loop = False
            

