import pygame as pg
import os
from arkanoid import ANCHO, ALTO, FPS
from arkanoid.elementos import Pala, Bola, Ladrillo
from arkanoid.funciones_records import extrae_nombres_records, extrae_valores_records

class Escena:
    def __init__(self, pantalla: pg.Surface):
        self.pantalla = pantalla
        self.clock = pg.time.Clock()

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
        self.jugador = Pala()
        self.bola = Bola(midbottom = self.jugador.rect.midtop)
        self.puntuacion = 0
        self.crear_muro()
        
    def crear_muro(self):
        num_filas = 5
        num_columnas = 6
        self.ladrillos = pg.sprite.Group()
        self.ladrillos.empty()
        
        margen_y = 40

        for fila in range(num_filas):
            for columna in range(num_columnas):
                ladrillo = Ladrillo(fila, columna)
                margen_x = (ANCHO - ladrillo.image.get_width()*num_columnas) / 2
                ladrillo.rect.x += margen_x
                ladrillo.rect.y += margen_y
                self.ladrillos.add(ladrillo)
    
    def bucle_principal(self):
        loop = True
        while loop == True:
            self.clock.tick(FPS) #IMPORTANTE AQUI
            for evento in pg.event.get():
                if evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE:
                    pg.quit()
                if evento.type == pg.KEYDOWN and evento.key == pg.K_SPACE:
                    self.bola.en_movimiento = True
                if evento.type == pg.QUIT:
                    pg.quit()
            #Pintar imagen de fondo
            self.pantalla.blit(self.background,(0, 0))

            #pintar jugador
            self.jugador.update()
            self.pantalla.blit(self.jugador.img, self.jugador.rect)

            #pintar muro
            self.ladrillos.draw(self.pantalla)

            #pintar pelota
            self.bola.colision(self.jugador)
            self.bola.update(self.jugador)
            self.pantalla.blit(self.bola.image, self.bola.rect)

            #Guardamos los ladrillos que colisionan con la bola
            golpeados = pg.sprite.spritecollide(self.bola, self.ladrillos, True)
            if len(golpeados) > 0:
                #Si hemos golpeado alguno invertimos la velocidad_y y sumamos 1 por cada elemento en la lista
                self.bola.vel_y = -self.bola.vel_y
                for _ in golpeados:
                    self.puntuacion += 1
                    print(self.puntuacion)
            pg.display.flip()
            loop = self.bola.game_over(self.puntuacion)

    

class Hall_of_fame(Escena):
    def __init__(self, pantalla: pg.Surface):
        super().__init__(pantalla)        
    
    def crear_texto(self):
        tipografia = pg.font.Font(os.path.join("resources", "fonts", "CabinSketch-Bold.ttf"), 40)
        csv_file = "puntuaciones.csv"
        valores = extrae_valores_records(csv_file)
        nombres = extrae_nombres_records(csv_file)
        borde = 100
        for index in range(len(valores)):
            texto_nombre = pg.font.Font.render(tipografia, nombres[index], True, (255, 255, 255))
            texto_record = pg.font.Font.render(tipografia, str(valores[index]), True, (255, 255, 255))
            pos_x = ANCHO/2 - texto_nombre.get_width()
            pos_x2 = ANCHO/2 + borde/2
            pos_y = index*texto_nombre.get_height() + borde*1.5
            self.pantalla.blit(texto_nombre, (pos_x, pos_y))
            self.pantalla.blit(texto_record, (pos_x2, pos_y))
        pg.display.flip()


    def bucle_principal(self):
        loop = True
        while loop == True:
            for evento in pg.event.get():
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_ESCAPE:
                        loop = False   
                if evento.type == pg.QUIT:
                    pg.quit()
            self.pantalla.fill((0,0,100))
            self.crear_texto()
            pg.display.flip()
            
            
            
            

