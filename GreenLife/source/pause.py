import pygame,sys
from random import randint
from pygame.locals import *
from juego import *

def mpause():
    pygame.init()
    ventana=pygame.display.set_mode([1280,720])
    salir=False
    fuente1 = pygame.font.SysFont ("Arial",30,True,False)
    fuente2 = pygame.font.SysFont ("Arial",60,True,False)
    naranjita = (139,81,143)
    reloj1=pygame.time.Clock()
    ifondo = pygame.image.load("../assets/Fondos/Pause.png").convert_alpha()
    icontinuar1 = pygame.image.load("../assets/Items/continuar.png").convert_alpha()
    icontinuar2 = pygame.image.load("../assets/Items/continuar1.png").convert_alpha()
    ireiniciar1 = pygame.image.load("../assets/Items/reiniciar.png").convert_alpha()
    ireiniciar2 = pygame.image.load("../assets/Items/reiniciar1.png").convert_alpha()
    cursor1 = Cursor()
    continuar = Button(icontinuar1,icontinuar2,400,720/2)
    reiniciar = Button(ireiniciar1,ireiniciar2,720,720/2)
    while salir!=True: #Loop principal
        for event in pygame.event.get(): #Corre todos los eventos en pygame
            if event.type == pygame.QUIT:
                salir=True
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cursor1.colliderect(continuar.rect):
                salir=True

        cursor1.update()
        ventana.blit(ifondo,(200,0))
        continuar.update(ventana,cursor1)
        reiniciar.update(ventana,cursor1)
        pygame.display.update()
