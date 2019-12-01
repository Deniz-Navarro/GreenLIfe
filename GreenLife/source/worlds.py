import pygame,sys
from random import randint
from pygame.locals import *
from juego import *
from world1 import *
from world2 import *
from tutorial import *

def munditos(music,sonido):
    pygame.init()
    ventana=pygame.display.set_mode([1280,720])
    salir=False
    fuente1 = pygame.font.SysFont ("Arial",30,True,False)
    verdesito = (15,210,197)
    music = music
    reloj1=pygame.time.Clock()
    imundo1 = pygame.image.load("../assets/Items/mundo1.png").convert_alpha()
    imundo12 = pygame.image.load("../assets/Items/mundo11.png").convert_alpha()
    imundo2 = pygame.image.load("../assets/Items/mundo2.png").convert_alpha()
    imundo21 = pygame.image.load("../assets/Items/mundo21.png").convert_alpha()
    back1 = pygame.image.load("../assets/Items/back.png").convert_alpha()
    back2 = pygame.image.load("../assets/Items/back1.png").convert_alpha()
    ituto = pygame.image.load("../assets/Items/btntutorial.png").convert_alpha()
    ituto2 = pygame.image.load("../assets/Items/btntutorial2.png").convert_alpha()
    mundo1 = Button(imundo1,imundo12,320,720/2-150)
    mundo2 = Button(imundo2,imundo21,960-253,720/2-150)
    tutorial = Button(ituto,ituto2,475,720/2+150)
    back = Button(back1,back2,1050,50)
    cursor1 = Cursor()
    while salir!=True: #Loop principal
        for event in pygame.event.get(): #Corre todos los eventos en pygame
            if event.type == pygame.QUIT:
                salir=True
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(mundo1.rect):
                    world1(music,sonido)
                if cursor1.colliderect(mundo2.rect):
                    world2(music,sonido)
                if cursor1.colliderect(tutorial.rect):
                    tuto(music,sonido)
                if cursor1.colliderect(back.rect):
                    salir=True

        cursor1.update()
        ventana.fill(verdesito)
        mundo1.update(ventana,cursor1)
        mundo2.update(ventana,cursor1)
        tutorial.update(ventana,cursor1)
        back.update(ventana,cursor1)
        pygame.display.update()
