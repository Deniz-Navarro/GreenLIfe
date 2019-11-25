import pygame,sys
from random import randint
from pygame.locals import *
import time
import threading
global seconds
seconds = 0
class Character(pygame.sprite.Sprite):
    def __init__(self,lifes):
        pygame.sprite.Sprite.__init__(self)
        self.ipersonaje = pygame.image.load("../assets/Personajes/Principal/mov.png").convert_alpha()
        self.rect= self.ipersonaje.get_rect()
        self.rect.top = 720/2
        self.rect.left = 1280/2
        self.lifes = lifes
        self.points = 0
        self.salto = False
        segundos = "0"

    def draw(self,surface): #Draw Character
        surface.blit(self.ipersonaje,self.rect)

    def move(self,event,termino): #Player move
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.rect.top == 360:
                        self.salto = True

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.salto = False

    def drawl(self,surface,fuente): #Draw Lifes
        lifess = str(self.lifes)
        clifes=fuente.render("Lifes: "+lifess,0,(0,0,0))
        surface.blit(clifes,(100,650))

    def drawp(self,surface,fuente): #Draw Points
        pointss = str(self.points)
        cpoints=fuente.render("Points: "+pointss,0,(0,0,0))
        surface.blit(cpoints,(1280/2,650))

    def win(self,surface,fuente): #Draw Win
        lectura=fuente.render("You Win",0,(0,0,0))
        surface.blit(lectura,(1280/2-200,720/2-200))

    def lose(self,surface,fuente): #Draw Lose
        lectura=fuente.render("You Lose",0,(0,0,0))
        surface.blit(lectura,(1280/2-200,720/2-200))

class Enemy(pygame.sprite.Sprite):
    def __init__(self,speed):
        pygame.sprite.Sprite.__init__(self)
        self.iciclista = pygame.image.load("../assets/Items/piedra.png").convert_alpha()
        self.rect= self.iciclista.get_rect()
        self.rect.top = 425
        self.rect.left = 1450
        self.speed = speed


    def draw(self,surface): #Enemy Draw
        surface.blit(self.iciclista,self.rect)

    def collision(self,player): #Enemy Collision
        (xr,yr)=(player.rect.left,player.rect.top)
        self.rect.left -= self.speed
        if self.rect.colliderect(player.rect):
            (player.rect.left,player.rect.top)=(xr,yr)
            self.rect.left= 1450
            self.rect.top = 425
            global seconds
            seconds += 5
        if self.rect.left <= -20:
            self.rect.left= 1450
            self.rect.top = 425

