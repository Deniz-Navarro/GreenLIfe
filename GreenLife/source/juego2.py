import pygame,sys
from random import randint
from pygame.locals import *
from juego import *

def menu():
    pygame.init()
    ventana=pygame.display.set_mode([1280,720])
    salir=False
    fuente1 = pygame.font.SysFont ("Arial",30,True,False)
    black = (0,0,0)
    reloj1=pygame.time.Clock()
    mundo1 = pygame.image.load("../assets/Items/mundo1.png").convert_alpha()
    #mundo11 = pygame.image.load("../assets/Items/mundo11.png").convert_alpha()
    #mundo2 = pygame.image.load("../assets/Items/mundo2.png").convert_alpha()
    #mundo22 = pygame.image.load("../assets/Items/mundo22.png").convert_alpha()
    ifondo = pygame.image.load("../assets/Fondos/Menu.png").convert_alpha()
    start1 = pygame.image.load("../assets/Items/botons1.png").convert_alpha()
    start2 = pygame.image.load("../assets/Items/botons2.png").convert_alpha()
    equis1 = pygame.image.load("../assets/Items/equis.png").convert_alpha()
    equis2 = pygame.image.load("../assets/Items/equis1.png").convert_alpha()
    start = Button(start1,start2,1280/2-100,720/2-200)
    equis = Button(equis1,equis2,600,510)
    cursor1 = Cursor()
    while salir!=True: #Loop principal
        for event in pygame.event.get(): #Corre todos los eventos en pygame
            if event.type == pygame.QUIT:
                salir=True
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(start.rect):
                    objetive =fuente1.render("Obten 100 puntos en 30 segundos",0,(0,0,0))
                    Game(False,2,3,25,20,20,objetive,50,25)
                if cursor1.colliderect(equis.rect):
                    salir=True
                    pygame.quit()
                    sys.exit()

        #reloj1.tick(15)
        cursor1.update()
        ventana.fill(black)
        ventana.blit(ifondo,(0,0))
        start.update(ventana,cursor1)
        equis.update(ventana,cursor1)
        pygame.display.update()

menu()
