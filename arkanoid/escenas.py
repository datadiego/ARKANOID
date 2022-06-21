from cgitb import text
import pygame as pg
import os
from arkanoid import ANCHO, ALTO
class Escena:
    def __init__(self, pantalla: pg.Surface):
        self.pantalla = pantalla

class Portada(Escena):
    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)
        self.logo = pg.image.load(os.path.join("resources", "images", "arkanoid_name.png"))
    
    def pintar_logo(self):
        width_logo = self.logo.get_width()
        pos_x = ANCHO/2-(width_logo/2)
        pos_y = ALTO/5
        self.pantalla.blit(self.logo,(pos_x, pos_y))
        pg.display.flip()

    def pintar_texto(self):
        tipografia = pg.font.Font(os.path.join("resources", "fonts", "CabinSketch-Bold.ttf"), 34)
        texto_start = pg.font.Font.render(tipografia, "Pulsa la barra espaciadora para empezar", True, (255, 255, 255))
        pos_x = ANCHO/2 - (texto_start.get_width()/2)
        pos_y = ALTO - (ALTO/3.2)
        self.pantalla.blit(texto_start, (pos_x, pos_y))
        pg.display.flip()

    def bucle_principal(self):
        loop = True
        self.pantalla.fill((23,111,193))
        self.pintar_logo()
        self.pintar_texto()
        
        while loop == True:
            for evento in pg.event.get():
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        loop = False   
                if evento.type == pg.QUIT:                 
                    pg.quit()
                    
class Partida(Escena):
    def bucle_principal(self):
        loop = True
        self.pantalla.fill((0,255,0))
        pg.display.flip()
        while loop == True:
            for evento in pg.event.get():
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_ESCAPE:
                        loop = False   
                if evento.type == pg.QUIT:
                    pg.quit()
            

class Hall_of_fame(Escena):
    def bucle_principal(self):
        self.pantalla.fill((0,0,255))
        pg.display.flip()
        loop = True
        while loop == True:
            for evento in pg.event.get():
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_ESCAPE:
                        loop = False   
                if evento.type == pg.QUIT:
                    pg.quit()
            

