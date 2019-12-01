import pygame,sys
from random import randint
from pygame.locals import *
from juego import *

def tuto(music,sonido):
    pygame.init()
    ventana=pygame.display.set_mode([1280,720])
    salir=False
    fuente1 = pygame.font.SysFont ("Arial",30,True,False)
    fuente2 = pygame.font.SysFont ("Arial",60,True,False)
    naranjita = (255,183,98)
    #Fondos
    ifondo =[pygame.image.load("../assets/Fondos/tutorial1.png").convert_alpha(),
    pygame.image.load("../assets/Fondos/tutorial2.png").convert_alpha(),
    pygame.image.load("../assets/Fondos/tutorial3.png").convert_alpha(),
    pygame.image.load("../assets/Fondos/tutorial4.png").convert_alpha(),
    pygame.image.load("../assets/Fondos/tutorial5.png").convert_alpha(),
    pygame.image.load("../assets/Fondos/tutorial6.png").convert_alpha(),
    pygame.image.load("../assets/Fondos/tutorial7.png").convert_alpha()]
    i=0
    aux = 0
    pygame.mixer.music.stop()
    reloj1=pygame.time.Clock()
    cursor1 = Cursor()
    while salir!=True: #Loop principal
        for event in pygame.event.get(): #Corre todos los eventos en pygame
            if event.type == pygame.QUIT:
                salir=True
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if i< 6:
                        i+=1
                    aux+=1
        ventana.blit(ifondo[i],(0,0))
        if aux == 7:
            objetive =fuente1.render("Obten 40 puntos en 20 segundos!",0,(0,0,0))
            objetive2 =fuente2.render("Obten 40 puntos en 20 segundos!",0,(0,0,0))
            Game(False,1,5,20,15,15,objetive,40,20,objetive2,music,sonido)
            salir = True
        pygame.display.update()
