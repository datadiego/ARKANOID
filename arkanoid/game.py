import pygame as pg

class Pala(pg.Rect):
    def __init__(self):
        self.width = 100
        self.height = 20
        self.x = ANCHO / 2 - self.width/2
        self.y = ALTO - 50
        super(Pala, self).__init__(self.x, self.y, self.width, self.height)
        self.bola = Bola(ANCHO/2, self.y, self.height)

class Bola(pg.Rect):
    def __init__(self, x, y, size):
        self.ball_size = size
        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.pegado_a_paleta = True
        super(Bola, self).__init__(self.x-(self.ball_size/2), self.y-(self.ball_size), self.ball_size, self.ball_size)

                


class Arkanoid:
    def __init__(self) -> None:
        print("Iniciando el juego")
        pg.init()
        print(f"Ancho: {ANCHO} x Alto: {ALTO}")
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        self.clock = pg.time.Clock()
        self.jugador = Pala()
        

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
            self.pantalla.fill((220,0,0))
            pg.draw.rect(self.pantalla, (255,255,255), self.jugador)
            pg.draw.rect(self.pantalla, (255,255,255), self.jugador.bola)
            pg.display.flip()
    

if __name__ == "__main__":
    from __init__ import ANCHO, ALTO
    juego = Arkanoid()
    juego.bucle_juego()
else:
    from arkanoid import ANCHO, ALTO
