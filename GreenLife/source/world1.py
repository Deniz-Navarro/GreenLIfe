import pygame,sys
from random import randint
from pygame.locals import *
from juego import *

def world1(music,sonido):
    pygame.init()
    ventana=pygame.display.set_mode([1280,720])
    salir=False
    fuente1 = pygame.font.SysFont ("Arial",30,True,False)
    fuente2 = pygame.font.SysFont ("Arial",60,True,False)
    naranjita = (255,183,98)
    reloj1=pygame.time.Clock()
    ilvl1 = pygame.image.load("../assets/Items/nvl1.png").convert_alpha()
    ilvl11 = pygame.image.load("../assets/Items/nvl11.png").convert_alpha()
    ilvl2 = pygame.image.load("../assets/Items/nvl2.png").convert_alpha()
    ilvl22 = pygame.image.load("../assets/Items/nvl22.png").convert_alpha()
    ilvl3 = pygame.image.load("../assets/Items/nvl3.png").convert_alpha()
    ilvl33 = pygame.image.load("../assets/Items/nvl33.png").convert_alpha()
    back1 = pygame.image.load("../assets/Items/back.png").convert_alpha()
    back2 = pygame.image.load("../assets/Items/back1.png").convert_alpha()
    lvl1 = Button(ilvl1,ilvl11,200,720/2-100)
    lvl2 = Button(ilvl2,ilvl22,542,720/2-100)
    lvl3 = Button(ilvl3,ilvl33,888,720/2-100)
    back = Button(back1,back2,1050,50)
    cursor1 = Cursor()
    while salir!=True: #Loop principal
        for event in pygame.event.get(): #Corre todos los eventos en pygame
            if event.type == pygame.QUIT:
                salir=True
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(lvl1.rect):
                    objetive =fuente1.render("Obten 50 puntos en 30 segundos!",0,(0,0,0))
                    objetive2 =fuente2.render("Obten 50 puntos en 30 segundos!",0,(0,0,0))
                    Game(False,1,7,20,10,10,objetive,50,30,objetive2,music,sonido)
                if cursor1.colliderect(lvl2.rect):
                    objetive =fuente1.render("Obten 70 puntos en 35 segundos",0,(0,0,0))
                    objetive2 =fuente2.render("Obten 70 puntos en 35 segundos",0,(0,0,0))
                    Game(False,1,5,20,15,15,objetive,70,35,objetive2,music,sonido)
                if cursor1.colliderect(lvl3.rect):
                    objetive =fuente1.render("Obten 100 puntos en 30 segundos",0,(0,0,0))
                    objetive2 =fuente2.render("Obten 100 puntos en 30 segundos",0,(0,0,0))
                    Game(False,1,5,25,20,20,objetive,100,30,objetive2,music,sonido)
                if cursor1.colliderect(back.rect):
                    salir=True

        cursor1.update()
        ventana.fill(naranjita)
        lvl1.update(ventana,cursor1)
        lvl2.update(ventana,cursor1)
        lvl3.update(ventana,cursor1)
        back.update(ventana,cursor1)
        pygame.display.update()
