import pygame,sys
from random import randint
from pygame.locals import *
from juego import *

def munditos():
    pygame.init()
    ventana=pygame.display.set_mode([1280,720])
    salir=False
    fuente1 = pygame.font.SysFont ("Arial",30,True,False)
    verdesito = (15,210,197)
    reloj1=pygame.time.Clock()
    imundo1 = pygame.image.load("../assets/Items/mundo1.png").convert_alpha()
    imundo12 = pygame.image.load("../assets/Items/mundo11.png").convert_alpha()
    imundo2 = pygame.image.load("../assets/Items/mundo2.png").convert_alpha()
    imundo21 = pygame.image.load("../assets/Items/mundo21.png").convert_alpha()
    back1 = pygame.image.load("../assets/Items/back.png").convert_alpha()
    back2 = pygame.image.load("../assets/Items/back1.png").convert_alpha()
    mundo1 = Button(imundo1,imundo12,320,720/2-100)
    mundo2 = Button(imundo2,imundo21,960-253,720/2-100)
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
                    objetive =fuente1.render("Obten 100 puntos en 30 segundos",0,(0,0,0))
                    Game(False,1,5,25,20,20,objetive,100,30)
                if cursor1.colliderect(mundo2.rect):
                    objetive =fuente1.render("Obten 50 puntos en 20 segundos",0,(0,0,0))
                    Game(False,2,3,30,20,20,objetive,50,20)
                if cursor1.colliderect(back.rect):
                    salir=True

        cursor1.update()
        ventana.fill(verdesito)
        mundo1.update(ventana,cursor1)
        mundo2.update(ventana,cursor1)
        back.update(ventana,cursor1)
        pygame.display.update()
