import pygame

class Arkanoid:
    def __init__(self) -> None:
        print("Iniciando el juego")
        pygame.init()
        print(f"Ancho: {ANCHO} x Alto: {ALTO}")
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        self.clock = pygame.time.Clock()

    def bucle_juego(self):
        loop = True
        while loop == True:
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        loop = False   
                if evento.type == pygame.QUIT:
                    loop = False
            #Guardamos el estado de las teclas que se han pulsado
            estado_teclas = pygame.key.get_pressed()

            if estado_teclas[pygame.K_LEFT]:
                pass
            if estado_teclas[pygame.K_RIGHT]:
                pass
            if estado_teclas[pygame.K_UP]:
                pass
            if estado_teclas[pygame.K_DOWN]:
                pass     
            #bucle de juego:
            self.pantalla.fill((220,0,0))

            pygame.display.flip()
    

if __name__ == "__main__":
    from __init__ import ANCHO, ALTO
    juego = Arkanoid()
    juego.bucle_juego()
else:
    from arkanoid import ANCHO, ALTO