class Object(pygame.sprite.Sprite):
    def __init__(self,speed,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.iobject = imagen
        self.rect= self.iobject.get_rect()
        self.rect.top = randint(160,400)
        self.rect.left = randint(1280,1500)
        self.speed = speed


    def draw(self,surface): #Enemy Draw
        surface.blit(self.iobject,self.rect)

    def collision(self,player,points): #Enemy Collision
        (xr,yr)=(player.rect.left,player.rect.top)
        self.rect.left -= self.speed
        if self.rect.colliderect(player.rect):
            (player.rect.left,player.rect.top)=(xr,yr)
            self.rect.top = randint(200,400)
            self.rect.left = randint(1280,2000)
            player.points+=points
        if self.rect.left <= -40:
            self.rect.top = randint(200,400)
            self.rect.left = randint(1280,2000)
            player.lifes -= 1

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

class Button(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x,y):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
    def update(self,surface,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal

        surface.blit(self.imagen_actual,self.rect)

def Game(endgame,fondo,life,venemy,vobject1,vobject2,goal,pointsg,tlimit,goal2):
    ss = 0
    def crono():
        if endgame == False:
            global seconds
            seconds +=1
            time.sleep(1)
            return crono()
    pygame.init() #Initialize pygame modules
    ventana=pygame.display.set_mode([1280,720])
    pygame.display.set_caption("GREEN LIFE")
    #Variables
    termino = False
    win=False
    reloj1=pygame.time.Clock()
    fuente1 = pygame.font.SysFont ("Arial",30,True,False)
    fuente2 = pygame.font.SysFont ("Arial",100,True,False)
    texto1= goal
    texto2=goal2
    rojo=(200,20,50)
    verde=(50,205,50)
    blanco=(255,255,255)
    altlimit = False
    cx = 1300
    #Images
    if fondo == 1:
        ifondo = pygame.image.load("../assets/Fondos/esc11.png").convert_alpha()

    if fondo == 2:
        ifondo = pygame.image.load("../assets/Fondos/esc2.png").convert_alpha()
    ipapel = pygame.image.load("../assets/Items/papel.png").convert_alpha()
    iperiodico = pygame.image.load("../assets/Items/periodico.png").convert_alpha()
    ciclista = pygame.image.load("../assets/Personajes/NPC/ciclista.png").convert_alpha()
    #Calling Classes
    player = Character(life)
    piedra = Enemy(venemy)
    objeto = Object(vobject1,ipapel)
    objeto2 = Object(vobject2,iperiodico)
    if endgame!=True:
        hilo = threading.Thread(target=crono, args=())
        hilo.start()
    while ss <= 5:
        if ss <= 3:
            ventana.fill(blanco)
            ventana.blit(texto2,(200,720/2))
        else:
            ventana.fill(rojo )
            lectura=fuente2.render("Listo!",0,(0,0,0))
            ventana.blit(lectura,(1280/2-200,720/2))
        lectura=fuente1.render("Presiona espacio para omitir",0,(0,0,0))
        ventana.blit(lectura,(1280/2-200,720-50))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ss = 5
        ss +=1
        time.sleep(1)
        pygame.display.update()
    global seconds
    seconds = 0
    while endgame!=True: #Loop principal
        for event in pygame.event.get(): #Corre todos los eventos en pygame
            if event.type == pygame.QUIT:
                endgame=True
                seconds = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    endgame=True
                    seconds = 0
            player.move(event,termino)
        if player.salto == True and player.rect.top >= 160 and altlimit == False:
            player.rect.top -=40
        if player.salto == False and player.rect.top < 720/2 and altlimit == False:
            player.rect.top +=40
        if player.rect.top == 120:
            altlimit = True
        if player.rect.top == 720/2:
            altlimit = False
        if altlimit == True and player.rect.top < 720/2:
            player.rect.top += 40
        if fondo==1:
            if seconds>tlimit/3 and seconds<=tlimit/3 *2:
                ifondo = pygame.image.load("../assets/Fondos/esc12.png").convert_alpha()
            if seconds>tlimit/3*2 and seconds<tlimit:
                ifondo = pygame.image.load("../assets/Fondos/esc13.png").convert_alpha()
        if fondo==2:
            if seconds>tlimit/3 and seconds<=tlimit/3 *2:
                ifondo = pygame.image.load("../assets/Fondos/esc21.png").convert_alpha()
            if seconds>tlimit/3*2 and seconds<tlimit:
                ifondo = pygame.image.load("../assets/Fondos/esc22.png").convert_alpha()

        #Chronometer
        if termino == False:
            segundos= str(seconds)

        reloj1.tick(15) #Frame Counter
        #End Game
        if termino == False:
            piedra.collision(player)
            objeto.collision(player,5)
            objeto2.collision(player,10)
            cx -= 20
            if cx <= -1300:
                cx = 1300
        #Draw on the surface
        ventana.blit(ifondo,(0,0))
        ventana.blit(ciclista,(cx,300))
        player.draw(ventana)
        player.drawl(ventana,fuente1)
        player.drawp(ventana,fuente1)
        ventana.blit(texto1,(50,20))
        chronometer=fuente1.render(segundos,0,(0,0,0))
        ventana.blit(chronometer,(1200,650)) #Draw Chronometer
        piedra.draw(ventana)
        objeto.draw(ventana)
        objeto2.draw(ventana)
        #Lose Condition
        if win == False:
            if player.lifes == 0 or seconds >= tlimit:
                termino = True
                ventana.fill(rojo)
                player.lose(ventana,fuente2)
        #Win Condition
        if player.points >= pointsg and seconds < tlimit or win == True:
            termino = True
            ventana.fill(verde)
            player.win(ventana,fuente2)
            win = True
        if endgame == True:
            seconds = 0
        pygame.display.update()
