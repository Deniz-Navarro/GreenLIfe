import pygame,sys
from random import randint
from pygame.locals import *
from juego import *
from worlds import *
def menu():
    pygame.init()
    ventana=pygame.display.set_mode([1280,720])
    salir=False
    fuente1 = pygame.font.SysFont ("Arial",30,True,False)
    black = (0,0,0)
    reloj1=pygame.time.Clock()
    menu = pygame.mixer.music.load("../assets/Sounds/menu.mp3")
    menu = pygame.mixer.music.play()
    mundo1 = pygame.image.load("../assets/Items/mundo1.png").convert_alpha()
    #mundo11 = pygame.image.load("../assets/Items/mundo11.png").convert_alpha()
    #mundo2 = pygame.image.load("../assets/Items/mundo2.png").convert_alpha()
    #mundo22 = pygame.image.load("../assets/Items/mundo22.png").convert_alpha()
    ifondo = pygame.image.load("../assets/Fondos/Menu.png").convert_alpha()
    start1 = pygame.image.load("../assets/Items/botons1.png").convert_alpha()
    start2 = pygame.image.load("../assets/Items/botons2.png").convert_alpha()
    equis1 = pygame.image.load("../assets/Items/equis.png").convert_alpha()
    equis2 = pygame.image.load("../assets/Items/equis1.png").convert_alpha()
    icon = pygame.image.load("../assets/Items/configuracion.png").convert_alpha()
    icon1 = pygame.image.load("../assets/Items/configuracion1.png").convert_alpha()
    start = Button(start1,start2,1280/2-100,720/2-225)
    config = Button(icon,icon1,600,425)
    equis = Button(equis1,equis2,600,575)
    cursor1 = Cursor()
    while salir!=True: #Loop principal
        for event in pygame.event.get(): #Corre todos los eventos en pygame
            if event.type == pygame.QUIT:
                salir=True
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(start.rect):
                    munditos(menu)
                if cursor1.colliderect(config.rect):
                    mopciones(menu)
                if cursor1.colliderect(equis.rect):
                    salir=True
                    pygame.quit()
                    sys.exit()

        cursor1.update()
        ventana.fill(black)
        ventana.blit(ifondo,(0,0))
        start.update(ventana,cursor1)
        equis.update(ventana,cursor1)
        config.update(ventana,cursor1)
        pygame.display.update()

def mopciones(menu):
    pygame.init()
    ventana=pygame.display.set_mode([1280,720])
    salir=False
    fuente1 = pygame.font.SysFont ("Arial",30,True,False)
    fuente2 = pygame.font.SysFont ("Arial",60,True,False)
    blanco = (179,19,176)
    reloj1=pygame.time.Clock()
    ifondo = pygame.image.load("../assets/Fondos/opciones.png").convert_alpha()
    isound = pygame.image.load("../assets/Items/sonidoh.png").convert_alpha()
    isound2 = pygame.image.load("../assets/Items/sonidoh1.png").convert_alpha()
    isoundd = pygame.image.load("../assets/Items/soundd.png").convert_alpha()
    isoundd2 = pygame.image.load("../assets/Items/sonidod1.png").convert_alpha()
    cursor1 = Cursor()
    sonidoh = Button(isound,isound2,450,720/2-150)
    sonidod = Button(isoundd,isoundd2,700,720/2-150)
    ssonidoh = Button(isound,isound2,450,720/2)
    ssonidod = Button(isoundd,isoundd2,700,720/2)
    while salir!=True: #Loop principal
        for event in pygame.event.get(): #Corre todos los eventos en pygame
            if event.type == pygame.QUIT:
                salir=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cursor1.colliderect(sonidoh.rect):
                if menu == pygame.mixer.music.stop():
                    menu = pygame.mixer.music.play()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cursor1.colliderect(sonidod.rect):
                menu = pygame.mixer.music.stop()



        cursor1.update()
        ventana.blit(ifondo,(0,0))
        sonidoh.update(ventana,cursor1)
        sonidod.update(ventana,cursor1)
        ssonidoh.update(ventana,cursor1)
        ssonidod.update(ventana,cursor1)
        pygame.display.update()

menu()
