import pygame as pg
from arkanoid.escenas import Hall_of_fame, Partida, Portada
import os
icon = pg.image.load(os.path.join("resources", "images", "ball1.png"))





class Arkanoid:
    def __init__(self) -> None:
        print("Iniciando el juego")
        pg.init()
        pg.font.init()
        print(f"Ancho: {ANCHO} x Alto: {ALTO}")
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("Arkanoid")
        pg.display.set_icon(icon)
        self.escenas = [Portada(self.pantalla), Partida(self.pantalla), Hall_of_fame(self.pantalla)]
        self.clock = pg.time.Clock()
        
    def jugar(self):
        for escena in self.escenas:
            escena.bucle_principal()
            pg.display.flip()
    def bucle_juego(self):
        loop = True
        while loop == True:
            for evento in pg.event.get():
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_ESCAPE:
                        loop = False   
                if evento.type == pg.QUIT:
                    loop = False
            #Guardamos el estado de las teclas que se han pulsado
            estado_teclas = pg.key.get_pressed()

            if estado_teclas[pg.K_LEFT]:
                pass
            if estado_teclas[pg.K_RIGHT]:
                pass
            if estado_teclas[pg.K_UP]:
                pass
            if estado_teclas[pg.K_DOWN]:
                pass
            #bucle de juego:
            #pg.draw.rect(self.pantalla, (255,255,255), self.jugador)
            #pg.draw.rect(self.pantalla, (255,255,255), self.jugador.bola)
            pg.display.flip()
    
if __name__ == "__main__":
    from __init__ import ANCHO, ALTO
    juego = Arkanoid()
    juego.bucle_juego()
else:
    from arkanoid import ANCHO, ALTO
