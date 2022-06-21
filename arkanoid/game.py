import pygame as pg
from arkanoid import ALTO, ANCHO
from arkanoid.escenas import Hall_of_fame, Partida, Portada
import os
icon = pg.image.load(os.path.join("resources", "images", "ball1.png"))

class Arkanoid:
    def __init__(self) -> None:
        print("Iniciando el juego")
        pg.init()
        pg.font.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("Arkanoid")
        pg.display.set_icon(icon)
        self.escenas = [Portada(self.pantalla), Partida(self.pantalla), Hall_of_fame(self.pantalla)]
        
    def jugar(self):
        for escena in self.escenas:
            escena.bucle_principal()
            pg.display.flip()
    

