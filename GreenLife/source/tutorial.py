import pygame,sys
from random import randint
from pygame.locals import *
from juego import *

def tutorial(music,sonido):
    pygame.init()
    ventana=pygame.display.set_mode([1280,720])
    salir=False
    fuente1 = pygame.font.SysFont ("Arial",30,True,False)
    fuente2 = pygame.font.SysFont ("Arial",60,True,False)
    naranjita = (255,183,98)
    reloj1=pygame.time.Clock()
    cursor1 = Cursor()
    while salir!=True: #Loop principal
        for event in pygame.event.get(): #Corre todos los eventos en pygame
            if event.type == pygame.QUIT:
                salir=True
                pygame.quit()
                sys.exit()

        objetive =fuente1.render("Obten 50 puntos en 30 segundos!",0,(0,0,0))
        objetive2 =fuente2.render("Obten 50 puntos en 30 segundos!",0,(0,0,0))
        Game(False,1,7,20,10,10,objetive,50,30,objetive2,music,sonido)

        pygame.display.update()
