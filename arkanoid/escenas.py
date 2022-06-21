import pygame as pg
import os
from arkanoid import ANCHO, ALTO
from arkanoid.elementos import Pala, Bola

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
        tipografia = pg.font.Font(os.path.join("resources", "fonts", "CabinSketch-Bold.ttf"), 30)
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
    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)
        self.background = pg.image.load(os.path.join("resources", "images", "background.jpg"))
        self.jugador = Pala(self.pantalla)
        self.bola = Bola(self.pantalla)
        self.clock = pg.time.Clock()
        #self.bola = Bola()

    def bucle_principal(self):
        loop = True
        while loop == True:
            for evento in pg.event.get():
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_ESCAPE:
                        loop = False
                if evento.type == pg.QUIT:
                    pg.quit()
            estado_teclas = pg.key.get_pressed()
            if estado_teclas[pg.K_LEFT]:
                self.jugador.mueve_izquierda()
            if estado_teclas[pg.K_RIGHT]:
                self.jugador.mueve_derecha()
            self.pantalla.blit(self.background,(0, 0))
            self.jugador.muestra_pala()
            self.bola.mover_bola()
            self.bola.muestra_bola()
            pg.display.flip()
            self.clock.tick(60)
            
    
    def pintar_fondo(self):
        pass
            

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
            

